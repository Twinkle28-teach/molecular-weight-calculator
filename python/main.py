# from parser import calculate_molecular_weight

# compounds = [
#     "H2O",
#     "Ca(OH)2",
#     "K2Cr2O7",
#     "Al2(SO4)3"
# ]

# for compound in compounds:
#     weight = calculate_molecular_weight(compound)

#     print(f"{compound} -> {weight:.3f} g/mol")

import csv
from parser import calculate_molecular_weight

with open("data/compounds.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        formula = row["compound"]
        weight = calculate_molecular_weight(formula)

        print(f"{formula} -> {weight} g/mol")