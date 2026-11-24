# ______________________________________________________________________________
#
# Builds the dataset used by index.html:
# - every system entering the TOP10 for the first time (date, Rmax, name...)
# - CPU vendor share of the TOP500 (number of systems and Rmax) per list
# - GPU / accelerator vendor share of the TOP500 per list
#
# Vendors are inferred from the free-text <computer> field of the TOP500 XML.
# Usage:
#   python3 build_infographic_data.py --db DIR [-v]
# DIR holds the TOP500_*_all.xml files (or set the TOP500_DB environment
# variable instead of passing --db).
# ______________________________________________________________________________

import glob
import json
import re
import statistics
import sys
import collections
import os
import xml.etree.ElementTree as ET

from tech_catalog import TECH_CATALOG, DEVICE_FP64
from everyday_devices import EVERYDAY_DEVICES

HERE = os.path.dirname(os.path.abspath(__file__))


def db_dir():
    if "--db" in sys.argv:
        i = sys.argv.index("--db")
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    elif os.environ.get("TOP500_DB"):
        return os.environ["TOP500_DB"]
    sys.exit("Usage: python3 build_infographic_data.py --db DIR [-v]\n"
             "DIR: folder holding the TOP500_*_all.xml files "
             "(or set TOP500_DB)")


NS = {"t": "http://www.top500.org/xml/top500/1.0"}

# ------------------------------------------------------------------------------
# CPU classification: (vendor, [regex...]) evaluated in order, first match wins
# ------------------------------------------------------------------------------

CPU_RULES = [
    ("Fujitsu", [r"a64fx", r"sparc64", r"\bfx10\b", r"\bfx100\b", r"\bfx700\b", r"monaka",
                 r"\bvpp\d+", r"\bvpp", r"primepower", r"fujitsu\s+(sparc|vpp)"]),
    ("NVIDIA", [r"\bgrace\b", r"\bgh200\b", r"\bgb200\b", r"\bgb300\b", r"\bvera\b"]),
    ("AMD", [r"opteron", r"\bxt[3-6]", r"\bxe6\b", r"\bxk[67]\b", r"epyc", r"\bathlon\b", r"mi300a"]),
    ("Intel", [r"xeon", r"\b[lxe]5[3-6][\dx]{2}\b", r"\be5-\d{4}", r"bl2x220", r"x6275", r"primergy rx200", r"itanium", r"pentium", r"\bi860\b", r"paragon",
               r"\bxp/s", r"ipsc", r"\bcore i\d", r"\bnehalem", r"\bxeon phi", r"knights",
               r"\bem64t", r"\bia-?64", r"\bia-?32", r"\bsgi altix", r"\baltix",
               r"\bicx\b"]),
    ("IBM", [r"\bpower\s?\d", r"\bpower\b", r"powerpc", r"\bppc", r"blue ?gene", r"bluegene",
             r"\bsp\d?\b", r"\brs/?6000", r"\bp\d{3}\b", r"\bp5\b", r"cell\b", r"powerxcell",
             r"\bjs\d{2}", r"\bqs\d{2}", r"eserver", r"\bpseries", r"\bp690",
             r"\bsp power", r"\bsp2\b", r"\bsp3\b", r"\bsp4\b"]),
    # Chinese designs (after Intel: some "Sunway" clusters are Xeon based)
    ("Chinese CPUs (Sunway, Phytium, Hygon, LX2…)", [
        r"sunway", r"sw26010", r"shenwei", r"phytium", r"ft-?1500", r"ft-?2000",
        r"hygon", r"\bc86\b", r"\blx2\b", r"lingkun", r"godson", r"loongson"
    ]),
    ("NEC (vector)", [r"\bsx-?\d", r"\bsx-?aurora", r"\bsx\b", r"\bnec\b"]),
    ("Cray (vector)", [r"\bt90\b", r"\bc90\b", r"\bj90\b", r"\by-mp",
                          r"\bymp\b", r"\bsv1\b", r"\bsv1ex\b", r"\bx1\b", r"\bx1e\b", r"\bt94\b",
                          r"\bt916\b", r"\bt932\b", r"\bc916\b", r"\bc94\b", r"\bc98\b",
                          r"\bcray x1", r"\bcray-?2", r"\bx-mp",
                          r"\bt9\d\b", r"\bc9\d\b", r"\bj9\d\b", r"\bx2\b"]),
    ("DEC / Compaq Alpha", [r"alpha", r"\bt3d\b", r"\bt3e", r"alphaserver", r"\bes\d{2}\b", r"\bgs\d{3}\b",
                            r"\bsc\d{2}\b", r"\bsc45\b", r"\bsc40\b", r"\bdec\b", r"compaq\b(?!.*xeon)"]),
    ("HP PA-RISC", [r"pa-?risc", r"pa\d{4}", r"\bspp\d+", r"exemplar", r"superdome(?!.*itanium)",
                    r"\bhp 9000", r"\brp\d{4}", r"\bv2[25]\d0\b", r"\bn4000\b", r"\bsuperdome\b",
                    r"\bconvex", r"\bc3\d{3}\b", r"\bv-class", r"\bx-class", r"\bs-class"]),
    ("SGI / MIPS", [r"origin", r"\bmips", r"\br1\d000", r"power challenge", r"challenge",
                    r"\bonyx", r"\bpower ?onyx", r"\bsgi\b"]),
    ("Sun SPARC", [r"\bsun\b(?!.*(opteron|xeon|amd|intel))", r"ultrasparc", r"\bhpc\s?\d{4,5}\b",
                   r"\be10000\b", r"\bstarfire", r"\bsunfire", r"sun fire(?!.*(x4|opteron|xeon))",
                   r"\bf15k\b", r"\bf6800\b", r"\bsparc"]),
    ("Hitachi", [r"\bsr\d{4}", r"hitachi", r"\bs-3800", r"\bs-?3\d{3}"]),
    ("Thinking Machines", [r"\bcm-?5", r"\bcm-?200", r"\bcm-?2\b", r"thinking"]),
    ("Arm (others)", [r"\barm\b", r"thunderx", r"cavium", r"marvell", r"graviton", r"kunpeng",
                      r"ampere altra", r"\baltra\b", r"rhea"]),
    ("Chinese CPUs (Sunway, Phytium, Hygon, LX2…)", [r"matrix-2000"]),
    # Clusters described only by their node model or clock (2000s)
    ("Intel", [r"poweredge", r"\bp4\b", r"\bpiii\b", r"pentium", r"\bx5\d{2}x?\b", r"\bx54xx",
               r"\be54xx", r"bullx", r"novascale", r"\bqc ht\b", r"\bprecision \d{3}"]),
    ("IBM", [r"xserve", r"\bg5\b", r"powerplus"]),
    ("DEC / Compaq Alpha", [r"\bev6\d", r"cplant", r"avalon"]),
    # Generic vendor names, only when nothing more specific matched
    ("AMD", [r"\bamd\b"]),
    ("Intel", [r"\bintel\b"]),
    ("IBM", [r"\bibm\b"]),
]

# ------------------------------------------------------------------------------
# GPU / accelerator classification
# ------------------------------------------------------------------------------

GPU_RULES = [
    ("NVIDIA", [r"nvidia", r"tesla", r"\bv100\b", r"\bp100\b", r"\ba100\b", r"\bh100\b", r"\bh200\b",
                r"\bgh200\b", r"\bgb200\b", r"\bgb300\b", r"\bb200\b", r"\bb300\b", r"\bk20x?\b",
                r"\bk40\b", r"\bk80\b", r"\bm2050\b", r"\bm2070\b", r"\bm2090\b", r"\bc2050\b",
                r"\bc2070\b", r"\bc2090\b", r"\bc1060\b", r"\bs1070\b", r"\bvolta\b", r"\bampere\b",
                r"\bhopper\b", r"\bblackwell\b", r"\bgv100\b", r"\bl40s?\b", r"\ba40\b", r"\ba30\b",
                r"\bt4\b", r"\bgtx", r"\bquadro", r"\brtx", r"\bxk\d", r"\bpascal\b", r"\bkepler\b"]),
    ("AMD", [r"instinct", r"\bmi\d{2,3}[a-z]?\b", r"radeon", r"firepro", r"\bati\b", r"\bvega\b",
             r"\bamd gpu", r"\bmi300a\b"]),
    ("Intel", [r"xeon phi", r"knights corner", r"\bmic\b", r"data center gpu max", r"ponte vecchio",
               r"intel gpu", r"\b5110p\b", r"\b7120p\b", r"\b31s1p\b", r"\bknc\b"]),
    ("Chinese accelerators (Matrix-2000, DCU, MetaX, LingQi…)", [r"matrix-?2000", r"lingqi", r"\bdcu\b", r"deep computing processor", r"metax"]),
    ("PEZY", [r"pezy"]),
    ("Others (Cell, NEC VE, MN-Core…)", [r"powerxcell", r"\bcell\b", r"clearspeed", r"\bgrape",
                                         r"\bmn-?core", r"\bsx-?aurora\s*tsubasa", r"vector engine",
                                         r"\bgpu\b", r"\baccelerator"]),
]

# Display groups (stacked areas): detailed vendors are folded into at most
# 8 coloured groups + "Others" so that the categorical palette stays readable.
CPU_GROUPS = {
    "Intel": ["Intel"],
    "AMD": ["AMD"],
    "IBM": ["IBM"],
    "NVIDIA": ["NVIDIA"],
    "Fujitsu": ["Fujitsu"],
    "Vector (Cray, NEC, Hitachi)": ["Cray (vector)", "NEC (vector)", "Hitachi"],
    "RISC Unix (Alpha, PA-RISC, MIPS, SPARC)": ["DEC / Compaq Alpha", "HP PA-RISC", "SGI / MIPS", "Sun SPARC"],
    "China": ["Chinese CPUs (Sunway, Phytium, Hygon, LX2…)"],
    "Others": ["Thinking Machines", "Arm (others)", "Others"],
}
GPU_GROUPS = {
    "NVIDIA": ["NVIDIA"],
    "AMD": ["AMD"],
    "Intel": ["Intel"],
    "China": ["Chinese accelerators (Matrix-2000, DCU, MetaX, LingQi…)"],
    "Others": ["PEZY", "Others (Cell, NEC VE, MN-Core…)"],
}

# Free-standing Xeon Phi (KNL, self-hosted) is a CPU, not an accelerator.
KNL_PATTERN = re.compile(r"xeon phi\s*7\d{3}|knights landing|\bknl\b", re.I)


def match(rules, text):
    for vendor, patterns in rules:
        for p in patterns:
            if re.search(p, text, re.I):
                return vendor
    return None


def classify_cpu(computer, manufacturer):
    v = match(CPU_RULES, computer)
    if v:
        return v
    # Fallback on the manufacturer field for the early lists
    m = (manufacturer or "").lower()
    fallback = {
        "intel": "Intel", "ibm": "IBM", "cray": "Cray (vector)", "nec": "NEC (vector)",
        "fujitsu": "Fujitsu", "hitachi": "Hitachi", "sgi": "SGI / MIPS",
        "silicon graphics": "SGI / MIPS", "thinking machines": "Thinking Machines",
        "hewlett-packard": "HP PA-RISC", "hp": "HP PA-RISC", "convex": "HP PA-RISC",
        "sun": "Sun SPARC", "digital": "DEC / Compaq Alpha", "compaq": "DEC / Compaq Alpha",
        "meiko": "Others", "kendall square": "Others", "parsytec": "Others", "nCUBE".lower(): "Others",
        "maspar": "Others",
    }
    for k, val in fallback.items():
        if k in m:
            return val
    return "Others"


def classify_gpu(computer):
    text = KNL_PATTERN.sub("", computer)
    return match(GPU_RULES, text)


# ------------------------------------------------------------------------------
# Parsing
# ------------------------------------------------------------------------------

def text(site, tag):
    v = site.findtext("t:" + tag, default="", namespaces=NS)
    return (v or "").strip()


def power_kw(site):
    try:
        v = float(text(site, "power") or 0)
    except ValueError:
        v = 0
    return v if v > 0 else None


def main():
    db = db_dir()
    files = sorted(glob.glob(os.path.join(db, "TOP500_*_all.xml")))
    if not files:
        sys.exit("No TOP500_*_all.xml found in " + db)
    lists = []
    seen_top10 = set()
    newcomers = []
    unknown_cpu = collections.Counter()
    tech_re = [re.compile(rx, re.I) for _, _, _, rx in TECH_CATALOG]
    tech_first = {}   # tech index -> first appearance record
    tech_counts = collections.defaultdict(dict)  # tech index -> {date: nb systems}

    for f in files:
        stamp = re.search(r"TOP500_(\d{4})(\d{2})", f)
        year, month = int(stamp.group(1)), int(stamp.group(2))
        date = f"{year}.{month:02d}"
        root = ET.parse(f).getroot()
        sites = root.findall("t:site", NS)

        cpu_count = collections.Counter()
        cpu_rmax = collections.Counter()
        gpu_count = collections.Counter()
        gpu_rmax = collections.Counter()
        total_rmax = 0.0

        for s in sites:
            rank = int(text(s, "rank"))
            computer = text(s, "computer")
            manufacturer = text(s, "manufacturer")
            rmax = float(text(s, "r-max") or 0)
            total_rmax += rmax

            cpu = classify_cpu(computer, manufacturer)
            if cpu == "Others":
                unknown_cpu[(computer, manufacturer)] += 1
            cpu_count[cpu] += 1
            cpu_rmax[cpu] += rmax

            for k, rx in enumerate(tech_re):
                if rx.search(computer):
                    tech_counts[k][date] = tech_counts[k].get(date, 0) + 1
                    if k not in tech_first:  # sites are sorted by rank
                        tech_first[k] = {
                            "date": date, "rank": rank, "computer": computer,
                            "name": (text(s, "system-name") or computer.split(",")[0]).split(" - ")[0].strip(),
                            "site": text(s, "installation-site/t:installation-site-name"),
                            "country": text(s, "country"),
                            "rmax": rmax,  # GFlop/s
                            "rpeak": float(text(s, "r-peak") or 0),
                        }

            gpu = classify_gpu(computer)
            if gpu:
                gpu_count[gpu] += 1
                gpu_rmax[gpu] += rmax

            if rank <= 10:
                # An upgraded machine often gets a new system-id: a system is
                # considered new only if both its id and its (site, name) are new.
                sid = text(s, "system-id")
                name = (text(s, "system-name") or computer.split(",")[0]).split(" - ")[0].strip()
                site = text(s, "installation-site/t:installation-site-name")
                key = (site.lower(), name.lower())
                if sid not in seen_top10 and key not in seen_top10:
                    seen_top10.update([sid, key])
                    newcomers.append({
                        "date": date,
                        "rank": rank,
                        "name": name,
                        "computer": computer,
                        "manufacturer": manufacturer,
                        "site": text(s, "installation-site/t:installation-site-name"),
                        "country": text(s, "country"),
                        "rmax": rmax,  # GFlop/s
                        "rpeak": float(text(s, "r-peak") or 0),
                        "power": power_kw(s),  # kW, None if not reported
                        # technologies of the catalogue found in the description
                        "cpu_tech": [n for (_, kd, n, _), r in zip(TECH_CATALOG, tech_re) if kd == "cpu" and r.search(computer)],
                        "gpu_tech": [n for (_, kd, n, _), r in zip(TECH_CATALOG, tech_re) if kd == "gpu" and r.search(computer)],
                        "cpu": cpu,
                        "gpu": gpu,
                    })

        rmax_sorted = sorted((float(text(x, "r-max") or 0) for x in sites), reverse=True)
        # power (kW), only for the systems that report it (lists from June 2008)
        power = []
        for x in sites:
            try:
                v = float(text(x, "power") or 0)
            except ValueError:
                v = 0
            power.append(v)
        reported = [v for v in power if v > 0]
        lists.append({
            "date": date,
            "n": len(sites),
            "top1": rmax_sorted[0],
            "top10": rmax_sorted[9],
            "last": rmax_sorted[-1],  # Rmax of the #500
            # aggregate Rmax of the list (GFlop/s)
            "sum": total_rmax,
            "mean": total_rmax / len(sites),
            "median": statistics.median(rmax_sorted),
            # power of the systems reporting it, in kW (None before 2008)
            "power": {
                "n": len(reported),
                "sum": round(sum(reported), 1),
                "max": max(reported),
                "mean": round(sum(reported) / len(reported), 1),
                "median": statistics.median(reported),
                "top1": power[0] or None,
            } if reported else None,
            # vendor -> [number of systems, % of the TOP500 total Rmax]
            "cpu": {k: [cpu_count[k], round(100 * cpu_rmax[k] / total_rmax, 2)] for k in cpu_count},
            "gpu": {k: [gpu_count[k], round(100 * gpu_rmax[k] / total_rmax, 2)] for k in gpu_count},
        })

    techs = []
    for k, (lane, kind, name, _) in enumerate(TECH_CATALOG):
        if k not in tech_first:
            print("Technology never found:", name)
            continue
        counts = tech_counts[k]
        peak_date = max(counts, key=lambda d: (counts[d], d))
        techs.append({
            "lane": lane, "kind": kind, "name": name,
            "fp64": DEVICE_FP64.get(name, (None, ""))[0],  # GFlop/s, one device
            "fp64_ref": DEVICE_FP64.get(name, (None, ""))[1],
            "first": tech_first[k],
            "peak": [counts[peak_date], peak_date],
            "last": max(counts),
            "nlists": len(counts),
        })

    out = {
        "source": "TOP500 lists (top500.org), " + lists[0]["date"] + " – " + lists[-1]["date"],
        "cpu_groups": CPU_GROUPS,
        "gpu_groups": GPU_GROUPS,
        "lists": lists,
        "top10_newcomers": newcomers,
        "technologies": techs,
        "everyday": [
            {"date": d, "cat": c, "name": n, "gflops": g, "ref": r}
            for d, c, n, g, r in EVERYDAY_DEVICES
        ],
    }
    with open(os.path.join(HERE, "top500_infographic_data.json"), "w", encoding="utf8") as fh:
        json.dump(out, fh, ensure_ascii=False)

    # Inject the data into the self-contained HTML page (between the markers)
    html_path = os.path.join(HERE, "index.html")
    try:
        with open(html_path, encoding="utf8") as fh:
            html = fh.read()
        payload = json.dumps(out, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        html = re.sub(r"/\*DATA_START\*/.*?/\*DATA_END\*/",
                      lambda _: "/*DATA_START*/" + payload + "/*DATA_END*/", html, flags=re.S)
        with open(html_path, "w", encoding="utf8") as fh:
            fh.write(html)
        print("Data injected into", html_path)
    except FileNotFoundError:
        print(html_path, "not found: data not injected")

    if "-v" in sys.argv:
        print("Unclassified CPU entries:")
        for (c, m), n in unknown_cpu.most_common(60):
            print(f"{n:5d} | {m} | {c}")
    if "-v" in sys.argv:
        print("Technologies (first appearance):")
        for t in sorted(techs, key=lambda t: t["first"]["date"]):
            f = t["first"]
            print(f'{f["date"]} | {t["lane"][:10]:10} | {t["kind"]} | {t["name"]:38} | #{f["rank"]:3d} {f["computer"][:70]} | peak {t["peak"]}')
    print(f"{len(lists)} lists, {len(newcomers)} TOP10 newcomers, {len(techs)} technologies")


if __name__ == "__main__":
    main()
