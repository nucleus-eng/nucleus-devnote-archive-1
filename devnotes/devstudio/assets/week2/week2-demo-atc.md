<!-- Status overlay for Week 2, transcribed from the participants' boards. -->
(fig:week2-atc)=
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    CYTOSOL["(M1) Cytosol"]
    LACZ["(M2) LacZ"]
    TETO_PLA["(M3) TetO-PLA"]
    TETR["(M4) TetR"]
    OUTER_SOLN["(M5) Chicago Outer Solution<br/>400 mM glucose ⊞ 1 M HEPES"]
    LIPID["(M6) Chicago Base Membrane: POPC/Chol<br/>Membrane[POPC ⊞ Chol ⊞ Rhod], 9:1"]
    SENSOR_CYTOSOL["(M7) aTc Sensor Cytosol"]
    MINERAL_OIL["(M8) Mineral oil"]
    PEG_NB["(M9) Gel: PEG-Norbornene"]
    SENSOR_CELL["(M10) aTc Sensing Cell<br/>SensorCell[aTc]⟨PLA1⟩"]
    CPRG["(M11) Substrate: CPRG"]
    ATC["(M12) Analyte: aTc<br/>&plusmn;"]
    CASCADE["(M13) aTc Cascade"]
    OUTCOME["Red +aTc / Orange &minus;aTc"]

    P1(["P1 &middot; Assemble Sensor"])
    P2(["P2 &middot; Assemble Aqueous Solution"])
    P3(["P3 &middot; Encapsulation: Phase Transfer"])
    P4(["P4 &middot; Embed"])
    P5(["P5 &middot; Trigger Solution"])
    P6(["P6 &middot; Addition of Solution to gel"])
    P7(["P7 &middot; Observation"])

    TETO_PLA --> P1
    TETR --> P1
    P1 --> SENSOR

    SENSOR["Sensor"]
    CYTOSOL --> P2
    LACZ --> P2
    SENSOR --> P2
    P2 --> SENSOR_CYTOSOL

    LIPID --> P3
    SENSOR_CYTOSOL --> P3
    MINERAL_OIL --> P3
    OUTER_SOLN --> P3
    P3 --> SENSOR_CELL

    PEG_NB --> P4
    SENSOR_CELL --> P4
    P4 --> GEL_PIECE

    GEL_PIECE["Embedded gel"]
    CPRG --> P5
    ATC --> P5
    P5 --> TRIGGER_SOLN

    TRIGGER_SOLN["Trigger Solution"]
    GEL_PIECE --> P6
    TRIGGER_SOLN --> P6
    P6 --> CASCADE
    CASCADE --> P7
    P7 --> OUTCOME

    %% Status is the fill. Node kind is the border weight and the shape.
    subgraph LEGEND["Legend"]
        direction LR
        LEG_GREEN["Works here"] ~~~ LEG_ORANGE["Needs tuning"] ~~~ LEG_RED["Ruled out"] ~~~ LEG_GRAY["Not attempted"]
        LEG_MODULE["Module<br/>thin border"] ~~~ LEG_BUILT["Built<br/>thick border"] ~~~ LEG_PROCESS(["Process"])
    end

    classDef m_green  fill:#E3F4DD,stroke:#5E8F52,stroke-width:1.5px,color:#111827;
    classDef m_orange fill:#FBE3C4,stroke:#A85F00,stroke-width:1.5px,color:#111827;
    classDef m_red    fill:#F5D6CC,stroke:#8A2B12,stroke-width:1.5px,color:#111827;
    classDef m_gray   fill:#E5E7EB,stroke:#6B7280,stroke-width:1.5px,color:#111827;
    classDef b_green  fill:#E3F4DD,stroke:#5E8F52,stroke-width:3px,color:#111827;
    classDef b_orange fill:#FBE3C4,stroke:#A85F00,stroke-width:3px,color:#111827;
    classDef b_red    fill:#F5D6CC,stroke:#8A2B12,stroke-width:3px,color:#111827;
    classDef b_gray   fill:#E5E7EB,stroke:#6B7280,stroke-width:3px,color:#111827;
    classDef p_green  fill:#E3F4DD,stroke:#5E8F52,stroke-width:1.5px,color:#111827;
    classDef p_orange fill:#FBE3C4,stroke:#A85F00,stroke-width:1.5px,color:#111827;
    classDef p_red    fill:#F5D6CC,stroke:#8A2B12,stroke-width:1.5px,color:#111827;
    classDef p_gray   fill:#E5E7EB,stroke:#6B7280,stroke-width:1.5px,color:#111827;

    class TETO_PLA,TETR,CYTOSOL,LACZ,OUTER_SOLN,LIPID,MINERAL_OIL,PEG_NB,CPRG,ATC m_orange;
    class SENSOR,SENSOR_CYTOSOL,SENSOR_CELL,GEL_PIECE,TRIGGER_SOLN,CASCADE,OUTCOME b_orange;
    class P1,P2,P3,P4,P5,P6,P7 p_orange;
    class LEG_GREEN m_green;
    class LEG_ORANGE m_orange;
    class LEG_RED m_red;
    class LEG_GRAY,LEG_MODULE m_gray;
    class LEG_BUILT b_gray;
    class LEG_PROCESS p_gray;
    style LEGEND fill:#ffffff,stroke:#9ca3af,color:#111827
```
*The aTc Sensor demonstration uses TetR repression of a TetO-PLA construct, so that aTc triggers lysis and a colorimetric readout from a PEG-NB gel. Status at the end of Week 2: every node is orange, with no gray and no green. The demonstration was assembled in full and assayed, and leaky expression of tetO made the readout ambiguous. Compare {ref}`the same board at the end of Week 1 <fig:week1-atc>`.*
