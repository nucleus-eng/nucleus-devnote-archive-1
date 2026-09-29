<!-- gen:status-overlay -->
<!-- source: nucleus-eng/devstudio-readiness @ status/week1 : src/20260927-demo-ahl-lysate.md -->
(fig:week1-ahl-lysate)=
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    LYSATE["(M1) S30 Lysate"]
    LUXR["(M2) 3OC6-HSL Detector<br/>LuxR"]
    GFP["(M3) deGFP Reporter"]
    OUTER_SOLUTION["(M4) London Outer Solution"]
    MEMBRANE["(M5) London Membrane: POPC"]
    SENSOR_LYSATE["(M6) AHSL Sensor Cytosol<br/>in S30 Lysate"]
    SENSOR_CELL["(M7) AHSL Sensing Cell<br/>SensorCell[AHSL]⟨GFP⟩"]
    ULGA["(M8) Gel: ULGA<br/>2&times;"]
    SOURCE["(M9) Bacteria &rarr; AHSL &rarr;<br/>LuxR sensing cascade"]
    SIGNAL["(M10) deGFP Reporter"]
    SPECTROMETER["(M11) Spectrometer"]
    UV["(M12) UV lamp"]

    P1(["P1 &middot; Plasmid assemble"])
    P2(["P2 &middot; Assemble Aqueous Solution"])
    P3(["P3 &middot; Encapsulation: Phase Transfer"])
    P4(["P4 &middot; Gel embed"])

    LUXR --> P1
    GFP --> P1
    P1 --> PLASMID

    PLASMID["Plasmid"]
    LYSATE --> P2
    PLASMID --> P2
    P2 --> SENSOR_LYSATE

    OUTER_SOLUTION --> P3
    MEMBRANE --> P3
    SENSOR_LYSATE --> P3
    P3 --> SENSOR_CELL

    ULGA --> P4
    SENSOR_CELL --> P4
    P4 --> DEVICE

    DEVICE["Embedded gel"]
    SOURCE --> DEVICE
    DEVICE --> SIGNAL
    SIGNAL --> SPECTROMETER
    UV --> SPECTROMETER

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

    class LYSATE,LUXR,GFP m_orange;
    class OUTER_SOLUTION,MEMBRANE,ULGA,SOURCE,UV m_gray;
    class PLASMID,SENSOR_LYSATE b_orange;
    class SENSOR_CELL,DEVICE,SIGNAL,SPECTROMETER b_gray;
    class P1,P2 p_orange;
    class P3,P4 p_gray;
    class LEG_GREEN m_green;
    class LEG_ORANGE m_orange;
    class LEG_RED m_red;
    class LEG_GRAY,LEG_MODULE m_gray;
    class LEG_BUILT b_gray;
    class LEG_PROCESS p_gray;
    style LEGEND fill:#ffffff,stroke:#9ca3af,color:#111827
```
*The LuxR-GFP Sensor demonstration detects 3OC6-HSL through LuxR in S30 Lysate and reports it as deGFP fluorescence. Status at the end of Week 1: the sensor chain is orange conservatively, because the dose response ran in Nucleus Cytosol rather than the lysate this figure draws, and no Sensing Cell has been encapsulated.*
<!-- /gen:status-overlay -->
