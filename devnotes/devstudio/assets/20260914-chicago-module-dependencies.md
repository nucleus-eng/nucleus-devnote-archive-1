<!-- gen:composition-diagram -->
(fig:chicago-deps)=
```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    NC["Nucleus Cytosol"]
    MPC["Chicago Membrane<br/>POPC:Chol"]
    P_CYTOSOL(["Assemble Base Cytosol"])
    P_ANNEAL(["Anneal pH Trigger Duplex"])
    P_GUV(["Encapsulation: Phase Transfer"])
    P_SUV(["SUV Encapsulation"])
    P_AGAR(["Agarose Hydrogel Embedding"])
    P_PHOTO(["Photodevelop Gel"])
    P_READ(["Colorimetric Readout"])
    CHI["Chicago Chassis"]
    ATC["aTc Sensing Module"]
    PH["pH-Sensing Module"]
    ATCV["aTc Sensing Cell"]
    PHV["pH Sensing Cell"]
    PLA1["PLA1 Lysis Module"]
    LACZ["LacZ Reporter"]
    XYLE["XylE / C23DO Reporter"]
    SUV["Substrate SUV: CPRG"]
    ATCCAS["aTc Cascade"]
    PHCAS["pH Cascade"]
    CHICAS["Chicago Cascade"]
    G_AGAR["Gel: Agarose"]
    G_PEGN["Gel: PEG-Norbornene"]

    P_CYTOSOL --> NC
    P_ANNEAL --> PH
    P_SUV --> SUV
    NC --> CHI
    MPC --> CHI
    CHI --> P_GUV
    ATC --> ATCV
    PH --> PHV
    P_GUV --> ATCV
    P_GUV -.-> PHV
    ATCV --> ATCCAS
    PLA1 --> ATCCAS
    LACZ --> ATCCAS
    SUV --> ATCCAS
    XYLE -.-> ATCCAS
    PHV --> PHCAS
    PLA1 --> PHCAS
    LACZ --> PHCAS
    SUV --> PHCAS
    ATCCAS -.-> CHICAS
    PHCAS -.-> CHICAS
    PHCAS -.-> P_AGAR
    ATCCAS -.-> P_PHOTO
    P_AGAR --> G_AGAR
    P_PHOTO -.-> G_PEGN
    G_AGAR --> P_READ
    G_PEGN -.-> P_READ

    classDef chicago fill:#e3f0f8,stroke:#0072B2,color:#063a57;
    classDef shared fill:#def5ee,stroke:#009E73,color:#00402e;
    classDef process fill:#ffffff,stroke:#6b7280,color:#111827;
    class NC,MPC,PLA1,LACZ,XYLE,SUV shared;
    class CHI,ATC,PH,ATCV,PHV,ATCCAS,PHCAS,CHICAS,G_AGAR,G_PEGN chicago;
    class P_CYTOSOL,P_ANNEAL,P_GUV,P_SUV,P_AGAR,P_PHOTO,P_READ process;
    style PHV stroke-dasharray: 5 5
    style PHCAS stroke-dasharray: 5 5
    style CHICAS stroke-dasharray: 5 5
    style G_PEGN stroke-dasharray: 5 5
```
*Module dependencies for the Chicago Cascade demonstration.*
<!-- /gen:composition-diagram -->
