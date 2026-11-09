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

| README item                                                   | Location                                           | Verifier                           | Result/gap                                                                                                                                                        |
|---------------------------------------------------------------|----------------------------------------------------|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose and included common/PG scope                          | Root README.md and project/README.md               | Mohammed Aboset and Fahad Almajeed | SmartCare purpose and undergraduate scope documented. PG-only stages are not part of our release.                                                                 |
| Out-of-scope capabilities and known limitations               | project/README.md                                  | Mohammed Aboset and Fahad Almajeed | Session-only storage and current limitations documented. No issues reported during independent verification.                                                      |
| Confirmed teaching Python version and dependency installation | project/README.md and project/requirements-dev.txt | Mohammed Aboset and Fahad Almajeed | Mohammed tested on macOS with Python 3.14.7. Fahad tested on Windows with Python 3.12.10. Both used pytest 8.3.5.                                                 |
| Working directory / demo / interactive / test commands        | project/README.md                                  | Mohammed Aboset and Fahad Almajeed | Mohammed: 39 tests passed in 0.03s. Fahad: 39 tests passed in 0.66s. Fahad also confirmed the original demo, interactive menu, and invalid-input recovery worked. |
| Repository structure and architecture responsibilities        | project/README.md                                  | Mohammed Aboset                    | Project structure and main components documented. No application defects reported by Fahad.                                                                       |
| Responsible AI summary / synthetic-data rule                  | project/README.md                                  | Mohammed Aboset                    | Responsible AI guidance and synthetic-data rule documented. Final release checks remain pending.                                                                  |
| Release label/version and SHA links                           | Root README.md and project/README.md               | Mohammed Aboset                    | SmartCare v1.0 release candidate documented. Fahad verified commit 34e713285bb56cfd5827279bb4ed40c1059ed6ce. Final submitted SHA pending.                         |
Root README index and project/README verified: Both README files were updated for Stage 12. Git whitespace check passed.
Fresh clone or extracted ZIP / candidate identity: Fahad Almajeed independently verified a fresh clone of commit 34e713285bb56cfd5827279bb4ed40c1059ed6ce from feature/stage12-release.
Verifier and clean environment / actual version: Mohammed Aboset tested locally on macOS using Python 3.14.7 and pytest 8.3.5. Fahad Almajeed independently tested on Windows using Python 3.12.10 and pytest 8.3.5.
Setup/run/test commands and observed results: Mohammed installed dependencies using python -m pip install -r requirements-dev.txt and ran python -m pytest -q from project/, with 39 passed in 0.03s. Fahad independently ran the full regression tests from a fresh clone, with 39 passed in 0.66s. He also confirmed the original demo and interactive menu worked, including registration, booking, conflict rejection, cancellation, retrieval, listing, and invalid-input recovery.
Missing local file or setup gap / remedy and recheck: No setup problems or application defects were reported during either member's verification. Final Pull Request approval, integration, and submission package checks remain pending.

## G Known limitations debt and release notes

Delivered features: SmartCare includes patient and practitioner management, appointment scheduling, patient search, appointment cancellation, and appointment queries through a console application.
Important fixes: Previous stages addressed patient search behaviour, appointment validation, and regression issues. The final release candidate passed all 39 automated tests.
Architecture/quality improvements: The application separates domain classes, data storage, services, and console interaction. Automated tests help verify the main features and expected errors.
Known limitations: SmartCare stores data in memory, so records are lost when the application closes. It is a teaching application and is not designed for real clinical use.
AI-assisted development note: GitHub Copilot was used during the permitted development activities. Human review and automated testing were used to check the application. AI assistance does not replace human verification.

| Debt item                           | Impact                                                       | Priority             | Future action                                             | Accepted? / release rationale                                              |
|-------------------------------------|--------------------------------------------------------------|----------------------|-----------------------------------------------------------|----------------------------------------------------------------------------|
| Session-only data storage           | Records disappear when the application closes.               | Low                  | Add permanent storage in a future version.                | Accepted because permanent storage is outside the required scope.          |
| No user authentication              | The application cannot securely manage real user accounts.   | High for production  | Add login and user roles before any real-world use.       | Accepted because SmartCare is a teaching application using synthetic data. |
| Local time without timezone support | Appointment times may be unclear across different timezones. | Medium               | Add timezone handling in a future version.                | Accepted because the current application uses local appointment times.     |
| Limited scalability and concurrency | The application is not designed for many simultaneous users. | Medium               | Add database storage and concurrency support.             | Accepted because the application is a small console-based project.         |
| Limited accessibility and usability | The console interface may not suit all users.                | Medium               | Improve accessibility and consider a graphical interface. | Accepted because a production interface is outside the assignment scope.   |
| No operational monitoring           | The application has no production monitoring system.         | Low for teaching use | Add logging and monitoring for future deployment.         | Accepted because production deployment is not required.                    |

Session-only synthetic data and minute-precision local time: SmartCare uses synthetic data stored only during the current session. Appointment times use local time with minute precision. Data is not saved after the application closes.
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: SmartCare does not include production authentication, user roles, a patient portal, notifications, billing, insurance processing, or clinical AI features. These are outside the undergraduate project scope.
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: SmartCare is designed for a small teaching demonstration. It does not support large-scale concurrent use, advanced timezone management, production monitoring, or a fully accessible graphical interface.
Difference between accepted scope limit and unresolved required behaviour: Accepted scope limits are features that were not required for this teaching application. Unresolved required behaviour means a required feature does not work correctly. No unresolved required behaviour was identified in the completed local tests, but independent release verification is still pending.
PG assurance residual risks / owner / status or not applicable: Not applicable. Both group members are undergraduate students, so postgraduate-only assurance requirements do not apply.

## H Release findings and corrective action

| Requirement/claim             | Reproduction/observation                                                                                      | Impact/severity                 | Owner/action                                  | Corrective diff                   | Focused/full recheck                                      | Residual limit                   |
|-------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------|-----------------------------------------------|-----------------------------------|-----------------------------------------------------------|----------------------------------|
| Full regression testing       | Ran python -m pytest -q from project/. All 39 tests passed in 0.03s using pytest 8.3.5.                       | No defect found                 | Mohammed Aboset / No correction required      | None                              | Full regression: 39 passed                                | Independent verification pending |
| Interactive application       | Ran python main.py --interactive and tested the available menu functions. The application worked as expected. | No defect found                 | Mohammed Aboset / No correction required      | None                              | Local interactive testing completed                       | Independent verification pending |
| README and setup instructions | Updated both README files and successfully installed dependencies from requirements-dev.txt.                  | Documentation updated           | Mohammed Aboset / Updated documentation       | README documentation changes only | Dependency installation succeeded and all 39 tests passed | Fresh-clone verification pending |
| Release formatting            | Ran git diff --check after correcting trailing whitespace. No further errors appeared.                        | Minor formatting issue resolved | Mohammed Aboset / Removed trailing whitespace | Root README formatting correction | git diff --check passed                                   | None identified                  |
Justified no-change conclusion if no defect found: No confirmed application defects were found during the completed local release checks. All 39 automated tests passed, and the interactive application worked as expected. Therefore, no application code changes were required. The README files and release documentation were updated to prepare the final release.
Release blockers still open / status: No confirmed application defects are currently blocking release. Independent fresh-clone verification, Pull Request review and approval, final SHA confirmation, and submission package checks are still pending. The release is not yet approved.

## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: Stage 12 Pull Request for feature/stage12-release in https://github.com/BigFa1/st1-assignment-3. Fahad independently reviewed and tested commit 34e713285bb56cfd5827279bb4ed40c1059ed6ce. Final Pull Request approval and integration are pending.
Independent reviewer / feedback / response: Fahad Almajeed (@BigFa1) completed independent fresh-clone verification on Windows using Python 3.12.10 and pytest 8.3.5. All 39 tests passed in 0.66s. The original demo and interactive menu worked correctly. He tested patient and practitioner registration, appointment booking, conflict rejection, cancellation, retrieval, listing, and invalid-input recovery. No issues were found. Mohammed recorded these results in Section F and Section I. Fahad will review the final documentation before approving the Pull Request.
Integration commit / full recheck: Stage 12 has not yet been merged into main. The release candidate passed all 39 automated tests using pytest 8.3.5. The final integration SHA and post-merge regression results will be recorded after approval and merging.
Tracked and untracked file inspection / cleanliness: Git status was checked before committing. Only the root README.md, project/README.md, and stage12/stage12_activities_and_evidence.md were modified. Git diff --check passed. Final working-tree cleanliness after all Stage 12 updates is pending.
Secrets/staff material/caches/tool-metadata exclusion check: No unexpected files appeared in the earlier git status output. A complete tracked-file and release ZIP inspection is still required to confirm that secrets, private staff material, virtual environments, caches, and unnecessary tool metadata are excluded.
Candidate recovery plan / known-good SHA: The Stage 12 starting commit is 26a6195ac76a66298b98a3e383fb0a6406f2b918. The first Stage 12 release candidate is 0c0e09d6237ea121826efed85fa454806d9c8c07. If a release problem is found, the group can return to a known-good commit, correct the issue on the release branch, and rerun the tests before merging.
Named substantive contributions: Mohammed Aboset completed Stage 12 local regression testing, interactive testing, README updates, release evidence documentation, and release candidate preparation. Fahad Almajeed contributed to earlier SmartCare development and is responsible for the pending independent release review and verification. Final Stage 12 contributions will be updated after the review.

## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: NOT YET READY. Both group members have successfully tested SmartCare, including Fahad's independent fresh-clone verification. Final Pull Request approval, integration, and submission checks are still pending.
Approver / date / rationale and evidence: Mohammed Aboset completed local verification with 39 tests passed. Fahad Almajeed completed independent verification on Windows with 39 tests passed in 0.66s and no issues found. Final approval by both members is pending.
What risks remain / conditions / owners: Fahad must review and approve the final Pull Request. Mohammed must complete the final SHA, release ZIP, and submission checks. Both members must confirm the final release decision.
Can the team explain the system: Mohammed has reviewed the main application components and tested the interactive functions. Both members must confirm they can explain the system during the final viva.
Can a change be recovered: Yes. Git records previous commits, including the Stage 12 starting SHA 26a6195ac76a66298b98a3e383fb0a6406f2b918. The group can return to a known-good version if necessary and repeat the tests.
Common decision / PG decision where different: The undergraduate release decision is NOT YET READY until the remaining checks are completed. Postgraduate-only requirements are not applicable because both members are undergraduate students.

## K Final tested release SHA

Exact common tested SHA: 34e713285bb56cfd5827279bb4ed40c1059ed6ce. Fahad independently verified this commit using a fresh clone on Windows with Python 3.12.10 and pytest 8.3.5. All 39 tests passed in 0.66s. The original demo and interactive menu also worked correctly, with no issues found. Mohammed's local regression testing also passed all 39 tests.
Exact PG tested SHA or not applicable: Not applicable. Both group members are undergraduate students.
Final submitted SHA / repository URL: Pending final review and merge. Repository: https://github.com/BigFa1/st1-assignment-3
Evidence-only later commit and difference explanation: Sections G–J were updated after the first release candidate commit. These are documentation changes only. A new commit SHA will be recorded after the remaining evidence is completed.
Executable changes after testing and re-verification: No executable code changes have been made during Stage 12 so far. All 39 automated tests passed. Final verification will be repeated before submission.
Source ZIP name / SHA correspondence / extracted comparison: Pending. The final source ZIP will be created from the exact submitted SHA after approval. Its contents will be checked against the final repository commit.

## L Submission package verification

- [x] Feature freeze and scoped requirements traced.
- [x] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [x] Root README and project/README reproduced by another verifier.
- [x] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: Pending confirmation from the University of Canberra submission instructions.
Deadline/timezone: Pending confirmation from the assessment instructions and Canvas.
Repository access arrangement: GitHub repository: https://github.com/BigFa1/st1-assignment-3. Stage 12 release branch: feature/stage12-release. Marker access has not yet been confirmed.
Mixed-candidate upload arrangement: Not applicable to our undergraduate-only group. Final submission route still requires confirmation.
Oral/video recording/accessibility arrangements: Pending confirmation of the team viva arrangements and any recording or accessibility requirements.
Remaining administration or release dependency: Fahad must complete independent verification and Pull Request review. Both members must approve the release. The final SHA, source ZIP, submission checklist, group reflection, individual peer forms, and viva preparation must also be completed.

## M Formative questions

1. What is a release candidate? A release candidate is a version of software that is almost ready for final release. It must pass the final checks before submission.

2. What is feature freeze and why is it used? Feature freeze means stopping the addition of new features. It allows the team to focus on testing and fixing problems before release.

3. What is regression testing in a release context? Regression testing checks that existing features still work after changes. In SmartCare, we ran 39 automated tests and all passed.

4. What is a known limitation? A known limitation is something the software cannot currently do. For example, SmartCare does not save data after the application closes.

5. What is technical debt? Technical debt is work that may need improvement in the future. For example, SmartCare could use permanent data storage instead of session-only storage.

6. What are release notes? Release notes explain what the software includes, what was fixed, and what limitations remain.

7. What is software maintenance? Software maintenance means fixing problems, improving features, and keeping software working after release.

8. What is the purpose of the individual demonstration/viva? The viva checks that each student understands the project and can explain their own contributions, code, testing, and decisions.

9. What should the final responsible-AI check establish before release? It should confirm that AI use followed the course rules, AI-assisted work was reviewed and tested by humans, and no private or sensitive information was included.

10. What is the main course conclusion about AI and the role of the software engineer? AI can help software engineers, but it cannot replace their responsibility. Engineers must understand, test, review, and take responsibility for their work.

## N Reflection viva and handover

Strongest evidence SmartCare is ready: All 39 automated tests passed using pytest 8.3.5. The interactive application was also tested successfully. The project includes separate domain, service, data storage, and testing components.
Weakest area: SmartCare only stores data during the current session. It also requires independent fresh-clone verification before the final release decision.
How AI use changed from Stage 1 to Stage 12: During the project, AI assistance was used where permitted to support development. By Stage 12, the focus was on human review, testing, checking evidence, and confirming that the application worked correctly.
Start doing — engineering and AI use: Start checking requirements and tests before accepting suggested changes. Record clear evidence for important decisions.
Stop doing — engineering and AI use: Stop assuming that code is correct simply because it runs or was suggested by AI. Avoid adding unnecessary features near release.
Continue doing — engineering and AI use: Continue using Git, automated testing, human reviews, and responsible AI practices.
What worked / caused rework / future delivery improvement: GitHub collaboration and automated testing helped the group manage changes. Earlier debugging and documentation updates required extra work. In future projects, we would review changes earlier and update documentation throughout development.
One paragraph — If AI can write code why do we still need software engineers: We still need software engineers because writing code is only one part of software development. Engineers must understand user requirements, design solutions, test software, fix problems, and make important decisions. AI can suggest code, but its suggestions may contain mistakes. Software engineers are responsible for checking that the application works correctly, meets requirements, and is safe to use. Human judgement and responsibility remain important even when AI is available.

| Preparation item                                                                  | Own explanation and evidence link                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Problem and stakeholders                                                          | SmartCare helps manage patients, practitioners, and appointments. The main stakeholders are patients, practitioners, and administrative staff. Evidence: project/README.md.                                                                                   |
| Two requirements and acceptance criteria                                          | Patient search should return the correct patient or report when a patient is not found. Appointment cancellation should update the appointment status and prevent invalid changes. Evidence: stage06/ and project/tests/.                                     |
| Domain model and architecture                                                     | SmartCare uses classes for patients, practitioners, and appointments. Domain classes manage rules, services coordinate operations, and the data store holds records. Evidence: project/smartcare/domain.py, services.py, and data_store.py.                   |
| Design trade-off                                                                  | We used in-memory storage because it is simple and suitable for a teaching project. The disadvantage is that records disappear when the program closes.                                                                                                       |
| Meaningful test and its limits / 100 percent coverage                             | Automated tests check patient search, appointment behaviour, and other application functions. All 39 tests passed. Passing tests does not prove that every possible situation has been tested or that code coverage is 100 percent. Evidence: project/tests/. |
| Diagnosed defect and verification                                                 | Stage 8 involved identifying and correcting faulty application behaviour. The final integrated application passed all 39 regression tests. Evidence: stage08/ and project/tests/.                                                                             |
| Shared store and session-state/query responsibilities                             | The shared data store holds patient, practitioner, and appointment records during the session. Services use the store, while queries retrieve information without changing stored records. Evidence: project/smartcare/data_store.py and services.py.         |
| What would break if session-state lookup/query responsibilities changed?          | Patient searches and appointment queries might return incorrect or inconsistent information. Existing tests could fail because services would no longer use the expected shared records.                                                                      |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | Cancellation changes the state of an appointment, so its rules belong in the domain model. Services coordinate appointments and check conflicts between records.                                                                                              |
| FR-07 retained history test                                                       | The retained history test checks that appointment history remains available as required during the session. Evidence: project/tests/. The exact test should be identified during viva preparation.                                                            |
| Actual AI change rejected/modified or honestly accepted with verification         | A specific GitHub Copilot suggestion and the group's decision must be confirmed from the earlier stage evidence before the viva. No unverified example is claimed here.                                                                                       |
| Unresolved limitation / future production work                                    | Future improvements would include permanent storage, authentication, user roles, timezone handling, and production monitoring.                                                                                                                                |
| Personal implementation contribution                                              | Mohammed Aboset contributed to SmartCare development and group activities during earlier stages. Exact implementation evidence should be confirmed using the relevant Git commits and stage records.                                                          |
| Personal test/review/design/integration contribution                              | Mohammed completed Stage 12 local regression testing, interactive testing, README updates, release documentation, and release candidate preparation. Evidence: stage12/ and commit 0c0e09d6237ea121826efed85fa454806d9c8c07.                                  |
| PG agentic change and rescheduling verification                                   | Not applicable. Both group members are undergraduate students.                                                                                                                                                                                                |
| PG responsible-AI risk/remediation or supported no finding                        | Not applicable. Both group members are undergraduate students.                                                                                                                                                                                                |

Optional bounded-change practice only: No additional coding practice has been undertaken during Stage 12. The release candidate will be preserved for final verification.
Practice question/change and reasoning: Not undertaken. The focus is on final verification and release preparation rather than adding new code.
Separate reflection / peer / common team viva evidence links and routing: The group reflection, confidential individual peer forms, and common team viva are separate assessment requirements. Their final submission links and arrangements are pending confirmation from the assessment instructions.
No further coding stage. Later corrections use the published assessment process.