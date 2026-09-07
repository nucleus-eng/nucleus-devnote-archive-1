# Document Workflow

This document represents our workflow for documenting the DevStudio. 

Most arrows carry an ID (`e1`, `e2`, ...) and a status glyph. Arrows that
just show containment are not labelled, because there is nothing to test.
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

    DEV["Developers"]
    FAC["Facilitators"]
    GDRIVE["GDrive"]
    LOG["GDrive:Node/Log/"]
    GDN["GDrive:Node/DevNote/"]
    GDOCS["GDrive:Node/Docs/"]
    GIT["GitHub"]
    GITDN["GitHub:nucleus-eng/devnotes-repo/"]
    GITDOCS["GitHub:nucleus-eng/nucleus-docs/"]

    DEV e1@-->|"e1 [?]"| GDRIVE
    FAC e2@-->|"e2 [?]"| GIT
    FAC e3@-->|"e3 [?]"| GDRIVE

    GDRIVE e4@<-->|"e4 [?]"| GIT

    %% Containment. Working, so no label.
    GDRIVE e5@--> LOG
    GDRIVE e6@--> GDN
    GDRIVE e7@--> GDOCS

    %%Unclear? ask ARM
    LOG e8@-->|"e8 [?]"| LOG

    LOG e9@-->|"e9 [?]"| GDN

    %%Comment and review. Gates subsequent flow
    GDN e10@-->|"e10 [?]"| GDN

    GDN e11@-->|"e11 [?]"| GDOCS

    GDN e12@-->|"e12 [?]"| GITDN
    GITDN e13@-->|"e13 [?]"| GDOCS
    GDOCS e14@-->|"e14 [?]"| GITDOCS

    %% Comment and review. Gates subsequent flow
    GDOCS e15@-->|"e15 [?]"| GDOCS

    %% Containment. Working, so no label.
    GIT e16@--> GITDN
    GIT e17@--> GITDOCS

    %% 
    %% ARROW STATUS
    %% Move an ID between these four lines to change its status.
    %% 
    class e5,e6,e7,e16,e17 eWorking
    %% class e0 eBroken
    class e1,e2,e3,e4,e8,e9,e10,e11,e12,e13,e14,e15 eTesting
    %% class e0 eMissing
```

## Legend

| Glyph | Status | Line | Meaning |
|---|---|---|---|
| [ok] | Working | Green, solid | Tested end to end. It works. |
| [x] | Broken | Red, thick | The connection exists but fails. |
| [?] | Needs testing | Grey, dashed | Built, but nobody has confirmed it. |
| [--] | Missing | Faint, dotted | Not built yet. |

## Arrow status

| ID | From | To | Status | Test | Notes |
|---|---|---|---|---|---|
| e1 | Developers | GDrive | [?] | | |
| e2 | Facilitators | GitHub | [?] | | |
| e3 | Facilitators | GDrive | [?] | | |
| e4 | GDrive | GitHub | [?] | | Two-way |
| e5 | GDrive | Node/Log/ | [ok] | | Containment. No label on diagram. |
| e6 | GDrive | Node/DevNote/ | [ok] | | Containment. No label on diagram. |
| e7 | GDrive | Node/Docs/ | [ok] | | Containment. No label on diagram. |
| e8 | Node/Log/ | Node/Log/ | [?] | | Unclear? ask ARM |
| e9 | Node/Log/ | Node/DevNote/ | [?] | | |
| e10 | Node/DevNote/ | Node/DevNote/ | [?] | | Comment and review. Gates the next step. |
| e11 | Node/DevNote/ | Node/Docs/ | [?] | | |
| e12 | Node/DevNote/ | devnotes-repo | [?] | | |
| e13 | devnotes-repo | Node/Docs/ | [?] | | |
| e14 | Node/Docs/ | nucleus-docs | [?] | | |
| e15 | Node/Docs/ | Node/Docs/ | [?] | | Comment and review. Gates the next step. |
| e16 | GitHub | devnotes-repo | [ok] | | Containment. No label on diagram. |
| e17 | GitHub | nucleus-docs | [ok] | | Containment. No label on diagram. |

# Locations
Boxes in diagram above

## Laptops
Designing experiments, personal notes, drafting language, interacting with remainder of workflow.

### Developers
### Facilitators


## Google Drive
Q: what permissions for participants? and how?

### Log
### DevNotes
### Docs

## GitHub
All your bases...

### [nucleus-docs](https://github.com/nucleus-eng/nucleus-docs)
### [nucleus-devnotes](https://github.com/nucleus-eng/nucleus-devnote-archive-1)


# Workflows / Skills
Arrows in diagram above.
