# Conversion constants
amu_to_GeV = 0.9315             # 1 atomic mass unit ≈ 0.9315 GeV
amu_to_MeV = 9315             # 1 atomic mass unit ≈ 9315 MeV
proton_mass_GeV = 0.9382720813   # Proton mass in GeV
neutron_mass_GeV = 0.939565413   # Neutron mass in GeV
electron_mass_GeV = 0.000511     # Electron mass in GeV
planck_mass_GeV = 1.2209e19      # Planck mass in GeV
hydrogen_mass_GeV = 0.938773            # Hydrogen mass in GeV (example value)
neuron_mass_GeV = 1.0e-10        # Neuron mass (example placeholder)
    
#    mass_Kg = (mass_with_hydrogen / 1000) / avogadro_number

# Approximate molar masses (g/mol) for ribonucleotides:
# A for AMP, C for CMP, G for GMP, and U for UMP (instead of T for thymine).
ribonucleotides = {
    "A": 347.22,  # AMP
    "C": 323.20,  # CMP
    "G": 363.22,  # GMP
    "U": 324.19   # UMP
}

# Compute conversion values for each ribonucleotide and store in a dictionary.
rna_data = {}
for nt, mass in ribonucleotides.items():
    mass_GeV = mass * amu_to_GeV
    proton_ratio = mass_GeV / proton_mass_GeV
    neutron_ratio = mass_GeV / neutron_mass_GeV
    electron_ratio = mass_GeV / electron_mass_GeV
    planck_ratio = mass_GeV / planck_mass_GeV
    hydrogen_ratio = mass_GeV / hydrogen_mass_GeV
    neuron_ratio = mass_GeV / neuron_mass_GeV  # New Neuron ratio
    rna_data[nt] = {
        "Molar": mass,          # in g/mol
        "GeV": mass_GeV,
        "Proton": proton_ratio,
        "Neutron": neutron_ratio,
        "Electron": electron_ratio,
        "Planck": planck_ratio,
        "Hydrogen": hydrogen_ratio,
        "Neuron": neuron_ratio  # Add Neuron ratio to the dictionary
    }

# Print the table of individual conversions.
header = f"{'NT':>2} | {'Molar(g/mol)':>8} | {'Mass(GeV)':>8} | {'ProtonRatio':>8} | {'NeutronRatio':>8} | {'HydrogenRatio':>14} | {'Planck Ratio':>14} |  {'Electron Ratio':>16} | {'Neuron Ratio':>14}"
print(header)
print("-" * len(header))
for nt in ["A", "C", "G", "U"]:
    row = rna_data[nt]
    print(f"{nt:>2} | {row['Molar']:8.2f} | {row['GeV']:8.2f} | {row['Proton']:8.2f} | {row['Neutron']:8.2f} | {row['Hydrogen']:14.2e} | {row['Planck']:14.2e} | {row['Electron']:16.2e} | {row['Neuron']:14.2e}")


# Now compute the sums for the pairs A+T and C+G in each of the five columns.
print("\n--- Equation Check ---")
print("We want to verify the relationships:")
print("  (1) C + G = A + T + 15")
print("  (2) A + T = C + G - 15\n")

cols = ["Molar", "GeV", "Proton"]

# Print the sums and the difference: (C+G) - (A+T)
header2 = f"{'Column':>10} | {'A+U':>12} | {'C+G':>12} | {'Difference':>12}"
print(header2)
print("-" * len(header2))
for col in cols:
    sum_AU = rna_data["A"][col] + rna_data["U"][col]
    sum_CG = rna_data["C"][col] + rna_data["G"][col]
    diff = sum_CG - sum_AU
    # diff should be nearly 1 if (C+G) = (A+U)+15 and equally (A+U) = (C+G)-15.
    print(f"{col:>10} | {sum_AU:12.4f} | {sum_CG:12.4f} | {diff:12.4f}")

# Provide an extra printout that frames the equations explicitly.
print("\nVerification of equations:")
for col in cols:
    sum_AU = rna_data["A"][col] + rna_data["U"][col]
    sum_CG = rna_data["C"][col] + rna_data["G"][col]
    eq1 = sum_AU + 15      # Expect eq1 to nearly equal sum_CG
    eq2 = sum_CG - 15      # Expect eq2 to nearly equal sum_AU
    print(f"{col:>10}:")
    print(f"    (A+U)+15 = {eq1:12.4f}    vs.    C+G = {sum_CG:12.4f}   (diff = {sum_CG - eq1: .4f})")
    print(f"    (C+G)-15 = {eq2:12.4f}    vs.    A+U = {sum_AU:12.4f}   (diff = {sum_AU - eq2: .4f})\n")
