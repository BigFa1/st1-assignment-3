# Software Technology 1 Assignment 3

One group repository and one evolving SmartCare application.
Baseline: Stage 6 foundation, 2026 revision 2. This starter deliberately leaves the three Stage 6 service tasks incomplete.

## Group index

- Group and tutorial: Monday 9:30–11:30, Group 4.
- Member names, GitHub usernames and UG/PG cohorts: Fahad Almajeed (@BigFa1, UG) and Mohammed Aboset (@MohammedAboset, UG).
- Shared repository URL: https://github.com/BigFa1/st1-assignment-3
- Latest completed stage: Stage 8 code integrated and verified. Final evidence handover pending. Stage 9 in progress.
- Verified code SHA: 362e9ba222741ab893d0b7a7cb15305b50519168 (Stage 8 integrated code; Stage 9 final SHA pending).
- Test command, working directory and observed result: py -m pytest -q from project/ on feature/stage9-queries. Result: 39 passed, 0 failed, in 0.07s. Stage 9 changes not yet integrated.
- Final submitted SHA, if different from tested code SHA: Pending Stage 9 review and merge. The final integrated SHA will be recorded after completion.

Do not put student IDs, private peer ratings, credentials or personal contact details here.

## Complete package and stage sequence

All Assignment 3 ordinary materials are supplied at the beginning: the Overview, Git/GitHub Group Guide, Stage 6–12 handouts, this incomplete SmartCare starter, all seven blank activity/evidence records, and assessment instructions/forms. Stage numbers control the engineering sequence, not document availability.

Start with Stage 6. Complete each stage only after the previous applicable stage has been integrated, verified and recorded.

UG: 6 → 7 → 8 → 9 → 12

PG: 6 → 7 → 8 → 9 → 10 → 11 → 12

Use ONE group repository and ONE evolving project/ throughout. The stage folders contain your response/evidence records; all templates are already present. Preserve previous code, tests, records and Git history. Never replace project/ with another starter or copy completed staff reference implementations: those are private staff material.

Stages 10 and 11 are PG-only. UG skipping these stages is correct and complete. In an UG-only submission, retain the supplied PG-only templates unchanged as intentionally not applicable; do not fill them with fabricated N/A responses. Optional UG collaboration is voluntary and unassessed. Mixed groups protect the verified common Stage 9 SHA while PG extends the same project. Use only the teaching team's confirmed Copilot agent capability or approved equivalent route.

The Stage 8 preparation utility version 1.1 is a controlled teaching asset supplied or run by teaching staff when Stage 8 begins. Follow the instructions provided by your tutor. It is not included in the normal student package. If temporarily supplied for the handout commands, keep it in a sibling Stage_8_Assets/ folder outside the repository. Never include it in Git or the final submission. The Stage 7 checkpoint and Stage 8 technical activity are unchanged.

Complete the supplied Stage 12 record when you reach Stage 12. UG releases the common scope; PG releases the extended scope, protecting the common SHA where needed. Record exact tested/submitted SHAs and create one source ZIP as the handout directs, without duplicate application copies per stage.

## Application and evidence

- [Application setup and commands](project/README.md)
- [Stage 6 activities and evidence](stage06/stage06_activities_and_evidence.md)
- [Stage 7 activities and evidence](stage07/stage07_activities_and_evidence.md)
- [Stage 8 activities and evidence](stage08/stage08_activities_and_evidence.md)
- [Stage 9 activities and evidence](stage09/stage09_activities_and_evidence.md)
- [Stage 10 PG activities and evidence](stage10_pg/stage10_activities_and_evidence.md)
- [Stage 11 PG activities and evidence](stage11_pg/stage11_activities_and_evidence.md)
- [Stage 12 activities and evidence](stage12/stage12_activities_and_evidence.md)

Git commands in the practical guide run from this root. Application commands run from project/:

```sh
cd project
python main.py
python -m pytest
cd ..
```

Use the approved environment described in the Git/GitHub group guide. The verified baseline is Python 3.13 with pytest 8.3.5. GitHub Copilot is the nominated assistant; verify significant output and record required decisions. Use synthetic data only. Use each supplied record only when you reach that stage in the applicable sequence.


## Stage 9 - Queries and Console Integration

The SmartCare application now supports appointment queries and an interactive console menu.

### How to run

Open the terminal in the `project/` directory.

Run the original demo:
```powershell
py main.py
```

Run the interactive menu:
```powershell
py main.py --interactive
```

Run all tests:
```powershell
py -m pytest -q
```

### Features

The interactive menu supports:
- Registering and finding patients.
- Registering and finding practitioners.
- Booking and cancelling appointments.
- Finding appointments, including cancelled appointments.
- Listing practitioner appointments with optional status filtering.
- Sorting appointments by date/time and appointment ID.
- Handling invalid inputs without closing the menu.

### Testing

The Stage 9 query and workflow tests were added to the existing test suite.

Latest verified result: 39 tests passed, 0 failed.

### Limitations

- Data is stored in memory and is lost when the program exits.
- No database or persistent storage is implemented.
- Appointment rescheduling is not supported.
- The application uses synthetic data for testing and demonstration.
