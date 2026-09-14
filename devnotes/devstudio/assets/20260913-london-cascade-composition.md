# London Cascade — composition

The London twin of `20260910-chicago-cascade-composition`, in the house greyscale. Boxes are
Modules, stadiums are the Processes that combine them, and each process carries its operator —
*mixing* into one compartment, *packing* into separate ones.

Light boxes are things you obtain, dark boxes are things a process makes. Rendered at depth 1:
anything obtainable is a leaf, so Base Cytosol appears whole rather than expanded. For the
expansion see `london-cascade-composition-deep`.

Generated 2026-09-13 from `docs/modules/london-cascade/spec.yml` by
`scripts/render-composition.py --depth 1`. It supersedes `london-module-dependencies`, which was
built by `gen-subsystem-tree.py` from the prose bullet list and therefore carries no processes
at all.

```mermaid
flowchart TD
    S30_LYSATE["Cytosol: S30 Lysate"]
    DETECTOR_3OC6_HSL["3OC6-HSL Detector Module"]
    EFFECTOR_PLA1["PLA1 Lysis Module"]
    MEMBRANE_POPC["London Membrane"]
    SUBSTRATE_CPRG["CPRG Substrate"]
    REPORTER_LACZ_ENZYME["LacZ Enzyme"]
    ULGA_POWDER["ULGA powder"]
    POTASSIUM_GLUTAMATE["Potassium L-glutamate"]
    HEPES["HEPES, pH 7.4"]
    GLUCOSE["Glucose"]

    P1_ASSEMBLE_CYTOSOL_0(["Assemble Cytosol (mixing)"])
    AHL_SENSOR_CYTOSOL["AHL Sensor Cytosol"]
    P2_ENCAPSULATE_SENSING_0(["Encapsulation: Phase Transfer (packing)"])
    AHL_SENSING_CELL["AHL Sensing Cell"]
    P3_ENCAPSULATE_SUBSTRATE_0(["Encapsulation: Phase Transfer (packing)"])
    GUV_CPRG["GUV: CPRG"]
    P4_ASSEMBLE_OUTER_SOLUTION_0(["Assemble Outer Solution (mixing)"])
    OUTER_SOLUTION["Outer Solution"]
    P5_EMBED_ULGA_0(["ULGA Embedding (packing)"])
    LONDON_CASCADE["London Cascade"]

    S30_LYSATE --> P1_ASSEMBLE_CYTOSOL_0
    DETECTOR_3OC6_HSL --> P1_ASSEMBLE_CYTOSOL_0
    EFFECTOR_PLA1 --> P1_ASSEMBLE_CYTOSOL_0
    P1_ASSEMBLE_CYTOSOL_0 --> AHL_SENSOR_CYTOSOL

    AHL_SENSOR_CYTOSOL --> P2_ENCAPSULATE_SENSING_0
    MEMBRANE_POPC --> P2_ENCAPSULATE_SENSING_0
    P2_ENCAPSULATE_SENSING_0 --> AHL_SENSING_CELL

    SUBSTRATE_CPRG --> P3_ENCAPSULATE_SUBSTRATE_0
    MEMBRANE_POPC --> P3_ENCAPSULATE_SUBSTRATE_0
    P3_ENCAPSULATE_SUBSTRATE_0 --> GUV_CPRG

    POTASSIUM_GLUTAMATE --> P4_ASSEMBLE_OUTER_SOLUTION_0
    HEPES --> P4_ASSEMBLE_OUTER_SOLUTION_0
    GLUCOSE --> P4_ASSEMBLE_OUTER_SOLUTION_0
    P4_ASSEMBLE_OUTER_SOLUTION_0 --> OUTER_SOLUTION

    ULGA_POWDER --> P5_EMBED_ULGA_0
    OUTER_SOLUTION --> P5_EMBED_ULGA_0
    REPORTER_LACZ_ENZYME --> P5_EMBED_ULGA_0
    AHL_SENSING_CELL --> P5_EMBED_ULGA_0
    GUV_CPRG --> P5_EMBED_ULGA_0
    P5_EMBED_ULGA_0 -->|"1:1:2"| LONDON_CASCADE


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class S30_LYSATE,DETECTOR_3OC6_HSL,EFFECTOR_PLA1,MEMBRANE_POPC,SUBSTRATE_CPRG,REPORTER_LACZ_ENZYME,ULGA_POWDER,POTASSIUM_GLUTAMATE,HEPES,GLUCOSE leaf;
    class AHL_SENSOR_CYTOSOL,AHL_SENSING_CELL,GUV_CPRG,OUTER_SOLUTION,LONDON_CASCADE composed;
    class P1_ASSEMBLE_CYTOSOL_0,P2_ENCAPSULATE_SENSING_0,P3_ENCAPSULATE_SUBSTRATE_0,P4_ASSEMBLE_OUTER_SOLUTION_0,P5_EMBED_ULGA_0 process;

    click S30_LYSATE "/docs/modules/s30-lysate/spec"
    click DETECTOR_3OC6_HSL "/docs/modules/detector-3oc6-hsl/spec"
    click EFFECTOR_PLA1 "/docs/modules/effector-pla1/spec"
    click MEMBRANE_POPC "/docs/modules/membrane-popc/spec"
    click SUBSTRATE_CPRG "/docs/modules/substrate-cprg/spec"
    click REPORTER_LACZ_ENZYME "/docs/modules/reporter-lacz-enzyme/spec"
    click ULGA_POWDER "/docs/modules/gel-ulga/spec"
    click P1_ASSEMBLE_CYTOSOL_0 "/docs/processes/assemble-cytosol/assemble-cytosol-main"
    click AHL_SENSOR_CYTOSOL "/docs/modules/ahl-sensor-cytosol/spec"
    click P2_ENCAPSULATE_SENSING_0 "/docs/processes/assemble-base-cell/main"
    click AHL_SENSING_CELL "/docs/modules/ahl-sensing-cell/spec"
    click P3_ENCAPSULATE_SUBSTRATE_0 "/docs/processes/assemble-base-cell/main"
    click GUV_CPRG "/docs/modules/guv-cprg/spec"
    click P4_ASSEMBLE_OUTER_SOLUTION_0 "/docs/processes/assemble-outer-solution/main"
    click P5_EMBED_ULGA_0 "/docs/processes/embed-ulga-hydrogel/main"
    click LONDON_CASCADE "/docs/modules/london-cascade/spec"
```
