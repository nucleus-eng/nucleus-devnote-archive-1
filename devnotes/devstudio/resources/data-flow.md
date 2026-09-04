# Data Flow

@Claude: format using standards in nucleus-skills; link to headers in this doc

Most arrows carry an ID (`e1`, `e2`, ...) and a status glyph. Arrows that
are known working are not labelled, because there is nothing to test.
See [Arrow status](#arrow-status) for the status of each one.

```mermaid
flowchart TD
    %% 
    %% STATUS STYLES
    %% 
    classDef eWorking stroke:#28a745,stroke-width:2px
    classDef eBroken  stroke:#d73a49,stroke-width:3.5px
    classDef eTesting stroke:#999999,stroke-width:1.5px,stroke-dasharray:5 4
    classDef eMissing stroke:#cccccc,stroke-width:1.5px,stroke-dasharray:2 5
    %% box styles: nWorking / nBroken / nTesting to follow the same pattern
    classDef nMissing fill:#fafafa,stroke:#bbbbbb,stroke-width:1.5px,stroke-dasharray:2 5,color:#777777

    %% 
    %% LOCATIONS
    %% 

    %% People
    DEV["Developers"]
    FAC["Facilitators"]

    %% Sites
    NUC["nucleus.engineering"]
    INV["Inventory [--]"]

    %% Plate Readers
    CY5["Cytation 5"]
    CY3["Cytation 3"]
    S2["Synergy 2"]

    %% Microscopes
    MS1["Cephla (#1)"]
    MS2["Cephla (#2)"]

    %% b.next computers
    GLY["Glycine"]
    TYR["Tyrosine"]
    VAL["Valine"]

    %% Servers
    R2["R2"]
    GDRIVE["GDrive"]
    GIT["GitHub"]
    CN["Curvenote"]

    %% 
    %% CONNECTIONS
    %% 

    %% User Access
    DEV e1@-->|"e1 [--]"| INV
    DEV e2@--> GDRIVE
    DEV e3@--> NUC

    FAC e4@-->|"e4 [--]"| INV
    FAC e5@-->|"e5 [?]"| R2
    FAC e6@--> GIT
    FAC e7@--> GDRIVE
    FAC e8@--> NUC

    %% Plate Reader Connections
    CY5 e9@-->|"e9 [?]"| GLY
    CY3 e10@-->|"e10 [?]"| GLY
    S2 e11@-->|"e11 [?]"| GLY

    %% Microscopy Connections
    MS1 e12@-->|"e12 [?]"| VAL
    MS2 e13@-->|"e13 [?]"| TYR

    %% Uploads to Servers
    TYR e14@-->|"e14 [?]"| R2
    VAL e15@-->|"e15 [?]"| R2
    GLY e16@-->|"e16 [?]"| R2
    GLY e17@-->|"e17 [?]"| GDRIVE

    %% Connections to Servers
    R2 e18@-->|"e18 [?]"| GIT
    GDRIVE e19@<-->|"e19 [?]"| GIT
    GIT e20@-->|"e20 [?]"| CN

    %% Serve Nucleus
    GIT e21@-->|"e21 [?]"| NUC
    CN e22@-->|"e22 [?]"| NUC

    %% 
    %% ARROW STATUS
    %% Move an ID between these four lines to change its status.
    %% 
    class e2,e3,e6,e7,e8 eWorking
    %% class e0 eBroken
    class e5,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22 eTesting
    class e1,e4 eMissing

    %% BOX STATUS
    class INV nMissing
```

## Legend

| Glyph | Status | Line | Meaning |
|---|---|---|---|
| [ok] | Working | Green, solid | Tested end to end. It works. |
| [x] | Broken | Red, thick | The connection exists but fails. |
| [?] | Needs testing | Grey, dashed | Built, but nobody has confirmed it. |
| [--] | Missing | Faint, dotted | Not built yet. |

## Arrow status

| ID  | From         | To                  | Status | Test | Notes                         |
|-----|--------------|---------------------|--------|------|-------------------------------|
| e1  | Developers   | Inventory           | [--]   |      | Inventory does not exist yet. |
| e2  | Developers   | GDrive              | [ok]   |      | Working. No label on diagram. |
| e3  | Developers   | nucleus.engineering | [ok]   |      | Working. No label on diagram. |
| e4  | Facilitators | Inventory           | [--]   |      | Inventory does not exist yet. |
| e5  | Facilitators | R2                  | [?]    |      |                               |
| e6  | Facilitators | GitHub              | [ok]   |      | Working. No label on diagram. |
| e7  | Facilitators | GDrive              | [ok]   |      | Working. No label on diagram. |
| e8  | Facilitators | nucleus.engineering | [ok]   |      | Working. No label on diagram. |
| e9  | Cytation 5   | Glycine             | [?]    |      |                               |
| e10 | Cytation 3   | Glycine             | [?]    |      |                               |
| e11 | Synergy 2    | Glycine             | [?]    |      |                               |
| e12 | Cephla (#1)  | Valine              | [?]    |      |                               |
| e13 | Cephla (#2)  | Tyrosine            | [?]    |      |                               |
| e14 | Tyrosine     | R2                  | [?]    |      |                               |
| e15 | Valine       | R2                  | [?]    |      |                               |
| e16 | Glycine      | R2                  | [?]    |      |                               |
| e17 | Glycine      | GDrive              | [?]    |      |                               |
| e18 | R2           | GitHub              | [?]    |      |                               |
| e19 | GDrive       | GitHub              | [?]    |      | Two-way                       |
| e20 | GitHub       | Curvenote           | [?]    |      |                               |
| e21 | GitHub       | nucleus.engineering | [?]    |      |                               |
| e22 | Curvenote    | nucleus.engineering | [?]    |      |                               |
