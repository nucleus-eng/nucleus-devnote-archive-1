<!-- gen:status-overlay -->
<!-- source: nucleus-eng/devstudio-readiness @ status/week1 : src/20260927-demo-ahl-cytosol-craic.md -->
(fig:week1-craic)=
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    CYTOSOL_A["(M1A) Cytosol"]
    SENSOR_DNA["(M2) Sensor: EsaR DNA"]
    SENSOR_PROTEIN["(M3) Sensor: EsaR protein"]
    CYTOSOL_B["(M1B) Cytosol"]
    REPORTER_DNA["(M5) Effector: PLA1<br/>as DNA"]
    SENS_CY["(M8i) Sensor Cytosol[AHSL]"]
    OS_I["(M6i) OS_i"]
    MEMBRANE_I["(M7i) Membrane_i"]
    SENS_CELL["(M9) SensorCell[AHSL]<br/>⟨PLA1⟩"]
    DYE["(M8Sj) Dye"]
    MEMBRANE_J["(M7j) Membrane_j"]
    OS_J["(M6j) OS_j"]
    DYE_VESICLE["(M12) Dye Vesicle⟨CPRG⟩"]
    GEL["(M10) Gel: ULGA"]
    ENZ["(M11) LacZ Enzyme"]
    DEVICE_OFF["(M14) Device[OFF]"]
    AHSL["(M13) Analyte: 3OC6-HSL<br/>AHSL"]
    DEVICE_ON["(M14) Device[ON]"]
    OBSERVATION["Observation"]

    P1A(["P1A &middot; Assemble Solution"])
    P1B(["P1B &middot; Assemble Aqueous Solution, again"])
    P2I(["P2i &middot; Encapsulation"])
    P2J(["P2j &middot; Encapsulation"])
    P3(["P3 &middot; Gel Embed"])
    P4(["P4 &middot; Incubate / Detection"])
    P5(["P5 &middot; Obs"])

    CYTOSOL_A --> P1A
    SENSOR_DNA --> P1A
    P1A --> SENSOR_PROTEIN

    CYTOSOL_B --> P1B
    SENSOR_PROTEIN --> P1B
    REPORTER_DNA --> P1B
    P1B --> SENS_CY

    OS_I --> P2I
    MEMBRANE_I --> P2I
    SENS_CY --> P2I
    P2I --> SENS_CELL

    OS_J --> P2J
    MEMBRANE_J --> P2J
    DYE --> P2J
    P2J --> DYE_VESICLE

    SENS_CELL --> P3
    GEL --> P3
    ENZ --> P3
    DYE_VESICLE --> P3
    P3 --> DEVICE_OFF

    DEVICE_OFF --> P4
    AHSL --> P4
    P4 --> DEVICE_ON
    DEVICE_ON --> P5
    P5 --> OBSERVATION

    subgraph LEGEND["Legend"]
        direction LR
        LEG_GREEN["Works here"] ~~~ LEG_ORANGE["Needs tuning"] ~~~ LEG_RED["Ruled out"] ~~~ LEG_GRAY["Not attempted"]
        LEG_MODULE["Module<br/>thin border"] ~~~ LEG_BUILT["Built<br/>thick border"] ~~~ LEG_PROCESS(["Process"])
    end

    %% Status is the fill. Node kind is the border weight and the shape.
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

    class CYTOSOL_A,SENSOR_DNA,CYTOSOL_B,DYE,MEMBRANE_J,OS_J,ENZ m_orange;
    class REPORTER_DNA,OS_I,MEMBRANE_I,GEL,AHSL m_gray;
    class SENSOR_PROTEIN,DYE_VESICLE b_orange;
    class SENS_CY,SENS_CELL,DEVICE_OFF,DEVICE_ON,OBSERVATION b_gray;
    class P1A,P1B,P2J p_orange;
    class P2I,P3,P4,P5 p_gray;
    class LEG_GREEN m_green;
    class LEG_ORANGE m_orange;
    class LEG_RED m_red;
    class LEG_GRAY,LEG_MODULE m_gray;
    class LEG_BUILT b_gray;
    class LEG_PROCESS p_gray;
    style LEGEND fill:#ffffff,stroke:#9ca3af,color:#111827
```
*CRAIC, a Colorimetric Reporter for AHL In Cytosol, detects AHSL through EsaR in Nucleus Cytosol and reports it by releasing CPRG from a dye vesicle in a gel. Status at the end of Week 1: no node is green, because mNeon stands in for PLA1 and the dye branch carries the same unresolved leakiness as the pH demonstration.*
<!-- /gen:status-overlay -->
