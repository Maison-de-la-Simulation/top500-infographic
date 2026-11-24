# ______________________________________________________________________________
#
# Everyday devices compared with the TOP500 in the "everyday devices" chart.
#
# Each entry: (date YYYY.MM of release, category, name, peak GFlop/s, basis)
# The figure is the single-precision (FP32) peak of the graphics processor as
# quoted by the manufacturer or by usual technical sources, which is how these
# devices are advertised. TOP500 figures are measured in double precision
# (FP64, LINPACK), so the comparison is generous to the devices: it gives an
# order of magnitude, not an equivalence. Values are approximate.
# ______________________________________________________________________________

EVERYDAY_DEVICES = [
    ("2000.03", "console", "PlayStation 2", 6.2, "Emotion Engine"),
    ("2005.11", "console", "Xbox 360", 240, "Xenos GPU"),
    ("2006.11", "console", "PlayStation 3", 230, "Cell processor"),
    ("2010.06", "phone", "iPhone 4", 1.6, "PowerVR SGX535 GPU"),
    ("2013.09", "phone", "iPhone 5s", 115, "A7 GPU"),
    ("2013.11", "console", "PlayStation 4", 1840, "GPU"),
    ("2017.03", "console", "Nintendo Switch", 393, "GPU, docked"),
    ("2017.11", "console", "Xbox One X", 6000, "GPU"),
    ("2020.11", "computer", "MacBook Air M1", 2600, "M1 GPU, 8 cores"),
    ("2020.11", "console", "PlayStation 5", 10280, "GPU"),
    ("2021.09", "phone", "iPhone 13 Pro", 1370, "A15 GPU, 5 cores"),
    ("2022.02", "console", "Steam Deck", 1600, "AMD APU GPU, 1.6 GHz (Valve figure)"),
    ("2022.10", "computer", "GeForce RTX 4090", 82600, "gaming graphics card"),
    ("2023.09", "phone", "iPhone 15 Pro", 2150, "A17 Pro GPU"),
    ("2024.11", "console", "PlayStation 5 Pro", 16700, "GPU"),
    ("2025.01", "computer", "GeForce RTX 5090", 104800, "gaming graphics card"),
    ("2025.10", "computer", "MacBook Pro M5", 4100, "M5 GPU, 10 cores, estimate (Apple publishes no figure)"),
    ("2026.09", "phone", "iPhone 18 Pro", 2960, "A20 Pro GPU, 7 cores, estimate (Apple publishes no figure)"),
]
