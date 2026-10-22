---
# Ensure that this title is the same as the one in `myst.yml`
title: "Supplementation and Encapsulation of PPK2 Enzymes in PURExpress Systems"
abstract: |
  Lipid encapsulation of PURExpress with PPK2 creates a simple synthetic cell-like system. PURExpress provides the purified machinery for transcription and translation, while lipid vesicles act as a membrane-bound compartment similar to a cell. PPK2 is added with polyphosphate to regenerate ATP/NTPs, replacing or supplementing the usual energy system. This helps test whether a polyP-powered energy pathway can support protein expression inside vesicles. Expression is measured with the fluorescent reporter sfGFP. Bright vesicles suggest successful encapsulation and energy regeneration, while dim vesicles may indicate poor encapsulation, low DNA/protein machinery capture, Mg²⁺ imbalance, or weak PPK2 activity.
---

# Overview

Lipid encapsulation of PURExpress with PPK2 creates a simple synthetic cell-like system. PURExpress provides the purified machinery for transcription and translation, while lipid vesicles act as a membrane-bound compartment similar to a cell. PPK2 is added with polyphosphate to regenerate ATP/NTPs, replacing or supplementing the usual energy system. This helps test whether a polyP-powered energy pathway can support protein expression inside vesicles. Expression is measured with the fluorescent reporter sfGFP. Bright vesicles suggest successful encapsulation and energy regeneration, while dim vesicles may indicate poor encapsulation, low DNA/protein machinery capture, Mg²⁺ imbalance, or weak PPK2 activity.

# Bill of Materials

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| POPC | 16:0-18:1 PC 25 mg/mL | Avanti Lipids | 850457C | $435.00 | -20 C | [16:0-18:1 PC (POPC) \| 26853-31-6 \| Avanti Research](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Liss-Rhod-PE | 16:0 Liss Rhod PE 1 mg/mL | Avanti Lipids | 810158C-1mg | $281.67 | -20 C | [16:0 Liss Rhod PE \| 384833-01-6 \| Avanti Research](https://www.avantiresearch.com/en-gb/products/product/810158-160-liss-rhod-pe) |
| Cholesterol | cholesterol (D7) 1EA | Avanti Lipids | A84100M | $193.72 | -20 C | [cholesterol (D7) \| 83199-47-7 \| Avanti Research](https://www.avantiresearch.com/en-gb/products/product/4100-cholesterol-d7) |
| Mineral Oil | Mineral oil, mixed weight | Thermo Scientific | AC415080010 | $53.40 | RT | [Mineral oil, pure 1 L \| Buy Online \| Thermo Scientific Chemicals \| thermofisher.com](https://www.thermofisher.com/order/catalog/product/415080010?SID=srch-srp-415080010) |
| Glucose | D-(+)-Glucose, 99% | Thermo Scientific | A16828.36 | $41.65 | RT | [D-(+)-Glucose, anhydrous, 99% 500 g \| Buy Online \| Thermo Scientific Chemicals \| thermofisher.com](https://www.thermofisher.com/order/catalog/product/A16828.36) |
| PURE | PURExpress | NEB | E6800S | $295.00 | -80 C | [PURExpress® In Vitro Protein Synthesis Kit \| NEB](https://www.neb.com/en-us/products/e6800-purexpress-invitro-protein-synthesis-kit) |
| RNase Inhibitor | RNase Inhibitor, Murine | NEB | M0314S | $81.00 | -20 C | [RNase Inhibitor, Murine \| NEB](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| OptiPrep | OptiPrep™ Density Gradient Medium | Sigma Aldrich | D1556-250ML | $373.00 | 4 C | [OptiPrep Density Gradient Medium, 60 (w/v) iodixanol in water](https://www.sigmaaldrich.com/US/en/product/sigma/d1556?msockid=1cb4fd24af9b66ff2777e832ae1867b1) |
| DNA | pJL1-sfGFP |  |  |  | -20 C |  |
| DrPPK2-III |  |  |  |  | -80 C |  |
| MaPPK2-III |  |  |  |  | -80 C |  |

# Protocol

## Prepare Lipid-oil Solution

1. Add mineral oil (3-5 mL) to a clean glass vial.
2. Using a glass syringe, draw up the lipid stock and inject it into the mineral oil at the correct molar ratio (70:29.95:0.05 POPC:cholesterol:Liss-Rhod PE).
3. Vortex the mixture for 10 seconds in the fume hood.
4. Cover the vial with aluminum foil and place it in a 55°C dry bath for 4 hours.

| Lipid | Target Percentage % | Molecular Weight | Concentration (mg/mL) | Volume to Add (µL) |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.66 | 50 | 17.65 |
| Liss Rhod PE | 0.05 | 1301.72 | 1 | 4.96 |

| Component | Concentration |
| --- | --- |
| Glucose | 850 mM |

## PURE Reaction Setup

1. Label 9 tubes, one of each of the following:
   - E1-E3 oil emulsion
   - T1-T3 transfer
   - L1-L3 liposomes
2. Pipette each reaction below into its own E tube (E1 = control, E2 = MaPPK2, E3 = DrPPK2):
3. 70 µL reaction volume per condition
   - 16 µL (2 × 8 µL) will be used for quantifying protein synthesis in a plate reader
   - 10 µL will be used for measuring osmolarity
   - 30 µL will be used for encapsulation

| Component | PURE + Control | PURE + MaPPK2 | PURE + DrPPK2 |
| --- | --- | --- | --- |
| Nuclease-free H2O (µL) | 6.31 | 4.01 | 4.01 |
| Solution A (µL) | 26 | 26 | 26 |
| Solution B (µL) | 19.5 | 19.5 | 19.5 |
| RNase inhibitor (µL) | 1.4 | 1.4 | 1.4 |
| pJL1-sfGFP Plasmid DNA (µL) Conc.: 116.1 ng/µL [final conc.: 10 ng/µL] | 5.99 | 5.99 | 5.99 |
| OptiPrep (µL) | 2.1 | 2.1 | 2.1 |
| PolyP (µL) | 4.2 | 4.2 | 4.2 |
| 200 mM Mg-acetate (µL) | 4.5 | 4.5 | 4.5 |
| PPK2 enzyme (µL) | 0 | 2.3 | 2.3 |
| Total (µL) | 70 | 70 | 70 |
| Osmolarity (mOsm/kg) | 1373 | 1453 | 1472 |

4. Pipette mix each reaction, then centrifuge the reaction at 5000g [6685 RPM for tabletop centrifuges (r=10 cm)] for 10-30 seconds to spin down bubbles in the reaction.
5. Check the osmolarity of your cytosol using a Vapor Pressure Osmometer before encapsulation.
   - Pipette 10 μL of your cytosol onto the disc and press "close".
   - Read and record the osmolarity.
6. Pipette mix the PURE solution before transferring 8 µL into two wells of a 384-well plate for kinetics quantification.
7. Set the micropipette to 8 μL and stop at the first stop when dispensing to prevent the introduction of bubbles into the sample. Use 30 µL of the remaining reaction in each E tube for encapsulation.

## Encapsulate PURExpress into Liposomes

1. Add 300 μL of the glucose outer solution to each tube labeled T.
2. Add 150 μL of the lipid-oil mixture to the top of the PURE reaction in each E tube.
3. Emulsify the lipid-oil and PURE mixture by running the tube along a row of empty slots on a 1.5 mL tube rack. Run it down 40-50 times until the solution forms a stable emulsion with an even milky color.
   - While running the tubes on the tube rack, hold the cap firmly to prevent it from coming off during vigorous mixing.
4. Slowly pipette the entire emulsion down the side of the corresponding T tube, so that the emulsion is layered on top of the glucose solution.
5. Centrifuge the T tube at 9000 g [8970 RPM for tabletop centrifuges (r=10 cm)] for 10 min at room temperature to pellet the liposomes.
   - When loading the centrifuge, arrange tubes with the hinge side facing out, and note that the pellet will form on the hinge side.
6. Extract the liposomes from the T tube:
   - Remove the oil layer and lipid debris from the top (supernatant) of the T tube by gently pipetting with a 1000 μL pipette set to 150 μL. Begin at the top of the mixture and aspirate from the solution surface as the liquid level descends in the tube. Dispose of supernatant in a designated container or an empty microcentrifuge tube, which can then be disposed of in designated waste.
   - Dislodge and resuspend the pellet by gently pipetting near the pellet. Pipet 50 μL of pellet and outer solution from tube T and transfer to the respective liposome tube L. Do not transfer the entire solution. It is important to avoid transferring the top of the solution, which may contain a residual oil layer.
7. Keep the tube on ice until ready for microscopy.

## Microscopy Set-up

1. Pipette ~30 μL of the liposomes from tube L into a well on a 384-well glass bottom plate. Set the micropipette to 32 μL and stop at the first stop when dispensing to prevent the introduction of bubbles into the sample.
2. Wipe the bottom of the plate with a Kimwipe to rid the plate of any dust. Handle the plate by its sides with gloved hands to avoid dirtying the glass bottom.
3. Launch Squid software on the Cephla Microscope monitor.
4. Lower the objective on the focus knob to 0.
5. Add the plate with your sample to the viewing surface, ensuring that well A1 is in the correct spot (labeled "A1" on the microscope).
6. Click "Start Live" in the software.
7. Set live configuration to fluorescence 638 nm to visualize liposomes or 488 nm to visualize sfGFP.
8. Set exposure time to 50 ms to start. Adjust if needed (with instructor or TA guidance) to find best visualization settings.
9. Select the well you would like to view.
10. Slowly raise the stage with the focus knob. The microscope will likely focus on z~3800.
11. Once you have focused on liposomes, go to the "laser AF" setting and press "Set Reference".
12. Under "Wellplate Multipoint," label your experiment ID with "initials.date.experiment#".
13. Select "laser AF", "fluorescence 488 nm", and "fluorescence 638 nm", then press "Snap Image" to view liposomes.

# Results and Observations

:::{figure} figures/fig1-control-sfgfp-kinetics.png
:name: fig-ppk2-control
:width: 90%

Figure 1. Encapsulation of the Standard PURExpress system over the course of 4 hours, tracking the expression of sfGFP.
:::

:::{figure} figures/fig2-mappk2-sfgfp-kinetics.png
:name: fig-ppk2-mappk2
:width: 90%

Figure 2. Encapsulation of the Standard PURExpress system supplemented with MaPPK2-III over the course of 4 hours, tracking the expression of sfGFP.
:::

:::{figure} figures/fig3-drppk2-sfgfp-kinetics.png
:name: fig-ppk2-drppk2
:width: 90%

Figure 3. Encapsulation of the Standard PURExpress system supplemented with DrPPK2-III over the course of 4 hours, tracking the expression of sfGFP.
:::

# Conclusion

PPK2 supported early sfGFP expression by regenerating ATP/NTPs from polyphosphate, giving the PURExpress system an immediate energy source for transcription and translation. The steady increase in fluorescence over time suggests that PPK2 continued to maintain energy availability, allowing sfGFP production to keep progressing rather than quickly plateauing. Overall, this shows that the PPK2/polyP system can effectively sustain protein expression in the encapsulated PURExpress system.
