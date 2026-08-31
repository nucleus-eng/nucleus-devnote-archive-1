```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    MATERIALS["**Materials**\nReagents and plasmid stocks"]
    INSTRUMENT["**Instrument access & data delivery**\nPortable file delivery"]
    LIVESTREAM["**Livestream**\nFeed to YouTube"]
    PLATEMAP["**Platemap generation**\nMost critical, underdeveloped"]
    CDK["**CDK & compute access**\nColab-based compute tools"]
    FIGURES["**Figure generation & analysis**\nPublication-quality, editable"]
    DRAFTING["**Collaborative drafting environment**\nGoogle Drive workspace"]
    DECISIONS["**Decision making**\nIn-Studio RFCs"]
    DEVNOTE["**Draft → DevNote**\nGoogle Docs to MyST"]
    DOCS["**DevNote → Docs**\nDocumentation pages"]
    MGMT["**Documentation management**\nAdapt as constraints evolve"]
    DELIVERABLES["**Deliverables**\nDevNotes and documentation pages"]

    MATERIALS --> INSTRUMENT
    INSTRUMENT --> LIVESTREAM
    INSTRUMENT --> PLATEMAP
    PLATEMAP --> CDK
    CDK --> FIGURES
    FIGURES --> DRAFTING
    DRAFTING --> DEVNOTE
    DECISIONS -.-> DEVNOTE
    DEVNOTE --> DOCS
    DOCS --> MGMT
    MGMT --> DELIVERABLES

    classDef materials fill:#e5e7eb,color:#374151,stroke:#9ca3af;
    classDef pipeline fill:#dbeafe,color:#1e40af,stroke:#93c5fd;
    classDef side fill:#e5e7eb,color:#374151,stroke:#9ca3af;
    classDef decisions fill:#ede9fe,color:#5b21b6,stroke:#c4b5fd,stroke-dasharray: 5 5;
    classDef deliverables fill:#dcfce7,color:#166534,stroke:#86efac;

    class MATERIALS materials;
    class INSTRUMENT,PLATEMAP,CDK,FIGURES,DRAFTING,DEVNOTE,DOCS,MGMT pipeline;
    class LIVESTREAM side;
    class DECISIONS decisions;
    class DELIVERABLES deliverables;
```
