# ______________________________________________________________________________
#
# Catalogue of processor and accelerator technologies tracked by the
# infographic ("Nouvelles technologies" chart).
#
# Each entry: (lane, kind, name, regex)
# - lane : vendor lane in the chart (same groups as the CPU share chart)
# - kind : "cpu" or "gpu" (accelerator)
# - name : label shown in the infographic
# - regex: matched (case-insensitive) against the <computer> field of every
#          system. Old lists describe the machine model rather than the chip,
#          so some patterns use the system model (e.g. ORIGIN 2000 -> R10000).
#
# The first TOP500 list in which at least one system matches gives the date of
# appearance of the technology.
# ______________________________________________________________________________

TECH_CATALOG = [
    # ---------------------------------------------------------------- Intel CPU
    ("Intel", "cpu", "i860 (Paragon)", r"paragon|xp/s|\bi860"),
    ("Intel", "cpu", "Pentium Pro", r"pentium pro|asci red"),
    ("Intel", "cpu", "Pentium III", r"pentium ?iii|\bpiii\b"),
    ("Intel", "cpu", "Pentium 4 / Xeon NetBurst", r"pentium ?4|\bp4\b|mcr linux cluster|aspen systems, dual xeon|xseries cluster xeon 2\.4|riken super combined cluster"),
    ("Intel", "cpu", "Itanium 2", r"itanium ?2|integrity superdome|altix (3[0-9]{3}|4[0-9]{3})|sgi altix [0-9.]+ ?ghz"),
    ("Intel", "cpu", "Xeon EM64T (Nocona)", r"em64t|poweredge 1850"),
    ("Intel", "cpu", "Xeon Woodcrest (51xx)", r"xeon[^,]*\b51[0-9]{2}\b|woodcrest|51xx"),
    ("Intel", "cpu", "Xeon Clovertown (53xx)", r"\b[ELX]53[0-9]{2}\b|xeon[^,]*\b53[0-9]{2}\b|clovertown|53xx|poweredge 1955, 2\.33"),
    ("Intel", "cpu", "Xeon Harpertown (54xx)", r"\b[ELX]54[0-9]{2}\b|harpertown|54xx"),
    ("Intel", "cpu", "Xeon Nehalem (55xx)", r"\b[ELWX]55[0-9]{2}\b|xeon[^,]*\b55[0-9]{2}\b|nehalem|55xx|bullx super-node s60[13]0"),
    ("Intel", "cpu", "Xeon Westmere (56xx)", r"\b[ELX]56[0-9]{2}\b|xeon[^,]*\b56[0-9]{2}\b|westmere|56xx"),
    ("Intel", "cpu", "Xeon Sandy Bridge (E5)", r"\bE5-[24]6(?!92)[0-9]{2}[lw]?\b(?!\s*v\d)|sandy ?bridge"),
    ("Intel", "cpu", "Xeon Ivy Bridge (E5 v2)", r"\bE5-[24]6[0-9]{2}[lw]?\s*v2|\bE5-2692\b|ivy ?bridge"),
    ("Intel", "cpu", "Xeon Haswell (E5 v3)", r"\bE5-[24]6[0-9]{2}[lw]?\s*v3|haswell"),
    ("Intel", "cpu", "Xeon Broadwell (E5 v4)", r"\bE5-[24]6[0-9]{2}[lw]?\s*v4|xeon d-15[0-9]{2}|broadwell"),
    ("Intel", "cpu", "Xeon Phi Knights Landing", r"xeon phi 72[0-9]{2}|knights landing|\bknl\b"),
    ("Intel", "cpu", "Xeon Skylake", r"(platinum|gold|silver) [0-9]1[0-9]{2}|skylake"),
    ("Intel", "cpu", "Xeon Cascade Lake", r"(platinum|gold|silver) [0-9]2[0-9]{2}|cascade ?lake"),
    ("Intel", "cpu", "Xeon Ice Lake", r"(platinum|gold|silver) [0-9]3[0-9]{2}|ice ?lake"),
    ("Intel", "cpu", "Xeon Sapphire Rapids", r"(platinum|gold|silver) [0-9]4[0-9]{2}|sapphire ?rapids"),
    ("Intel", "cpu", "Xeon CPU Max (HBM)", r"xeon cpu max"),
    ("Intel", "cpu", "Xeon Emerald Rapids", r"(platinum|gold|silver) [0-9]5[0-9]{2}|emerald ?rapids"),
    ("Intel", "cpu", "Xeon 6 (Granite Rapids)", r"xeon 6[0-9]{3}[pe]\b|granite ?rapids"),
    # ---------------------------------------------------------------- Intel GPU
    ("Intel", "gpu", "Xeon Phi Knights Corner", r"xeon phi (31s1p|5110p|5120d|se10|7120|3120)|xeon phi(?! ?72)"),
    ("Intel", "gpu", "Data Center GPU Max (Ponte Vecchio)", r"data center gpu max|ponte vecchio"),
    # ------------------------------------------------------------------ AMD CPU
    ("AMD", "cpu", "Opteron (K8)", r"opteron|cray xt[34],"),
    ("AMD", "cpu", "Opteron dual-core", r"opteron[^,]*(dual|\bdc\b)|dual ?core opteron"),
    ("AMD", "cpu", "Opteron Barcelona (quad-core)", r"opteron[^,]*(quad[ -]?core|\bqc\b|\b4c\b)|\bqc opteron|quad[ -]?core opteron|barcelona|xt4 quadcore|xt5[^,]*\bqc\b"),
    ("AMD", "cpu", "Opteron Istanbul (6-core)", r"opteron[^,]*(six|6c\b|24[0-9]{2})|istanbul|xt5-he"),
    ("AMD", "cpu", "Opteron Magny-Cours", r"opteron 61[0-9]{2}|magny|\b12-core\b|opteron[^,]*12 ?c|cray xe6 8-core"),
    ("AMD", "cpu", "Opteron Interlagos", r"opteron 62[0-9]{2}|interlagos|opteron[^,]*16 ?c"),
    ("AMD", "cpu", "EPYC Naples", r"epyc 7[0-9]{2}1\b|naples"),
    ("AMD", "cpu", "EPYC Rome", r"epyc 7[0-9v]{2}2\b|\brome\b|2nd gen(eration)? epyc"),
    ("AMD", "cpu", "EPYC Milan", r"epyc 7[0-9]{2}3x?\b|milan|3rd gen(eration)? epyc"),
    ("AMD", "cpu", "EPYC Genoa", r"epyc 9[0-9]{2}4x?\b|genoa|4th gen(eration)? epyc"),
    ("AMD", "cpu", "EPYC Turin", r"epyc 9[0-9]{2}5f?\b|\bturin\b|5th gen(eration)? epyc"),
    # ------------------------------------------------------------------ AMD GPU
    ("AMD", "gpu", "Radeon / FirePro", r"radeon|firepro|\bati\b"),
    ("AMD", "gpu", "Instinct MI50 / MI60", r"\bmi50\b|\bmi60\b|instinct mi[56]0"),
    ("AMD", "gpu", "Instinct MI100", r"\bmi100\b"),
    ("AMD", "gpu", "Instinct MI250X", r"\bmi250x?\b"),
    ("AMD", "gpu", "Instinct MI300A (APU)", r"\bmi300a\b"),
    ("AMD", "gpu", "Instinct MI300X", r"\bmi300x\b"),
    ("AMD", "gpu", "Instinct MI325X / MI355X", r"\bmi3[25]5x?\b"),
    # --------------------------------------------------------------- NVIDIA GPU
    ("NVIDIA", "gpu", "Tesla (GT200)", r"\bgt200\b|\bc1060\b|\bs1070\b|\bt10\b|tesla s10"),
    # "NVIDIA 2050" or a bare "NVIDIA GPU" on Tianhe-1A and TSUBAME 2.0 (Tesla M2050)
    ("NVIDIA", "gpu", "Fermi", r"\b[cm]20[5-9]0\b|nvidia 20[5-9]0\b|fermi|tianhe-1a.*nvidia gpu|tsubame 2\.0.*nvidia gpu|sl390s g7 xeon 6c x5670, nvidia gpu"),
    ("NVIDIA", "gpu", "Kepler", r"\bk20[xm]?\b|\bk40[mt]?\b|\bk80\b|nvidia kepler"),
    ("NVIDIA", "gpu", "Pascal (P100)", r"\bp100\b|pascal"),
    ("NVIDIA", "gpu", "Volta (V100)", r"\bv100\b|\bvolta\b|gv100"),
    ("NVIDIA", "gpu", "Ampere (A100)", r"\ba100\b|nvidia ampere"),
    ("NVIDIA", "gpu", "Hopper (H100 / GH200)", r"\bh100\b|\bh200\b|\bgh200\b|grace hopper|nvidia hopper"),
    ("NVIDIA", "gpu", "Blackwell (B200 / GB200)", r"\bg?b[23]00\b|blackwell"),
    # --------------------------------------------------------------- NVIDIA CPU
    ("NVIDIA", "cpu", "Grace (Arm)", r"\bgrace\b|\bgh200\b|gh superchip|\bgb200\b"),
    # ---------------------------------------------------------------------- IBM
    ("IBM", "cpu", "POWER2", r"power ?2\b|p2sc|\bsp2\b"),
    ("IBM", "cpu", "PowerPC 604", r"\b604e?\b|sp silver|sp powerpc"),
    ("IBM", "cpu", "POWER3", r"power ?3\b"),
    ("IBM", "cpu", "POWER4", r"power ?4\+?\b|p690|p655|p630|pseries 6[39]0|pseries 655"),
    ("IBM", "cpu", "PowerPC 970", r"ppc ?970|powerpc 970|\bg5\b|\bjs2[01]\b|xserve"),
    ("IBM", "cpu", "PowerPC 440 (Blue Gene/L)", r"blue ?gene/l|bluegene/l|powerpc 440|blue gene solution"),
    ("IBM", "cpu", "POWER5", r"power ?5\+?\b|\bp5\b|p575(?!.*p6)"),
    ("IBM", "gpu", "PowerXCell 8i", r"powerxcell|\bcell\b|\bqs2[12]\b"),
    ("IBM", "cpu", "PowerPC 450 (Blue Gene/P)", r"blue ?gene/p|bluegene/p|powerpc 450"),
    ("IBM", "cpu", "POWER6", r"power ?6\b|\bp6\b"),
    ("IBM", "cpu", "POWER7", r"power ?7\b"),
    ("IBM", "cpu", "Power BQC (Blue Gene/Q)", r"blue ?gene/q|power bqc"),
    ("IBM", "cpu", "POWER8", r"power ?8\b"),
    ("IBM", "cpu", "POWER9", r"power ?9\b"),
    ("IBM", "cpu", "POWER10", r"power ?10\b"),
    # ------------------------------------------------------------------ Fujitsu
    ("Fujitsu", "cpu", "VPP500 (vector)", r"vpp500|numerical wind tunnel"),
    ("Fujitsu", "cpu", "VPP300 / VPP700", r"vpp[37]00"),
    ("Fujitsu", "cpu", "VPP5000", r"vpp5000"),
    ("Fujitsu", "cpu", "SPARC64 V", r"primepower|sparc64 v\b"),
    ("Fujitsu", "cpu", "SPARC64 VII", r"sparc64 vii\b"),
    ("Fujitsu", "cpu", "SPARC64 VIIIfx (K)", r"viiifx|k computer"),
    ("Fujitsu", "cpu", "SPARC64 IXfx", r"ixfx"),
    ("Fujitsu", "cpu", "SPARC64 XIfx", r"xifx"),
    ("Fujitsu", "cpu", "A64FX (Arm)", r"a64fx"),
    # -------------------------------------------------------------------- China
    ("China", "cpu", "ShenWei SW1600", r"sw1600|shenwei"),
    ("China", "cpu", "Loongson / Godson", r"loongson|godson"),
    ("China", "cpu", "Phytium FT-1500 / FT-2000", r"ft-?1500|ft-?2000|phytium"),
    ("China", "cpu", "Sunway SW26010", r"sw26010(?!.?pro)"),
    ("China", "gpu", "Matrix-2000", r"matrix-?2000"),
    ("China", "cpu", "Hygon Dhyana / C86", r"hygon|\bc86\b"),
    ("China", "gpu", "Hygon DCU", r"deep computing processor|\bdcu\b"),
    ("China", "cpu", "Sunway SW26010-Pro", r"sw26010.?pro"),
    ("China", "gpu", "MetaX", r"metax"),
    ("China", "cpu", "LX2 (LingKun)", r"\blx2\b|lingkun"),
    # --------------------------------------------------------------- Vector
    ("Vector (Cray, NEC, Hitachi)", "cpu", "Cray T90", r"\bt9[0-9]{1,2}\b|\bt90\b"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "Cray J90", r"\bj9[0-9]{1,2}"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "Cray SV1", r"\bsv1"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "Cray X1", r"\bx1e?\b(?!000)|cray x1"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "NEC SX-4", r"sx-?4"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "NEC SX-5", r"sx-?5"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "NEC SX-6 (Earth Simulator)", r"sx-?6|earth-simulator|earth simulator"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "NEC SX-8", r"sx-?8"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "NEC SX-9", r"sx-?9"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "NEC SX-ACE", r"sx-?ace"),
    ("Vector (Cray, NEC, Hitachi)", "gpu", "NEC SX-Aurora (Vector Engine)", r"sx-?aurora|vector engine"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "Hitachi SR2201", r"sr2201|cp-pacs"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "Hitachi SR8000", r"sr8000"),
    ("Vector (Cray, NEC, Hitachi)", "cpu", "Hitachi SR11000", r"sr11000"),
    # ---------------------------------------------------------------- RISC Unix
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "Alpha 21064 (Cray T3D)", r"\bt3d\b"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "Alpha 21164 (EV5)", r"alphaserver 8[24]00|\bt3e|21164|\bev56?\b"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "Alpha 21264 (EV6)", r"ev6[78]?\b|21264|es40|alphaserver sc|\bsc4[05]\b"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "MIPS R8000 (POWER CHALLENGE)", r"power ?challenge(?! ?10000)|r8000"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "MIPS R10000 (ORIGIN 2000)", r"r10000|origin ?2000|challenge ?10000|blue mountain"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "MIPS R12000 / R14000 (ORIGIN 3000)", r"r1[24]000|origin ?3000"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "UltraSPARC", r"ultrasparc(?! ?iii)|ultra (enterprise|hpc)|\bhpc ?10000\b|starfire|e10000"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "UltraSPARC III", r"ultrasparc ?iii|sun fire ?(15k|6800|25k)|\bf15k\b"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "PA-RISC 7x00 (SPP)", r"\bspp[0-9]{3,4}|exemplar s"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "PA-8000 (Exemplar X)", r"exemplar x|\bspp2000|\bv2[25]00\b|\bv-class"),
    ("RISC Unix (Alpha, PA-RISC, MIPS, SPARC)", "cpu", "PA-8x00 (SuperDome)", r"superdome(?![^,]*(itanium|integrity))"),
    # ------------------------------------------------------------------- Others
    ("Others", "cpu", "Arm ThunderX2", r"thunderx2"),
    ("Others", "cpu", "Arm Kunpeng / Graviton", r"kunpeng|graviton"),
    ("Others", "gpu", "ClearSpeed", r"clearspeed"),
    ("Others", "gpu", "GRAPE-DR", r"grape-?dr"),
    ("Others", "gpu", "PEZY-SC", r"pezy"),
    ("Others", "gpu", "MN-Core", r"mn-?core"),
]

# ______________________________________________________________________________
#
# Peak FP64 performance of ONE device (chip, or package for multi-die parts),
# in GFlop/s, from vendor specifications. The variant is, where possible, the
# one used by the first TOP500 system in which the technology appears (clock
# and core count read from the <computer> field). For GPUs and accelerators the
# vector FP64 figure is used (matrix / tensor units excluded).
# These are approximate reference values for the infographic; None means no
# reliable public FP64 figure, and the technology is then not plotted.
# ______________________________________________________________________________

DEVICE_FP64 = {
    # name: (GFlop/s, basis)
    # Intel
    "i860 (Paragon)": (0.075, "i860 XP 50 MHz"),
    "Pentium Pro": (0.2, "200 MHz"),
    "Pentium III": (0.8, "800 MHz"),
    "Pentium 4 / Xeon NetBurst": (3.4, "1.7 GHz, SSE2"),
    "Itanium 2": (3.6, "900 MHz"),
    "Xeon EM64T (Nocona)": (6.4, "3.2 GHz"),
    "Xeon Woodcrest (51xx)": (24, "2 cores, 3.0 GHz"),
    "Xeon Clovertown (53xx)": (37.3, "4 cores, 2.33 GHz"),
    "Xeon Harpertown (54xx)": (48, "4 cores, 3.0 GHz"),
    "Xeon Nehalem (55xx)": (46.9, "X5570, 4 cores, 2.93 GHz"),
    "Xeon Westmere (56xx)": (63.8, "X5650, 6 cores, 2.66 GHz"),
    "Xeon Sandy Bridge (E5)": (166.4, "8 cores, 2.6 GHz, AVX"),
    "Xeon Ivy Bridge (E5 v2)": (211.2, "E5-2692 v2 (Tianhe-2), 12 cores, 2.2 GHz"),
    "Xeon Haswell (E5 v3)": (480, "E5-2680 v3, 12 cores, 2.5 GHz, AVX2"),
    "Xeon Broadwell (E5 v4)": (604.8, "E5-2695 v4, 18 cores, 2.1 GHz"),
    "Xeon Phi Knights Landing": (3046.4, "7250, 68 cores, 1.4 GHz"),
    "Xeon Skylake": (1612.8, "Platinum 8160, 24 cores, 2.1 GHz, AVX-512"),
    "Xeon Cascade Lake": (2419.2, "Platinum 8280, 28 cores, 2.7 GHz"),
    "Xeon Ice Lake": (2764.8, "Platinum 8360Y, 36 cores, 2.4 GHz"),
    "Xeon Sapphire Rapids": (3584, "Platinum 8480C, 56 cores, 2.0 GHz"),
    "Xeon CPU Max (HBM)": (3993.6, "Max 9470, 52 cores, 2.4 GHz"),
    "Xeon Emerald Rapids": (2560, "Gold 6548Y+, 32 cores, 2.5 GHz"),
    "Xeon 6 (Granite Rapids)": (7372.8, "6972P, 96 cores, 2.4 GHz"),
    "Xeon Phi Knights Corner": (1074, "SE10P, 61 cores, 1.1 GHz"),
    "Data Center GPU Max (Ponte Vecchio)": (52000, "Max 1550, Intel peak figure"),
    # AMD
    "Opteron (K8)": (4, "2.0 GHz"),
    "Opteron dual-core": (8.8, "2 cores, 2.2 GHz"),
    "Opteron Barcelona (quad-core)": (30.4, "4 cores, 1.9 GHz"),
    "Opteron Istanbul (6-core)": (62.4, "6 cores, 2.6 GHz"),
    "Opteron Magny-Cours": (100.8, "12 cores, 2.1 GHz"),
    "Opteron Interlagos": (147.2, "6276, 16 cores, 2.3 GHz"),
    "EPYC Naples": (563.2, "7601, 32 cores, 2.2 GHz"),
    "EPYC Rome": (2662.4, "7H12, 64 cores, 2.6 GHz"),
    "EPYC Milan": (2508.8, "7763, 64 cores, 2.45 GHz"),
    "EPYC Genoa": (3686.4, "9654, 96 cores, 2.4 GHz"),
    "EPYC Turin": (9830.4, "9745, 128 cores, 2.4 GHz, AVX-512"),
    "Radeon / FirePro": (368, "Radeon HD 4870 X2 board at 575 MHz (Tianhe-1)"),
    "Instinct MI50 / MI60": (7400, "MI60, vector"),
    "Instinct MI100": (11500, "MI100, vector"),
    "Instinct MI250X": (47900, "MI250X, vector"),
    "Instinct MI300A (APU)": (61300, "MI300A, vector"),
    "Instinct MI300X": (81700, "MI300X, vector"),
    "Instinct MI325X / MI355X": (78600, "MI355X, vector"),
    # NVIDIA
    "Tesla (GT200)": (78, "Tesla T10 / C1060"),
    "Fermi": (515, "Tesla C2050"),
    "Kepler": (1310, "Tesla K20X"),
    "Pascal (P100)": (4700, "Tesla P100 PCIe"),
    "Volta (V100)": (7800, "Tesla V100 SXM2"),
    "Ampere (A100)": (9700, "A100, non-tensor"),
    "Hopper (H100 / GH200)": (26000, "H100 PCIe, non-tensor"),
    "Blackwell (B200 / GB200)": (37000, "B200 (HGX / DGX, 1000 W)"),
    "Grace (Arm)": (3571, "72 cores, 3.1 GHz"),
    # IBM
    "POWER2": (0.267, "66.7 MHz"),
    "PowerPC 604": (0.664, "604e, 332 MHz"),
    "POWER3": (0.8, "200 MHz"),
    "POWER4": (10.4, "2 cores, 1.3 GHz"),
    "PowerPC 970": (8, "2.0 GHz"),
    "PowerPC 440 (Blue Gene/L)": (4, "2 cores, 500 MHz"),
    "POWER5": (15.2, "2 cores, 1.9 GHz"),
    "PowerXCell 8i": (102.4, "8 SPEs, 3.2 GHz"),
    "PowerPC 450 (Blue Gene/P)": (13.6, "4 cores, 850 MHz"),
    "POWER6": (37.6, "2 cores, 4.7 GHz"),
    "POWER7": (245.5, "8 cores, 3.836 GHz"),
    "Power BQC (Blue Gene/Q)": (204.8, "16 cores, 1.6 GHz"),
    "POWER8": (208.6, "8 cores, 3.26 GHz"),
    "POWER9": (540.3, "22 cores, 3.07 GHz"),
    "POWER10": (3840, "15 SMT8 cores, 64 FP64 operations per cycle, ~4 GHz, estimate"),
    # Fujitsu
    "VPP500 (vector)": (1.6, "one processing element"),
    "VPP300 / VPP700": (2.2, "one processing element"),
    "VPP5000": (9.6, "one processing element"),
    "SPARC64 V": (2.7, "675 MHz"),
    "SPARC64 VII": (40.3, "4 cores, 2.52 GHz"),
    "SPARC64 VIIIfx (K)": (128, "8 cores, 2.0 GHz"),
    "SPARC64 IXfx": (236.5, "16 cores, 1.848 GHz"),
    "SPARC64 XIfx": (1013.8, "32 cores, 1.98 GHz"),
    "A64FX (Arm)": (3072, "48 cores, 2.0 GHz, SVE"),
    # China
    "ShenWei SW1600": (124.8, "16 cores, 975 MHz"),
    "Loongson / Godson": (128, "Godson-3B, 8 cores, 1.05 GHz"),
    "Phytium FT-1500 / FT-2000": (614.4, "FT-2000+, 64 cores, 2.2 GHz"),
    "Sunway SW26010": (3062, "260 cores, 1.45 GHz"),
    "Matrix-2000": (2458, "128 cores, 1.2 GHz"),
    "Hygon Dhyana / C86": (512, "32 cores, 2.0 GHz"),
    "Hygon DCU": (None, ""),
    "Sunway SW26010-Pro": (14026, "384 cores"),
    "MetaX": (None, ""),
    "LX2 (LingKun)": (60300, "304 cores, 1.55 GHz, designer figure (matrix units)"),
    # Vector
    "Cray T90": (1.8, "one CPU"),
    "Cray J90": (0.2, "one CPU"),
    "Cray SV1": (1.2, "one CPU, 300 MHz"),
    "Cray X1": (12.8, "one MSP"),
    "NEC SX-4": (2, "one CPU"),
    "NEC SX-5": (8, "one CPU"),
    "NEC SX-6 (Earth Simulator)": (8, "one CPU"),
    "NEC SX-8": (16, "one CPU"),
    "NEC SX-9": (102.4, "one CPU"),
    "NEC SX-ACE": (256, "one CPU, 4 vector cores, 1 GHz"),
    "NEC SX-Aurora (Vector Engine)": (2430, "Type 10AE, 8 cores, 1.58 GHz"),
    "Hitachi SR2201": (0.3, "one processing element"),
    "Hitachi SR8000": (1, "one CPU, 250 MHz"),
    "Hitachi SR11000": (13.6, "POWER4+ chip, 2 cores, 1.7 GHz"),
    # RISC Unix
    "Alpha 21064 (Cray T3D)": (0.15, "150 MHz"),
    "Alpha 21164 (EV5)": (0.6, "300 MHz"),
    "Alpha 21264 (EV6)": (1, "500 MHz"),
    "MIPS R8000 (POWER CHALLENGE)": (0.36, "90 MHz"),
    "MIPS R10000 (ORIGIN 2000)": (0.39, "195 MHz"),
    "MIPS R12000 / R14000 (ORIGIN 3000)": (0.8, "400 MHz"),
    "UltraSPARC": (0.5, "UltraSPARC II, 250 MHz"),
    "UltraSPARC III": (2.4, "1.2 GHz"),
    "PA-RISC 7x00 (SPP)": (0.2, "PA-7100, 100 MHz"),
    "PA-8000 (Exemplar X)": (0.72, "180 MHz"),
    "PA-8x00 (SuperDome)": (2.2, "PA-8600, 552 MHz"),
    # Others
    "Arm ThunderX2": (448, "CN9975, 28 cores, 2.0 GHz"),
    "Arm Kunpeng / Graviton": (666, "Kunpeng 920, 64 cores, 2.6 GHz, estimate"),
    "ClearSpeed": (50, "Advance X620 board"),
    "GRAPE-DR": (256, "one chip"),
    "PEZY-SC": (1500, "one chip"),
    "MN-Core": (32800, "one chip"),
}

# Sources of the values above, shown in the methodology page. Entries not
# listed here are computed from the processor's characteristics (cores x clock
# x FP64 operations per cycle, clock and cores read from the TOP500 description
# when given) or taken from the manufacturer's specifications.
FP64_SOURCES = {
    # vector machines
    "VPP500 (vector)": "https://museum.ipsj.or.jp/en/computer/super/0012.html",
    "VPP300 / VPP700": "https://www.fujitsu.com/global/documents/about/resources/publications/fstj/archives/vol33-1/paper02.pdf",
    "VPP5000": "https://www.fujitsu.com/global/about/corporate/history/products/computer/supercomputer/vpp5000.html",
    "Cray T90": "https://en.wikipedia.org/wiki/Cray_T90",
    "Cray J90": "https://netlib.org/benchmark/top500/reports/report95/Architectures/node3.html",
    "Cray SV1": "https://cug.org/5-publications/proceedings_attendee_lists/2001CD/S01_Proceedings/Pages/Authors/Bell.pdf",
    "Cray X1": "https://www.netlib.org/utk/papers/advanced-computers/x1.html",
    "NEC SX-4": "https://jpn.nec.com/hpc/sxauroratsubasa/history/index.html",
    "NEC SX-5": "https://jpn.nec.com/hpc/sxauroratsubasa/history/index.html",
    "NEC SX-6 (Earth Simulator)": "https://jpn.nec.com/hpc/sxauroratsubasa/history/index.html",
    "NEC SX-8": "https://link.springer.com/referenceworkentry/10.1007/978-0-387-09766-4_425/tables/1",
    "NEC SX-9": "https://jpn.nec.com/hpc/sxauroratsubasa/history/index.html",
    "NEC SX-ACE": "https://de.nec.com/de_DE/en/documents/SX-ACE-brochure.pdf",
    "Hitachi SR2201": "https://www.netlib.org/utk/papers/advanced-computers/sr2201.html",
    # accelerators
    "ClearSpeed": "https://www.tomshardware.com/news/clearspeed-announces-50-gflops-add,1331.html",
    "GRAPE-DR": "https://arxiv.org/pdf/0707.4293",
    "PEZY-SC": "https://en.wikichip.org/wiki/pezy/pezy-sc",
    "MN-Core": "https://projects.preferred.jp/mn-core/en/",
    "Radeon / FirePro": "https://blog.zorinaq.com/introducing-tianhe-1a-4702-tflops-of-gpu-power-made-in-china-and/",
    "Tesla (GT200)": "https://www.tomshardware.com/news/Tesla-C1060-S1070,5672.html",
    "Fermi": "https://www.nvidia.com/docs/io/43395/nv_ds_tesla_c2050_c2070_jul10_lores.pdf",
    "Kepler": "https://www.hpcwire.com/2012/11/12/nvidia_unveils_1-3_teraflop_gpu_for_supercomputing/",
    "Pascal (P100)": "https://nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-p100/pdf/nvidia-tesla-p100-datasheet.pdf",
    "Volta (V100)": "https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet.pdf",
    "Ampere (A100)": "https://nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf",
    "Hopper (H100 / GH200)": "https://www.nvidia.com/en-gb/data-center/h100/",
    "Blackwell (B200 / GB200)": "https://glennklockwood.com/garden/processors/b200",
    "Data Center GPU Max (Ponte Vecchio)": "https://www.intel.com/content/www/us/en/products/sku/232873/intel-data-center-gpu-max-1550/specifications.html",
    "Instinct MI250X": "https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-gpu-family-brochure.pdf",
    "Instinct MI300A (APU)": "https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300a-data-sheet.pdf",
    "Instinct MI300X": "https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-data-sheet.pdf",
    "Instinct MI325X / MI355X": "https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi355x-gpu-brochure.pdf",
    # processors with a published figure
    "LX2 (LingKun)": "https://www.glennklockwood.com/garden/processors/lx2",
    "Sunway SW26010-Pro": "https://www.nextplatform.com/2022/03/11/pondering-the-cpu-inside-chinas-sunway-oceanlight-supercomputer/",
    "Loongson / Godson": "https://jcst.ict.ac.cn/EN/10.1007/s11390-011-1151-6",
    "Phytium FT-1500 / FT-2000": "https://www.tomshardware.com/news/chines-exascale-supercomputer-prototype-ai-workloads-phytiym",
    "Arm Kunpeng / Graviton": "https://www.hikunpeng.com/document/detail/en/kunpengfaq/productfaq/hardwarefaq/hardware_faq_0001.html",
    "POWER10": "https://www.anandtech.com/show/15985",
    # no figure
    "Hygon DCU": "no public FP64 figure found",
    "MetaX": "no public FP64 figure found (https://flopper.io/gpu/metax-c500)",
}

# Reference for the FP64 operations per cycle of each microarchitecture, used for
# the computed values.
FLOPS_PER_CYCLE_REF = "https://en.wikichip.org/wiki/FLOPS"


# ______________________________________________________________________________
#
# Characteristics of the reference model of each processor (the model used for
# DEVICE_FP64): number of cores, nominal (base) frequency, vector or SIMD
# capabilities, and FP64 operations per cycle and per core (an FMA counts as 2).
# For vector machines (Cray, NEC, Fujitsu VPP, Hitachi) "cores" is the number of
# CPUs or vector cores in the device, and the vector figure is per CPU.
# Values come from vendor documentation and usual technical references
# (see FLOPS_PER_CYCLE_REF); some are approximate.
#
# name -> (cores, nominal frequency, vector / SIMD capabilities, FP64 flop/cycle/core)
# ______________________________________________________________________________

CPU_SPECS = {
    "i860 (Paragon)": (1, "50 MHz", "scalar pipelined FPU (add + multiply)", 1.5),
    "Pentium Pro": (1, "200 MHz", "x87 scalar FPU", 1),
    "Pentium III": (1, "800 MHz", "SSE, 128-bit (FP32 only); x87 for FP64", 1),
    "Pentium 4 / Xeon NetBurst": (1, "1.7 GHz", "SSE2, 128-bit", 2),
    "Itanium 2": (1, "900 MHz", "EPIC, 2 FMA units", 4),
    "Xeon EM64T (Nocona)": (1, "3.2 GHz", "SSE3, 128-bit", 2),
    "Xeon Woodcrest (51xx)": (2, "3.0 GHz", "SSSE3, 128-bit, add + multiply", 4),
    "Xeon Clovertown (53xx)": (4, "2.33 GHz", "SSSE3, 128-bit, add + multiply", 4),
    "Xeon Harpertown (54xx)": (4, "3.0 GHz", "SSE4.1, 128-bit, add + multiply", 4),
    "Xeon Nehalem (55xx)": (4, "2.93 GHz", "SSE4.2, 128-bit, add + multiply", 4),
    "Xeon Westmere (56xx)": (6, "2.66 GHz", "SSE4.2, 128-bit, add + multiply", 4),
    "Xeon Sandy Bridge (E5)": (8, "2.6 GHz", "AVX, 256-bit, add + multiply", 8),
    "Xeon Ivy Bridge (E5 v2)": (12, "2.2 GHz", "AVX, 256-bit, add + multiply", 8),
    "Xeon Haswell (E5 v3)": (12, "2.5 GHz", "AVX2, 256-bit, 2 FMA units", 16),
    "Xeon Broadwell (E5 v4)": (18, "2.1 GHz", "AVX2, 256-bit, 2 FMA units", 16),
    "Xeon Phi Knights Landing": (68, "1.4 GHz", "AVX-512, 2 FMA units", 32),
    "Xeon Skylake": (24, "2.1 GHz", "AVX-512, 2 FMA units", 32),
    "Xeon Cascade Lake": (28, "2.7 GHz", "AVX-512, 2 FMA units", 32),
    "Xeon Ice Lake": (36, "2.4 GHz", "AVX-512, 2 FMA units", 32),
    "Xeon Sapphire Rapids": (56, "2.0 GHz", "AVX-512, 2 FMA units; AMX matrix units (BF16/INT8)", 32),
    "Xeon CPU Max (HBM)": (52, "2.4 GHz", "AVX-512, 2 FMA units; AMX (BF16/INT8); 64 GB HBM2e", 32),
    "Xeon Emerald Rapids": (32, "2.5 GHz", "AVX-512, 2 FMA units; AMX (BF16/INT8)", 32),
    "Xeon 6 (Granite Rapids)": (96, "2.4 GHz", "AVX-512, 2 FMA units; AMX (BF16/FP16/INT8)", 32),
    "Opteron (K8)": (1, "2.0 GHz", "SSE2, 128-bit (executed in 64-bit halves)", 2),
    "Opteron dual-core": (2, "2.2 GHz", "SSE3, 128-bit (executed in 64-bit halves)", 2),
    "Opteron Barcelona (quad-core)": (4, "1.9 GHz", "SSE4a, 128-bit, add + multiply", 4),
    "Opteron Istanbul (6-core)": (6, "2.6 GHz", "SSE4a, 128-bit, add + multiply", 4),
    "Opteron Magny-Cours": (12, "2.1 GHz", "SSE4a, 128-bit, add + multiply", 4),
    "Opteron Interlagos": (16, "2.3 GHz", "AVX / FMA4, two 128-bit FMA units shared by 2 cores", 4),
    "EPYC Naples": (32, "2.2 GHz", "AVX2, two 128-bit FMA units", 8),
    "EPYC Rome": (64, "2.6 GHz", "AVX2, 256-bit, 2 FMA units", 16),
    "EPYC Milan": (64, "2.45 GHz", "AVX2, 256-bit, 2 FMA units", 16),
    "EPYC Genoa": (96, "2.4 GHz", "AVX-512 on 256-bit units, 2 FMA units", 16),
    "EPYC Turin": (128, "2.4 GHz", "AVX-512, 512-bit, 2 FMA units", 32),
    "Grace (Arm)": (72, "3.1 GHz", "Neoverse V2, SVE2 / NEON, 4 x 128-bit FMA units", 16),
    "POWER2": (1, "66.7 MHz", "2 scalar FMA units", 4),
    "PowerPC 604": (1, "332 MHz", "1 scalar FMA unit", 2),
    "POWER3": (1, "200 MHz", "2 scalar FMA units", 4),
    "POWER4": (2, "1.3 GHz", "2 scalar FMA units per core", 4),
    "PowerPC 970": (1, "2.0 GHz", "2 scalar FMA units; AltiVec (FP32 only)", 4),
    "PowerPC 440 (Blue Gene/L)": (2, "500 MHz", "double FPU (2-wide FP64 SIMD FMA)", 4),
    "POWER5": (2, "1.9 GHz", "2 scalar FMA units per core", 4),
    "PowerPC 450 (Blue Gene/P)": (4, "850 MHz", "double FPU (2-wide FP64 SIMD FMA)", 4),
    "POWER6": (2, "4.7 GHz", "2 scalar FMA units per core; VMX (FP32 only)", 4),
    "POWER7": (8, "3.836 GHz", "VSX, 4 FP64 FMA per cycle", 8),
    "Power BQC (Blue Gene/Q)": (16, "1.6 GHz", "QPX, 256-bit FMA (4-wide FP64)", 8),
    "POWER8": (8, "3.26 GHz", "VSX, two 128-bit FMA units", 8),
    "POWER9": (22, "3.07 GHz", "VSX, two 128-bit FMA units", 8),
    "POWER10": (15, "~4 GHz", "VSX (4 x 128-bit) and MMA matrix units", 64),
    "VPP500 (vector)": (1, "100 MHz", "vector processor (vector pipes)", 16),
    "VPP300 / VPP700": (1, "~143 MHz", "vector processor (vector pipes)", 15.4),
    "VPP5000": (1, "300 MHz", "vector processor (vector pipes)", 32),
    "SPARC64 V": (1, "675 MHz", "2 scalar FMA units", 4),
    "SPARC64 VII": (4, "2.52 GHz", "2 scalar FMA units per core", 4),
    "SPARC64 VIIIfx (K)": (8, "2.0 GHz", "HPC-ACE, 2-wide FP64 SIMD, 2 FMA units", 8),
    "SPARC64 IXfx": (16, "1.848 GHz", "HPC-ACE, 2-wide FP64 SIMD, 2 FMA units", 8),
    "SPARC64 XIfx": (32, "1.98 GHz", "HPC-ACE2, 256-bit SIMD, 2 FMA units", 16),
    "A64FX (Arm)": (48, "2.0 GHz", "SVE, 512-bit, 2 FMA units", 32),
    "ShenWei SW1600": (16, "975 MHz", "SIMD, 256-bit FMA", 8),
    "Loongson / Godson": (8, "1.05 GHz", "256-bit vector units, 2 FMA (approx.)", 16),
    "Phytium FT-1500 / FT-2000": (64, "2.2 GHz", "NEON, 128-bit FMA (approx.)", 4),
    "Sunway SW26010": (260, "1.45 GHz", "256-bit SIMD FMA (4-wide FP64)", 8),
    "Hygon Dhyana / C86": (32, "2.0 GHz", "AVX2, two 128-bit FMA units (Zen)", 8),
    "Sunway SW26010-Pro": (384, "~2.25 GHz", "512-bit SIMD FMA (approx.)", 16),
    "LX2 (LingKun)": (304, "1.55 GHz", "Armv9, SVE and matrix units (designer figure)", 128),
    "Cray T90": (1, "450 MHz", "vector processor, 2 vector pipes (add + multiply)", 4),
    "Cray J90": (1, "100 MHz", "vector processor (add + multiply)", 2),
    "Cray SV1": (1, "300 MHz", "vector processor, 2 vector pipes (add + multiply)", 4),
    "Cray X1": (4, "800 MHz", "MSP of 4 vector SSPs, 2 pipes each", 4),
    "NEC SX-4": (1, "125 MHz", "vector processor, 8 pipes (add + multiply)", 16),
    "NEC SX-5": (1, "250 MHz", "vector processor, 16 pipes (add + multiply)", 32),
    "NEC SX-6 (Earth Simulator)": (1, "500 MHz", "vector processor, 8 pipes (add + multiply)", 16),
    "NEC SX-8": (1, "1 GHz", "vector processor, 4 pipe sets (vector unit at 2 GHz)", 16),
    "NEC SX-9": (1, "3.2 GHz", "vector processor, 8 pipe sets, 2 add + 2 multiply", 32),
    "NEC SX-ACE": (4, "1 GHz", "vector cores, 4 x 16 pipes (FMA)", 64),
    "Hitachi SR2201": (1, "150 MHz", "PA-RISC based, pseudo-vector, add + multiply", 2),
    "Hitachi SR8000": (1, "250 MHz", "POWER based, pseudo-vector, 2 FMA units", 4),
    "Hitachi SR11000": (2, "1.7 GHz", "POWER4+, 2 scalar FMA units per core", 4),
    "Alpha 21064 (Cray T3D)": (1, "150 MHz", "scalar FPU", 1),
    "Alpha 21164 (EV5)": (1, "300 MHz", "scalar FPU, add + multiply", 2),
    "Alpha 21264 (EV6)": (1, "500 MHz", "scalar FPU, add + multiply", 2),
    "MIPS R8000 (POWER CHALLENGE)": (1, "90 MHz", "2 scalar FMA units", 4),
    "MIPS R10000 (ORIGIN 2000)": (1, "195 MHz", "scalar FPU, add + multiply", 2),
    "MIPS R12000 / R14000 (ORIGIN 3000)": (1, "400 MHz", "scalar FPU, add + multiply", 2),
    "UltraSPARC": (1, "250 MHz", "scalar FPU, add + multiply; VIS (integer SIMD)", 2),
    "UltraSPARC III": (1, "1.2 GHz", "scalar FPU, add + multiply; VIS (integer SIMD)", 2),
    "PA-RISC 7x00 (SPP)": (1, "100 MHz", "scalar FPU, multiply-add", 2),
    "PA-8000 (Exemplar X)": (1, "180 MHz", "2 scalar FMA units", 4),
    "PA-8x00 (SuperDome)": (1, "552 MHz", "2 scalar FMA units", 4),
    "Arm ThunderX2": (28, "2.0 GHz", "NEON, two 128-bit FMA units", 8),
    "Arm Kunpeng / Graviton": (64, "2.6 GHz", "NEON, 128-bit FMA", 4),
}


# ______________________________________________________________________________
#
# Characteristics of the reference model of each accelerator (the model used
# for DEVICE_FP64): compute units, shader cores (NVIDIA CUDA cores, AMD stream
# processors, Intel vector lanes), tensor or matrix cores, boost clock and
# memory. None when the vendor publishes no figure. Some values are approximate.
#
# name -> (reference model, compute units, shader cores, tensor / matrix cores,
#          clock, memory)
# ______________________________________________________________________________

GPU_SPECS = {
    "Xeon Phi Knights Corner": ("Xeon Phi SE10P", "61 x86 cores, 512-bit SIMD", None, None, "1.1 GHz", "8 GB GDDR5"),
    "Data Center GPU Max (Ponte Vecchio)": ("Max 1550", "128 Xe cores", 16384, 1024, "1.6 GHz", "128 GB HBM2e"),
    "Radeon / FirePro": ("Radeon HD 4870 X2 (2 GPUs)", "2 x 10 SIMD engines", 1600, None, "575 MHz", "2 GB GDDR5"),
    "Instinct MI50 / MI60": ("MI60", "64 CUs", 4096, None, "1.8 GHz", "32 GB HBM2"),
    "Instinct MI100": ("MI100", "120 CUs", 7680, 480, "1.502 GHz", "32 GB HBM2"),
    "Instinct MI250X": ("MI250X (2 dies)", "220 CUs", 14080, 880, "1.7 GHz", "128 GB HBM2e"),
    "Instinct MI300A (APU)": ("MI300A", "228 CUs + 24 Zen 4 CPU cores", 14592, 912, "2.1 GHz", "128 GB HBM3 (shared with the CPU)"),
    "Instinct MI300X": ("MI300X", "304 CUs", 19456, 1216, "2.1 GHz", "192 GB HBM3"),
    "Instinct MI325X / MI355X": ("MI355X", "256 CUs", 16384, 1024, "2.4 GHz", "288 GB HBM3E"),
    "Tesla (GT200)": ("Tesla C1060", "30 SMs", 240, None, "1.296 GHz", "4 GB GDDR3"),
    "Fermi": ("Tesla C2050", "14 SMs", 448, None, "1.15 GHz", "3 GB GDDR5"),
    "Kepler": ("Tesla K20X", "14 SMX", 2688, None, "732 MHz", "6 GB GDDR5"),
    "Pascal (P100)": ("Tesla P100 PCIe", "56 SMs", 3584, None, "1.303 GHz", "16 GB HBM2"),
    "Volta (V100)": ("Tesla V100 SXM2", "80 SMs", 5120, 640, "1.53 GHz", "16 or 32 GB HBM2"),
    "Ampere (A100)": ("A100 SXM4", "108 SMs", 6912, 432, "1.41 GHz", "40 or 80 GB HBM2e"),
    "Hopper (H100 / GH200)": ("H100 PCIe (SXM: 132 SMs, 16,896 CUDA cores, 528 tensor cores)", "114 SMs", 14592, 456, "1.755 GHz", "80 GB HBM2e"),
    "Blackwell (B200 / GB200)": ("B200 (2 dies; NVIDIA publishes no SM count, 148 SMs is the usual figure)", "148 SMs", 18944, 592, "~1.84 GHz", "180 GB HBM3e"),
    "PowerXCell 8i": ("PowerXCell 8i", "1 PPE + 8 SPEs, 128-bit SIMD", None, None, "3.2 GHz", "up to 32 GB DDR2"),
    "Matrix-2000": ("Matrix-2000", "128 cores, 256-bit vector units", None, None, "1.2 GHz", "DDR4"),
    "Hygon DCU": ("DCU (Deep Computing Unit)", None, None, None, None, None),
    "MetaX": ("MetaX C500", "64 CUs (community estimate)", None, None, None, "64 GB HBM2e"),
    "NEC SX-Aurora (Vector Engine)": ("Vector Engine Type 10AE", "8 vector cores, 32 pipes x 3 FMA", None, None, "1.584 GHz", "48 GB HBM2"),
    "ClearSpeed": ("Advance X620 (2 CSX600)", "2 x 96 processing elements", None, None, "210 MHz", "1 GB DDR2"),
    "GRAPE-DR": ("GRAPE-DR chip", "512 processing elements", None, None, "500 MHz", "external DDR2"),
    "PEZY-SC": ("PEZY-SC chip", "1,024 processing elements", None, None, "733 MHz", "DDR3"),
    "MN-Core": ("MN-Core board (4 dies)", "4 dies, SIMD matrix arithmetic units", None, None, "500 MHz", "32 GB DDR4"),
}

# Variants of an accelerator family recognised in the TOP500 'computer' field;
# the first matching regular expression replaces the reference model's figures
# (same layout as GPU_SPECS).
GPU_VARIANTS = {
    "Hopper (H100 / GH200)": [
        (r"GH200|Grace Hopper|GH Superchip", ("GH200", "132 SMs + 72 Grace CPU cores", 16896, 528, "1.98 GHz", "96 GB HBM3 (+ LPDDR5X on the Grace CPU)")),
        (r"H200", ("H200 SXM", "132 SMs", 16896, 528, "1.98 GHz", "141 GB HBM3e")),
        (r"H100.*(SXM|HGX|DGX)|DGX H100|HGX H100|ND H100|NDv5|H100 (80|94|64)", ("H100 SXM", "132 SMs", 16896, 528, "1.98 GHz", "80 GB HBM3")),
    ],
}
