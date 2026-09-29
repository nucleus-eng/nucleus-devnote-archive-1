<!-- gen:status-overlay -->
<!-- source: nucleus-eng/devstudio-readiness @ status/week1 : src/20260927-demo-ph.md -->
(fig:week1-ph)=
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    PH_RES["(M1) pH-responsive strand"]
    TRIGGER["(M2) Trigger"]
    CYTOSOL["(M3) Cytosol"]
    PH_DNA["(M4) pH-sensing DNA"]
    TOEHOLD["(M5) Toehold switch [PLA]"]
    CPRG["(M6) Substrate: CPRG"]
    MEMBRANE_V["(M7) Membrane"]
    PH_CYTOSOL["(M8) pH Sensor Cytosol"]
    MEMBRANE_C["(M9) Chicago Base Membrane: POPC/Chol<br/>Membrane[POPC ⊞ Chol ⊞ Rhod], 9:1, 0.1% Rhod"]
    CPRG_VESICLE["(M10) CPRG Vesicle"]
    PH_CELL["(M11) pH Sensing Cell"]
    HYDROGEL["(M12) Hydrogel: LGA"]
    BASIC_BUFFER["(M13) Basic buffer ⊞ LacZ Enzyme"]
    RELEASED_GEL["(M14) CPRG released gel"]
    COLOR["Color"]

    P1(["P1 &middot; Anneal pH-Responsive Trigger Duplex<br/>3:1"])
    P2(["P2 &middot; Assemble Aqueous Solution"])
    P3(["P3 &middot; Encapsulation: LUV preparation"])
    P4(["P4 &middot; Encapsulation: Phase Transfer"])
    P5(["P5 &middot; Gel embed &amp; incubation, 37 &deg;C"])
    P6(["P6 &middot; Color Development<br/>incubation"])

    PH_RES --> P1
    TRIGGER --> P1
    P1 --> PH_DNA

    CYTOSOL --> P2
    PH_DNA --> P2
    TOEHOLD --> P2
    P2 --> PH_CYTOSOL

    CPRG --> P3
    MEMBRANE_V --> P3
    P3 --> CPRG_VESICLE

    PH_CYTOSOL --> P4
    MEMBRANE_C --> P4
    P4 --> PH_CELL

    CPRG_VESICLE --> P5
    PH_CELL --> P5
    HYDROGEL --> P5
    P5 --> RELEASED_GEL

    BASIC_BUFFER --> P6
    RELEASED_GEL --> P6
    P6 --> COLOR

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

    class PH_RES,TRIGGER,CYTOSOL,TOEHOLD,MEMBRANE_C m_green;
    class CPRG,MEMBRANE_V,BASIC_BUFFER m_orange;
    class HYDROGEL m_gray;
    class PH_DNA,PH_CYTOSOL,PH_CELL b_green;
    class CPRG_VESICLE b_orange;
    class RELEASED_GEL,COLOR b_gray;
    class P1,P2,P4 p_green;
    class P3,P6 p_orange;
    class P5 p_gray;
    class LEG_GREEN m_green;
    class LEG_ORANGE m_orange;
    class LEG_RED m_red;
    class LEG_GRAY,LEG_MODULE m_gray;
    class LEG_BUILT b_gray;
    class LEG_PROCESS p_gray;
    style LEGEND fill:#ffffff,stroke:#9ca3af,color:#111827
```
*The pH Sensing demonstration releases CPRG from a vesicle when low pH opens a toehold switch that expresses PLA1, giving a color read out of a gel. Status at the end of Week 1: the sensing chain through the pH Sensing Cell is green, the CPRG vesicle branch is orange on unresolved leakiness, and no gel has been used for this demonstration.*
<!-- /gen:status-overlay -->
