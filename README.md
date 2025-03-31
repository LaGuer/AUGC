# AUGC

RNA nucleotides Mass Ratio using natural units (mol,GeV,m_n,m_p,m_e)

We’re checking two equations: (1) C + G = A + U + 15 (2) A + U = C + G – 15

For each of our six columns, we compute the sum of (A+U) and (C+G), then the difference.

ACGU (RNA):
A-U Pairing: Adenine (A) and Uridine (U) pair similarly to A-T, with slightly higher mass for U compared to T, indicating RNA's distinct functional characteristics.

C-G Pairing: Cytosine (C) and Guanine (G) in RNA retain their heavier molar mass contributions, emphasizing structural stability.

Sample output :


(((

NT | Molar(g/mol) | Mass(GeV) | ProtonRatio | NeutronRatio |  HydrogenRatio |   Planck Ratio |    Electron Ratio |   Neuron Ratio
---------------------------------------------------------------------------------------------------------------------------------
 A |   347.22 |   323.44 |   344.71 |   344.24 |       3.45e+02 |       2.65e-17 |         6.33e+05 |       3.23e+12
 C |   323.20 |   301.06 |   320.87 |   320.43 |       3.21e+02 |       2.47e-17 |         5.89e+05 |       3.01e+12
 G |   363.22 |   338.34 |   360.60 |   360.10 |       3.60e+02 |       2.77e-17 |         6.62e+05 |       3.38e+12
 U |   324.19 |   301.98 |   321.85 |   321.41 |       3.22e+02 |       2.47e-17 |         5.91e+05 |       3.02e+12

)))

(((

--- Equation Check ---
    Column |          A+U |          C+G |   Difference
-------------------------------------------------------
     Molar |     671.4100 |     686.4200 |      15.0100
       GeV |     625.4184 |     639.4002 |      13.9818
    Proton |     666.5640 |     681.4657 |      14.9017
   Neutron |     665.6465 |     680.5276 |      14.8812
  Hydrogen |     666.2084 |     681.1021 |      14.8937
    Planck |       0.0000 |       0.0000 |       0.0000
  Electron | 1223910.7926 | 1251272.4658 |   27361.6732
    Neuron | 6254184150000.0000 | 6394002300000.0000 | 139818150000.0000

)))


