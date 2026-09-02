(fig:devstudio-pipeline)=
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    MATERIALS["Materials"]
    PLATEMAP["Platemap generation"]
    INSTRUMENT["Instrument access & data delivery"]
    CDK["CDK & compute access"]
    FIGURES["Figure generation & analysis"]
    DRAFTING["Collaborative drafting environment"]
    DECISIONS["Decision making"]
    DEVNOTE["Draft → DevNote"]
    DOCS["DevNote → Docs"]
    MGMT["Documentation management"]
    DELIVERABLES["Deliverables"]

    MATERIALS --> PLATEMAP
    PLATEMAP --> INSTRUMENT
    INSTRUMENT --> CDK
    CDK --> FIGURES
    FIGURES --> DRAFTING
    DRAFTING --> DEVNOTE
    DECISIONS -.-> DEVNOTE
    DEVNOTE --> DOCS
    DOCS --> MGMT
    MGMT --> DELIVERABLES

    classDef shared fill:#def5ee,stroke:#009E73,color:#00402e;
    classDef process fill:#ffffff,stroke:#6b7280,color:#111827;

    class MATERIALS,DELIVERABLES shared;
    class PLATEMAP,INSTRUMENT,CDK,FIGURES,DRAFTING,DEVNOTE,DOCS,MGMT,DECISIONS process;
    style DECISIONS stroke-dasharray: 5 5
```
*End-to-end pipeline from bench materials through documentation delivery.*
