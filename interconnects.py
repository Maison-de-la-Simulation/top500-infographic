# ______________________________________________________________________________
#
# Interconnects recognised in the TOP500 'computer' field (or deduced from the
# machine model for early systems), shown in all_systems.html.
#
# Each entry: (regular expression, name, bandwidth of one link or port,
#              usual topology). The first matching entry wins, so specific
#              entries come before generic ones. Bandwidths are the nominal
#              signalling rate of one port in one direction; topologies are the
#              usual ones for the family (an empty string when they vary, as for
#              InfiniBand and Ethernet clusters). Values are approximate.
# ______________________________________________________________________________

INTERCONNECTS = [
    # HPE / Cray
    (r"slingshot[- ]?400", "HPE Slingshot 400", "400 Gb/s", "dragonfly"),
    (r"slingshot[- ]?11", "HPE Slingshot 11", "200 Gb/s", "dragonfly"),
    (r"slingshot[- ]?10", "HPE Slingshot 10", "100 Gb/s", "dragonfly"),
    (r"slingshot", "HPE Slingshot", "200 Gb/s", "dragonfly"),
    (r"aries|cray xc", "Cray Aries", "~ 100 Gb/s", "dragonfly"),
    (r"gemini|cray xk|cray xe6", "Cray Gemini", "~ 75 Gb/s", "3D torus"),
    (r"seastar|cray xt", "Cray SeaStar", "~ 50 Gb/s", "3D torus"),
    (r"\bt3e|\bt3d", "Cray T3D/T3E network", "~ 4 Gb/s", "3D torus"),
    # InfiniBand, fastest first
    (r"quantum[- ]?x800|infiniband xdr|\bxdr\b", "InfiniBand XDR", "800 Gb/s", ""),
    (r"ndr ?400|ndr400", "InfiniBand NDR", "400 Gb/s", ""),
    (r"ndr ?200|ndr200", "InfiniBand NDR200", "200 Gb/s", ""),
    (r"infiniband ndr|\bndr\b", "InfiniBand NDR", "400 Gb/s", ""),
    (r"hdr ?100|hdr100", "InfiniBand HDR100", "100 Gb/s", ""),
    (r"hdr ?200|hdr200|infiniband hdr|\bhdr\b", "InfiniBand HDR", "200 Gb/s", ""),
    (r"\bedr\b|infiniband edr", "InfiniBand EDR", "100 Gb/s", ""),
    (r"fdr ?14|\bfdr\b|infiniband fdr", "InfiniBand FDR", "56 Gb/s", ""),
    (r"\bqdr\b|infiniband qdr", "InfiniBand QDR", "40 Gb/s", ""),
    (r"\bddr\b|infiniband ddr", "InfiniBand DDR", "20 Gb/s", ""),
    (r"infiniband|infinband|\bib\b", "InfiniBand", "", ""),
    # Intel / Atos / Fujitsu / NEC / Chinese
    (r"omni-?path|\bopa\b", "Intel Omni-Path", "100 Gb/s", "fat tree"),
    (r"bxi ?v?2|bxi v2", "Atos BXI V2", "200 Gb/s", ""),
    (r"\bbxi", "Bull BXI", "100 Gb/s", ""),
    (r"tofu interconnect d|tofu ?d\b|a64fx", "Fujitsu Tofu D", "~ 54 Gb/s", "6D mesh/torus"),
    (r"tofu ?2|tofu interconnect 2|sparc64 xifx", "Fujitsu Tofu2", "100 Gb/s", "6D mesh/torus"),
    (r"tofu|k computer|sparc64 (viiifx|ixfx)", "Fujitsu Tofu", "40 Gb/s", "6D mesh/torus"),
    (r"th express-?2|th-ivb|matrix-2000", "TH Express-2", "~ 112 Gb/s", "fat tree"),
    (r"sunway", "Sunway network", "~ 128 Gb/s", "fat tree"),
    (r"lingqi", "LingQi (LineShine)", "", ""),
    (r"\bixs\b|sx-[0-9]|sx-ace|earth simulator", "NEC IXS crossbar", "", "crossbar"),
    # IBM
    (r"blue ?gene/q|bqc|power bqc", "Blue Gene/Q network", "16 Gb/s", "5D torus"),
    (r"blue ?gene/p|bluegene/p|ppc 450|powerpc 450", "Blue Gene/P network", "~ 3.4 Gb/s", "3D torus"),
    (r"blue ?gene/l|bluegene/l|ppc 440|powerpc 440", "Blue Gene/L network", "~ 1.4 Gb/s", "3D torus"),
    (r"\bsp switch|sp2|\bsp\b|ibm sp", "IBM SP Switch", "~ 1 Gb/s", "multistage"),
    (r"federation", "IBM Federation", "~ 16 Gb/s", "multistage"),
    # older cluster networks
    (r"myri-?10g", "Myri-10G", "10 Gb/s", ""),
    (r"myrinet", "Myrinet", "2 Gb/s", ""),
    (r"quadrics|qsnet", "Quadrics QsNet", "~ 7 Gb/s", "fat tree"),
    (r"numalink|origin|altix|sgi uv", "SGI NUMAlink", "", ""),
    (r"cm-5", "CM-5 data network", "", "fat tree"),
    (r"paragon|xp/s", "Paragon mesh", "", "2D mesh"),
    (r"hyperplex|hplex", "HP HyperPlex", "", ""),
    # Ethernet: handled by ethernet() below, since its speed must be read in
    # the part of the field that names Ethernet (to avoid "40 GB" of memory)
]

# Number of rails per node, when the 'computer' field gives it
RAILS = [(r"octo-?rail", 8), (r"quad-?rail", 4), (r"dual-?rail", 2)]


ETHERNET_RE = r"ethernet|\bgbe\b|gige|gig-e|gigabit|\broce|spectrum-?x"
ETHERNET_SPEED_RE = r"\b(10|25|40|100|200|400|800)\s?(?:g|gb|gbe|gbit|gig|gigabit)\b"
