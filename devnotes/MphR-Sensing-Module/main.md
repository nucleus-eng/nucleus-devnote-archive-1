---
# Ensure that this title is the same as the one in `myst.yml`
title: "MphR Sensing Module"
abstract: |
  The MphR sensing module consists of the TetR-family allosteric transcription factor (aTF) MphR in the ROSALIND system. The ROSALIND system is based on the regulation of an *in vitro* transcription of a fluorescence activating RNA known as the 3WJdB (three-way junction dimeric Broccoli) aptamer. In the presence of a suitable binding dye (DFHBI-1T), transcription of the 3WJdB aptamer can be measured in real-time. Transcription can be regulated by including the MphR protein in the *in vitro* transcription reaction with a suitably encoded DNA transcription template that includes the MphR binding site (known as the operator sequence, *mphO*). Repression can be relieved through induction of MphR and resulting transcription can be monitored fluorescently (see [References and Resources](#resources-and-references) below for a more thorough description).
---

# Overview

### Description of Module

The MphR sensing module consists of the TetR-family allosteric transcription factor (aTF) MphR in the ROSALIND system. The ROSALIND system is based on the regulation of an *in vitro* transcription of a fluorescence activating RNA known as the 3WJdB (three-way junction dimeric Broccoli) aptamer. In the presence of a suitable binding dye (DFHBI-1T), transcription of the 3WJdB aptamer can be measured in real-time. Transcription can be regulated by including the MphR protein in the *in vitro* transcription reaction with a suitably encoded DNA transcription template that includes the MphR binding site (known as the operator sequence, *mphO*). Repression can be relieved through induction of MphR and resulting transcription can be monitored fluorescently (see [References and Resources](#resources-and-references) below for a more thorough description).

MphR induces transcription in the presence of macrolides - a class of antibiotics (e.g., azithromycin, erythromycin) that are widely used in human and animal health and are included on WHO's list of essential medicines. The availability of biological sensors for macrolides will help the discovery and development of new macrolides and macrolide analogues, and enable the ability to monitor the presence of antibiotics in the environment, which give rise to antibiotic resistance. These compounds represent candidates for antifungal, antimicrobial, and antibacterial medicines that are important for human, animal, and planetary health. Such biological sensors can also enable scalable screening and process optimization in biomanufacturing.

### Component specifications

**Protein: MphR-6xHis**

Sequence ({download}`plain text <sequences/MphR-6xHis.txt>`):

```
MPRPKLKSDDEVLEAATVVLKRCGPIEFTLSGVAKEVGLSRAALIQRFTNRDTLLVRMME
RGVEQVRHYLNAIPIGAGPQGLWEFLQVLVRSMNTRNDFSVNYLISWYELQVPELRTLAI
QRNRAVVEGIRKRLPPGAPAAAELLLHSVIAGATMQWAVDPDGELADHVLAQIAAILCLM
FPEHDDFQLLQPHAKLAAALEHHHHHH
```

Plasmid: pJBL715 (Backbone: pET28c, Addgene #[140385](https://www.addgene.org/140385/) - UBMTA)

**DNA-reporter: T7-mphO-3WJdB-T**

Sequence ({download}`plain text <sequences/T7-mphO-3WJdB-T.txt>`):

```
gcggataacaatttcacacaggaaacagctatgaccatgattacgccaagcttgcatgcc
tgcaggtcgactctagataatacgactcactataggagggaatataaccgacgtgactgt
tacatttaggtggcccacatactctgatgatccgagacggtcgggtccagatattcgtat
ctgtcgagtagagtgtgggctcggatcattcatggcaagagacggtcgggtccagatatt
cgtatctgtcgagtagagtgtgggctcttgccatgtgtatgtgggtagcataaccccttg
gggcctctaaacgggtcttgaggggttttttg
```

Plasmid: pUC19-T7-mphO-3WJdB-T (Backbone: pUC19, Addgene #[140386](https://www.addgene.org/87308/)- UBMTA)

# Materials and Equipment

| **Name** | **Product** | **Manufacturer** | **Part #** | **Price** | **Link** | **Storage Conditions** |
| --- | --- | --- | --- | --- | --- | --- |
| Spermidine | Spermidine, ≥99% (GC) | Sigma-Aldrich | S2626-5G | $176 | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/s2626)] | -25C to -15C |
| Tris-HCL | Trizma® hydrochloride anhydrous, free-flowing, Redi-Dri™, ≥99.0% | Sigma-Aldrich | RDD009-1KG | $268.60 | [[link](https://www.sigmaaldrich.com/US/en/search/rdd009-2.5kg?focus=products&page=1&perpage=30&sort=relevance&term=rdd009-2.5kg&type=product)] | 4C to 30C |
| MgCl2 | Magnesium chloride hexahydrate, BioXtra ≥99.0% | Sigma-Aldrich | **M2670-100G** | $50.50 | [[link](https://www.sigmaaldrich.com/US/en/product/sial/m2670?srsltid=AfmBOor6chfxnjM0Q78LwEqNQaC50UipQSIs0EypWm5R7Bd8UD9IN2x3)] | 4C to 30C |
| DTT |  |  |  |  |  |  |
| NaCl | Sodium chloride, anhydrous, Redi-Dri™, free-flowing, ACS reagent, ≥99% | Sigma-Aldrich | 746398-500G | $79.70 | [[link](https://www.sigmaaldrich.com/US/en/product/sigald/746398?srsltid=AfmBOoryaSsUPjRtxIF88Ce1CXw0JgVbimmbLX0HKklYHtO1RFD6_Rhb)] | 4C to 30C |
| rATP  | Adenosine 5′-triphosphate disodium salt hydrate, BioXtra, ≥99% (HPLC), from microbial | Sigma-Aldrich | A7699-1G | $125.00 | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/a7699)] | -25C to -15C |
| rGTP | Guanosine 5′-triphosphate sodium salt hydrate, ≥ 95% (HPLC), powder | Sigma-Aldrich | G8877-100MG | $155 | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/g8877)] | -25C to -15C |
| rCTP | Cytidine 5′-triphosphate disodium salt, ≥95% | Sigma-Aldrich | C1506-100MG | $102.00 | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/c1506)] | -25C to -15C |
| rUTP | Uridine 5′-triphosphate trisodium salt hydrate, Type IV, ≥93.0% (HPLC) | Sigma-Aldrich | U6750-100MG | $58.20 | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/u6750)] | -25C to -15C |
| 0.3 U TIPP | Thermostable Inorganic Pyrophosphatase | New England Biolabas | M0296S | $82.00 | [[link](https://www.neb.com/en-us/products/m0296-thermostable-inorganic-pyrophosphatase)] | -25C to -15C |
| DFHBI-1T (dye) | DFHBI 1T | Tocris Bioscience | 5610 | $346.00 | [[link](https://www.tocris.com/products/dfhbi-1t_5610)] | -25C to -15C |
| MphR (plasmid) | pJBL715 | AddGene | 140385 | $85.00 | [[link](https://www.addgene.org/140385/)] | -25C to -15C |
| T7-mphO-3WJdb-T (plasmid) | pJBL716 | AddGene | 140386 | $85.00 | [[link](https://www.addgene.org/140386/)] | -25C to -15C |
| Forward primer | GCGGATAACAATTTCACACAGGAAACAGC |  |  |  |  | -25C to -15C |
| Reverse primer | CAAAAAACCCCTCAAGACCCG |  |  |  |  | -25C to -15C |
| PCR Kit | Phusion® High-Fidelity PCR Kit | New England Biolabs | E0553S | $84.00 | [link] | -25C to -15C |
| T7 RNAP* | T7 RNA Polymerase | New England Biolabs | M0251S | $74.00 | [[link](https://www.neb.com/en-us/products/m0251-t7-rna-polymerase)] | -25C to -15C |

\* Alternatively, the T7 RNAP is available within the [DNA Distribution](https://docs.nucleus.engineering/docs/dna-distro) as the component `pT7-lacO-UTR1-T7RNAP-tT7hyb6`

## Usage

### Preparation of purified MphR

Purified MphR from the plasmid pJBL715 is described in Jung *et al* (DOI: 10.1038/s41587-020-0571-7) and is likely compatible with the following guides:

- [Grow and Induce Expression Strains](https://docs.nucleus.engineering/docs/processes/make-protein/grow-bacteria/main)
- [Purify Proteins by Ni2+ Gravity Column](https://docs.nucleus.engineering/docs/processes/make-protein/purify-proteins-grav-column/main)

### Preparation of linear DNA templates

The DNA templates used in the ROSALIND system are purified linear PCR amplicons from the plasmid pJBL716 using the forward and reverse primers as described in Jung *et al* (DOI: 10.1038/s41587-020-0571-7).

It is recommended to use the Phusion PCR kit with the following thermocycle parameters: 98 C for 3 min—(98 C for 30 s, 71 C for 30 s, 72 C for 15 s) 25 cycles—72 C for 10 min—hold at 12 C. Purify the product via spin column into MQ water.

Characterize the size and purity of the product by running ~50–100 ng of the purified DNA template on a 2% TAE agarose gel to confirm the size and purity of the product.

### Stocks solutions and buffers

**Stock solutions**

1) Input Template, Dye, aTF and ligand stock concentrations. Add desired amounts per reaction for template, Dye and aTF. (Ligand is added below in step 6).

|  | Linear DNA Template | Dye | aTF | Ligand |
| --- | --- | --- | --- | --- |
| Name | pT7-mphO-3WJdb-T | DFHBI-1T | MphR-dimer | aTc |
| Stock concentration | 0.5 uM | 40.00 mM | 210 uM | 50 uM |
| Amount per reaction | 0.5 pmol | 45.00 nmol | 25 pmol |  |
| Volume per reaction | 1.0 uL | 1.13 uL | 0.12 uL |  |

**10x ROSALIND buffer**

| Reagent | 10x concentration [mM] |
| --- | --- |
| Spermidine | 20 |
| Tris-HCl (pH 8) | 400 |
| MgCl2 | 80 |
| DTT | 100 |
| NaCl | 200 |

**TRIS buffered nucleotides**

100 mM rNTPs are buffered in a 11.4 mM solution of TRIS-HCL (pH 7.5) and store at -25C to -15C.

### Transcription Mastermix

2) Prepare a mastermix by mixing the following components at room temperature.

| Reagent | Vol (uL) for 1 rxn | Vol (uL) for 5 rxn |
| --- | --- | --- |
| 10X ROSALIND Buffer | 2.00 | 10.00 |
| 100 mM ATP | 0.57 | 2.86 |
| 100 mM CTP | 0.57 | 2.86 |
| 100 mM GTP | 0.57 | 2.86 |
| 100 mM UTP | 0.57 | 2.86 |
| 0.3 U TIPP | 0.15 | 0.75 |
| DFHBI-1T | 1.13 | 5.63 |
| DNA | 1.00 | 5.00 |
| MphR | 0.12 | 0.60 |
| nuc. free H2O | 8.32 | 41.60 |
| Total | 15 | 75.00 |

3) For each desired reaction, aliquot 15 µL of incubated mastermix in each reaction tube.

4) Incubate the aliquoted mastermix at 37° C for 15 min to allow MphR:DNA equillibration.

5) Meanwhile prepare 1:10 dilution of T7 RNAP stock (stock concentration: 1 µg/µL).

6) For each desired reaction, add ligand, diluted T7 RNAP, and remaining water according to the table below. (Modify the table according to your experiment design.) Add these components immediately before transferring to a plate reader for measurement.

| Ligand Concentrations [pmol] | Volume of Ligand [uL] | Volume of diluted T7 RNAP [uL] | Volume of H2O [uL] |
| --- | --- | --- | --- |
| 0 | 0.00 | 2.00 | 3.00 |
| 25 | 0.50 | 2.00 | 2.50 |
| 50 | 1.00 | 2.00 | 2.00 |
| 100 | 2.00 | 2.00 | 1.00 |

# Performance Data

The performance of the MphR macrolides sensor is characterized using erythromycin - a common antibiotic used to treat a variety of bacterial infections. Here, 12.5 uM of erythromycin (Sigma Aldrich, cat no. [E5389](https://www.sigmaaldrich.com/US/en/product/sigma/e5389?srsltid=AfmBOopfybA84_YCzQ99mFwCReGjkem33XjzBVci6e25_mi_NsvL1zpy)) dissolved in ethanol is added to a ROSALIND reaction containing 208 uM MphR. The fluorescence response is expressed in units of micromolar equivalent fluorescein (MEF) using a NIST traceable fluorescein standard (Invitrogen, cat no. [F36915](https://www.thermofisher.com/order/catalog/product/F36915))

:::{figure} figures/ery_kinetics_12_5uM.png
:name: fig-ery-kinetics
:width: 75%

MphR can detect erythromycin. The three colored curves represent independent replicates in the presence of 12.5 uM erythromycin. The black curves shows the response with no erythromycin present. Original data from DOI: 10.1038/s41587-020-0571-7
:::

:::{figure} figures/ery_dose_response.png
:name: fig-ery-dose-response
:width: 75%

Dose response curve of MphR with erythromycin. Each data point is an independent biological replicate. Original data from DOI: 10.1038/s41587-020-0571-7
:::

MphR represses transcription until 2.5 uM erythromycin is introduced with a response saturation occurring at approximately 10 uM erythromycin. The kinetic time series data displayed for 12.5 uM erythromycin shows a response of 0.5 MEF within 1 hour.

The complete study wherein the behavior of MphR is characterized using the ROSALIND system can be found Jung *et al* (DOI: 10.1038/s41587-020-0571-7). There, additional macrolides - azithromycin, clarithromycin, and roxithromycin - were also characterized with slightly higher dose response thresholds to obtain saturation. Despite these different saturation thresholds, visible amounts of fluorescence could be observed within similar time frames. The author's of that study note that the "broad range of MphR specificity is expected based on its known promiscuity, and is probably a common feature of xenobiotic-sensing aTFs."

# Resources and References

- Other Protocols
    - Jung, J. K., Alam, K. K., & Lucks, J. B. (2022). ROSALIND: Rapid Detection of Chemical Contaminants with In Vitro Transcription Factor-Based Biosensors. In Cell-Free Gene Expression (pp. 325–342) [[link](https://link.springer.com/protocol/10.1007/978-1-0716-1998-8_20)]
- Papers
    - Alam, K. K., Tawiah, K. D., Lichte, M. F., Porciani, D. & Burke, D. H. A Fluorescent Split Aptamer for Visualizing RNA–RNA Assembly In Vivo. ACS Synthetic Biology vol. 6 1710–1721 (2017) [[link](https://pubs.acs.org/doi/10.1021/acssynbio.7b00059)]
    - Jung, J. K. et al. Cell-free biosensors for rapid detection of water contaminants. Nature Biotechnology vol. 38 1451–1459 (2020) [[link](https://www.nature.com/articles/s41587-020-0571-7)]
    - Kasey, C. M., Zerrad, M., Li, Y., Cropp, T. A. & Williams, G. J. Development of Transcription Factor-Based Designer Macrolide Biosensors for Metabolic Engineering and Synthetic Biology. ACS Synthetic Biology vol. 7 227–239 (2017) [[link](https://pubs.acs.org/doi/epdf/10.1021/acssynbio.7b00287)]
- Resources
    - N/A

# Credits

- Developers
    - [Stemloop](https://stemloop.com/)
- Testers
    - Untested
