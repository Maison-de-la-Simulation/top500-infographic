# TOP500 timeline

An interactive infographic tracing the history of supercomputers from the
[TOP500](https://www.top500.org) lists, from November 1994 to today.

The page [top500_infographic.html](top500_infographic.html) is self-contained:
the data are embedded in it, so you only need to open it in a browser (only the
fonts are loaded from Google Fonts).

## What the infographic shows

- **New entries in the top 10**: every machine when it first enters the top 10,
  with its Rmax.
- **Performance of the list**: aggregate, maximum, mean and median Rmax of
  the 500 systems of each list.
- **Power consumption**: largest consumer, #1 system, mean and median power of
  the systems that report it (from June 2008).
- **Power of new top 10 entries**: power of each machine entering the top 10,
  when it is reported.
- **New processors** and **new accelerators**: first appearance of about one
  hundred processor and accelerator generations (Xeon Sandy Bridge, EPYC Rome,
  Fermi, Hopper, SPARC64 VIIIfx…), placed at the peak FP64 performance of
  one device (vendor figures, listed in `tech_catalog.py`).
- **Processors (CPU)**: share of each vendor in the TOP500.
- **Accelerators (GPU…)**: share of each accelerator vendor.

Shares can be shown as a number of systems or as a share of the list's
aggregate Rmax. The method is described in [methodology.html](methodology.html).

## Files

| File | Purpose |
|---|---|
| `top500_infographic.html` | The infographic page (HTML/SVG/JS, data included) |
| `methodology.html` | How vendors, technologies and shares are computed |
| `build_infographic_data.py` | Reads the TOP500 XML files, computes the data and injects them into the page |
| `tech_catalog.py` | Catalogue of tracked technologies (vendor, type, name, regular expression) and peak FP64 of one device |
| `top500_infographic_data.json` | The same data as JSON |

## Regenerating the data

Requirements: Python 3 (standard library only) and the
`TOP500_YYYYMM_all.xml` files downloaded from top500.org.

Pass the folder holding the XML files:

```bash
python3 build_infographic_data.py --db /path/to/xml
# or
TOP500_DB=/path/to/xml python3 build_infographic_data.py
```

The script rewrites `top500_infographic_data.json` and replaces the data
embedded in `top500_infographic.html` (between the `/*DATA_START*/` and
`/*DATA_END*/` markers). The `-v` option prints the machines whose CPU was not
recognised, and the first appearance date of each technology.

To add a new list, put its XML file in that folder and run the script again.
To track a new chip, add an entry to `tech_catalog.py`.

## Publishing on GitHub Pages

The workflow `.github/workflows/pages.yml` publishes the pages on GitHub Pages
at every push to `main` (it can also be started by hand from the *Actions*
tab). It does not regenerate the data, since the TOP500 XML files are not in
the repository: regenerate them locally, then commit `top500_infographic.html`.

One-time setup: in the repository *Settings → Pages*, set *Source* to
*GitHub Actions*.

## Method in brief

The TOP500 files have no structured "processor" field. The CPU vendor and the
accelerator vendor are therefore inferred from the free-text `<computer>` field
with keyword rules. For the 1990s, this field often gives the machine model
rather than the chip (ORIGIN 2000 → MIPS R10000, SuperDome → PA-RISC…), so some
rules are based on the machine model.

## Data source

The data come from the [TOP500](https://www.top500.org) lists
(E. Strohmaier, J. Dongarra, H. Simon, M. Meuer and H. Meuer), downloaded in
XML format from the TOP500 website. The original XML files are not redistributed in
this repository: download them from the project's website.

The vendor and technology groupings are this project's own interpretation and
are not provided by TOP500. TOP500 is a registered trademark of Prometeus GmbH;
this project is neither affiliated with nor endorsed by the TOP500 project.
