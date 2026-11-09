# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Monday 9:30–11:30, Group 4
Members and UG/PG applicability: Fahad Almajeed (@BigFa1, UG) and Mohammed Aboset (@MohammedAboset, UG). Both members follow the undergraduate pathway. Stages 10 and 11 are not applicable.


## A Release scope and starting SHA

Release label/version and requirements baseline:
SmartCare v1.0 course release candidate. Based on Assignment 3 Overview/revision 2 requirements. The undergraduate release includes Stages 6, 7, 8, 9 and 12, covering FR-01–FR-09, QRY-01–04, FP-01–03 and the interactive console requirements.
Common starting SHA / branch / applicable members:
Starting SHA: 26a6195ac76a66298b98a3e383fb0a6406f2b918. Branch: feature/stage12-release, created from main. Applies to Fahad Almajeed (@BigFa1) and Mohammed Aboset (@MohammedAboset), both undergraduate students.
PG starting SHA / branch / applicable members or not applicable:
Not applicable. Both group members are undergraduate students, so Stages 10 and 11 are not required.
Working-state review and approved integration:
Stages 6–9 were completed, reviewed and merged into main. The Stage 12 branch was created from the updated main branch. Git status confirmed a clean working tree with no uncommitted changes. All 39 tests passed during the previous verification.
Protected common candidate and PG differences:
The starting common candidate is commit 26a6195ac76a66298b98a3e383fb0a6406f2b918. This contains the completed undergraduate work from Stages 6–9. No PG extension is required. The final release SHA will be recorded after Stage 12 verification and integration.
Feature freeze / owner / verifier:
No optional features will be added during Stage 12. Only necessary release corrections will be considered. Mohammed Aboset will prepare the release evidence and checks. Fahad Almajeed will be asked to independently review and verify the final release before approval.

## B Requirements and release readiness matrix

Tutorial activity 1: Decision: Do not release yet. Even if all tests pass, the project is not fully ready because the README is incomplete, one dependency has not been reviewed, and a known limitation is undocumented. The team must complete the README, review the dependency, and document the limitation before releasing the project. After resolving these issues, the team should verify the release again.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope                   | Evidence                                                 | Location/link and SHA                                                               | Reviewer                 | Sufficient?        | Gap/action                            |
|-------------------------------------------------------|----------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------|--------------------|---------------------------------------|
| Cancellation history works                            | Cancellation and retained appointment tests collected    | tests/test_regressions.py, tests/test_services.py; starting SHA 26a6195             | Mohammed (initial check) | Pending final run  | Confirm full regression               |
| Architecture responsibilities are appropriate         | Domain, service and query tests collected                | tests/test_domain.py, tests/test_services.py, tests/test_queries.py; 26a6195        | Pending review           | Pending            | Review code responsibilities          |
| Rescheduling is safe — PG only                        | Not applicable to UG                                     | PG only                                                                             | Not applicable           | N/A                | None                                  |
| AI use is responsible — common recheck / PG assurance | Earlier development and review evidence to be checked    | Stage 6–9 records; 26a6195                                                          | Pending review           | Pending            | Complete final AI review              |
| System is maintainable                                | Separate domain, service, query and workflow tests       | project/tests; 26a6195                                                              | Pending review           | Pending            | Check code quality and README         |
| FR-01–03 register/find and validation                 | Patient and practitioner tests collected                 | tests/test_domain.py, tests/test_services.py, tests/test_starter.py; 26a6195        | Mohammed (initial check) | Pending final run  | Verify registration and lookup        |
| FR-04–05 booking/conflict rules                       | Booking and conflict tests collected                     | tests/test_starter.py, tests/test_services.py, tests/test_regressions.py; 26a6195   | Mohammed (initial check) | Pending final run  | Verify booking conflicts              |
| FR-06–08 cancellation/history/find                    | Cancellation and retrieval tests collected               | tests/test_services.py, tests/test_regressions.py, tests/test_workflows.py; 26a6195 | Mohammed (initial check) | Pending final run  | Verify retained history               |
| FR-09 and QRY/FP listing/filter/order/purity          | Seven query tests collected                              | tests/test_queries.py; 26a6195                                                      | Mohammed (initial check) | Pending final run  | Verify sorting and filtering          |
| UI full console sequence and error recovery           | Previous interactive demonstration completed             | project/main.py; 26a6195                                                            | Mohammed (previous demo) | Pending final demo | Repeat complete release demonstration |
| Session-only scope / FR-10 retired                    | Previous application output identified session-only data | project/main.py; 26a6195                                                            | Pending review           | Pending            | Confirm and document limitation       |
| PG RES and assurance integration                      | Not applicable to UG                                     | PG only                                                                             | Not applicable           | N/A                | None                                  |

## C Full regression results

| Suite/scope                              | Environment/version         | Working directory and command | Tested SHA     | Actual result                  | Evidence link  |
|------------------------------------------|-----------------------------|-------------------------------|----------------|--------------------------------|----------------|
| Complete common                          | Python 3.14.7, pytest 9.2.0 | project/; python -m pytest -q | 26a6195        | PASS: 39 tests passed in 0.01s | project/tests/ |
| Complete PG if applicable                | Not applicable (UG only)    | Not applicable                | Not applicable | Not applicable                 | Not applicable |
| Affected focused checks after correction | No corrections made yet     | Not required at this stage    | 26a6195        | Pending final release review   | Pending        |
| Full integrated recheck                  | Python 3.14.7, pytest 9.2.0 | project/; python -m pytest -q | 26a6195        | PASS: 39 tests passed in 0.01s | project/tests/ |
Prior assertions preserved / reviewed test diff: All 39 existing tests passed. No test changes have been made during Stage 12 so far. Final test-diff review is pending.
Remaining failure / limitation: No test failures were found. The application uses session-only data, which is an accepted course limitation. Final release checks are still required.

## D Console and end to end demonstration

| Demo step                                                        | Synthetic setup/input                                         | Expected requirement                                      | Observed result                                                   | Evidence/link             |
|------------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------|---------------------------|
| Problem and stakeholders                                         | SmartCare appointment management                              | Manage patients, practitioners and appointments           | Application supports the required appointment management features | project/main.py           |
| Register and find Patient and two Practitioners                  | Synthetic patient and practitioner records                    | Registration and lookup work correctly                    | Passed during manual testing                                      | project/main.py           |
| Valid booking                                                    | Valid patient, practitioner, date and time                    | Appointment is created successfully                       | Passed during manual testing                                      | project/main.py           |
| Same practitioner exact-time conflict rejected                   | Two appointments for the same practitioner and time           | Conflicting booking is rejected                           | Passed during manual testing                                      | tests/test_regressions.py |
| Different practitioner same time allowed                         | Two practitioners with the same appointment time              | Booking is allowed                                        | Passed during manual testing                                      | tests/test_starter.py     |
| Cancel SCHEDULED and retain/find CANCELLED object                | Cancel an existing appointment                                | Appointment remains available with CANCELLED status       | Passed during manual testing                                      | tests/test_services.py    |
| Invalid/repeated cancellation rejected                           | Attempt to cancel an invalid or already cancelled appointment | Invalid cancellation is rejected                          | Passed during manual testing                                      | tests/test_services.py    |
| Default all-status listing                                       | List practitioner appointments without status filter          | All applicable appointments are displayed                 | Passed during manual testing                                      | tests/test_queries.py     |
| Explicit filtering / empty vs unknown / deterministic order      | Filter and sort practitioner appointments                     | Correct filtering and ordering                            | Passed during manual testing                                      | tests/test_queries.py     |
| Invalid date/status/menu/lookup recovery and continued operation | Enter invalid inputs                                          | Errors are handled without crashing                       | Passed during manual testing                                      | tests/test_workflows.py   |
| Session-only limitation and normal exit                          | Exit the application                                          | Application closes and session data is not saved          | Application exited correctly; data is session-only                | project/main.py           |
| One meaningful requirement-linked pytest test explained          | Booking conflict regression test                              | Same practitioner cannot be double-booked                 | Test passed in the 39-test suite                                  | tests/test_regressions.py |
| Architecture and one actual AI decision / known limitation       | Domain, services, queries and console                         | Responsibilities are separated and limitations understood | Architecture review and AI decision explanation still pending     | project/                  |
| PG reschedule identity/participants/time and no-op               | Not applicable                                                | PG only                                                   | Not applicable                                                    | Not applicable            |
| PG conflict/invalid status/failure non-mutation                  | Not applicable                                                | PG only                                                   | Not applicable                                                    | Not applicable            |
| PG old slot / current lookup/list ordering / assurance risks     | Not applicable                                                | PG only                                                   | Not applicable                                                    | Not applicable            |
Stable demo owner / fresh process / command: Mohammed Aboset. Application started using python main.py --interactive from project/. The interactive menu opened correctly. User reports that all menu functions worked during manual testing.
PG demonstrations through service/tests or not applicable: Not applicable. Both group members are undergraduate students.

## E Final code quality and AI review

| Review area                                                     | Code/evidence location                          | Finding or no finding                                                                       | Correction/no change and recheck               |
|-----------------------------------------------------------------|-------------------------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------|
| OOP responsibilities and pure-query boundaries                  | smartcare/domain.py, data_store.py, services.py | Domain, storage and service responsibilities are separated. Query module review is pending. | No changes to reviewed functionality.          |
| PascalCase and snake_case naming                                | domain.py, data_store.py, services.py           | Naming conventions followed.                                                                | No change needed.                              |
| Useful type hints and meaningful docstrings                     | domain.py, data_store.py, services.py           | Type hints are present. Some old Stage 6 TODO comments remain.                              | Minor documentation issue accepted for review. |
| Four-space indentation and imports/layout                       | Reviewed Python files                           | Indentation is consistent. One unused import was identified.                                | No functional change needed.                   |
| Focused methods / duplication / dead or commented code          | Reviewed Python files                           | Methods are generally short. Some outdated comments remain.                                 | No functional change needed.                   |
| Globals / leakage / unnecessary inheritance or frameworks       | Reviewed Python files                           | No unnecessary frameworks or inheritance identified.                                        | No change needed.                              |
| No SQLite/persistence/repository ABCs/speculative features      | data_store.py                                   | Uses in-memory dictionaries without database persistence.                                   | No change needed.                              |
| Synthetic data / secrets / dependencies / provenance            | Project files                                   | Final secrets and dependency review pending.                                                | Complete before release.                       |
| Significant common Copilot contributions and human verification | Previous stage records                          | Previous Copilot evidence requires final review.                                            | Review actual AI evidence before release.      |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST           | Not applicable                                  | Undergraduate group only.                                                                   | Not applicable.                                |

| AI claim                          | Affected requirement/code | Human check                       | Accept/Modify/Reject and reason | Actual outcome/action or no change                  |
|-----------------------------------|---------------------------|-----------------------------------|---------------------------------|-----------------------------------------------------|
| Previous Copilot-assisted changes | Earlier applicable stages | Review existing records and tests | Pending final review            | No new AI-generated changes during Stage 12 so far. |

Access route or approved equivalent / limitations: GitHub Copilot is the permitted coding assistant. Previous AI evidence will be reviewed using the available stage records.
Available AI evidence and missing evidence honestly disclosed: Earlier stage documentation is available. Final confirmation of AI prompts, suggestions and human verification is pending.

## F README and reproducibility check

| README item                                                   | Location                                           | Verifier        | Result/gap                                                                                        |
|---------------------------------------------------------------|----------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------|
| Purpose and included common/PG scope                          | Root README.md and project/README.md               | Mohammed Aboset | SmartCare purpose and undergraduate scope documented. PG-only stages are not part of our release. |
| Out-of-scope capabilities and known limitations               | project/README.md                                  | Mohammed Aboset | In-memory data storage and current limitations documented.                                        |
| Confirmed teaching Python version and dependency installation | project/README.md and project/requirements-dev.txt | Mohammed Aboset | Python 3.14.7 used locally. pytest 8.3.5 installed successfully from requirements-dev.txt.        |
| Working directory / demo / interactive / test commands        | project/README.md                                  | Mohammed Aboset | Commands documented. Interactive menu tested locally and all 39 automated tests passed.           |
| Repository structure and architecture responsibilities        | project/README.md                                  | Mohammed Aboset | Project structure and main components documented.                                                 |
| Responsible AI summary / synthetic-data rule                  | project/README.md                                  | Mohammed Aboset | Responsible AI guidance and synthetic-data rule documented.                                       |
| Release label/version and SHA links                           | Root README.md and project/README.md               | Mohammed Aboset | SmartCare v1.0 release candidate documented. Starting SHA recorded. Final release SHA pending.    |
Root README index and project/README verified: Both README files were updated for Stage 12. Git whitespace check passed.
Fresh clone or extracted ZIP / candidate identity: Pending independent verification by Fahad Almajeed using the final release candidate.
Verifier and clean environment / actual version: Mohammed Aboset completed local verification using Python 3.14.7 and pytest 8.3.5. Independent clean-environment verification is pending.
Setup/run/test commands and observed results: From project/, installed dependencies using python -m pip install -r requirements-dev.txt, ran python -m pytest -q with 39 tests passed in 0.03s, and successfully tested the interactive application using python main.py --interactive.
Missing local file or setup gap / remedy and recheck: No local dependency installation or automated testing errors observed. Independent fresh-clone verification remains pending.

## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [response]

2. What is feature freeze and why is it used? [response]

3. What is regression testing in a release context? [response]

4. What is a known limitation? [response]

5. What is technical debt? [response]

6. What are release notes? [response]

7. What is software maintenance? [response]

8. What is the purpose of the individual demonstration/viva? [response]

9. What should the final responsible-AI check establish before release? [response]

10. What is the main course conclusion about AI and the role of the software engineer? [response]


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
