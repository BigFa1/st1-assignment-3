# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Monday 9:30–11:30, Group 4.
Members and UG/PG cohorts: Member 1 — Fahad Almajeed (BigFa1, UG, repository owner). Member 2 — Mohammed Aboset (MohammedAboset, UG, group member).
Record owner / contribution links for each member: Mohammed Aboset — Stage 8 debugging, regression tests, repairs, refactoring and evidence documentation on branch debug/stage08. Fahad Almajeed — Repository owner; Stage 8 review and integration contributions to be recorded in Section I after completion.


Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.


Response and reason:

1. "Appointment disappears after cancellation."
   Classification: Symptom.
   Reason: This describes the visible problem, but does not explain what caused it.
2. "The data-store removal path is probably being called."
   Classification: Hypothesis/opinion.
   Reason: This suggests a possible cause without evidence. The current SmartCare project has no public delete operation, so this hypothesis must be checked rather than assumed.
3. "The failing test shows store.find_appointment('A1') returns None."
   Classification: Evidence.
   Reason: This describes an observed test result that can be checked and reproduced.
4. "The service layer is badly designed."
   Classification: Hypothesis/opinion.
   Reason: This is a judgement without specific supporting evidence and does not identify the actual defect.
5. "Traceback points to smartcare/services.py line 42 in the example."
   Classification: Evidence.
   Reason: A traceback identifies where an error was reported. However, line 42 is only an illustrative example and does not prove the root cause.


### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.


Response and reason:
Scenario: F8-02 — Cancelled appointment history cannot be retrieved.
Expected behaviour: According to FR-07, cancelling an appointment must retain its record so it can still be found later.
Observed behaviour: After cancelling appointment A1, the data-store lookup returned None, and the service lookup raised LookupError instead of returning the cancelled appointment.
Minimal reproduction:
1. Register patient P1 and practitioner DR1.
2. Book appointment A1.
3. Cancel appointment A1.
4. Call store.find_appointment("A1") and appointments.find_appointment("A1").
5. Observe that the cancelled appointment cannot be retrieved.
Initial hypothesis: The appointment lookup method may be incorrectly filtering out cancelled appointments.
Evidence to inspect: The failing regression test, its traceback, the find_appointment() method in smartcare/data_store.py, the appointment status after cancellation, and the FR-07 requirement.
Conclusion: The hypothesis was supported. The faulty data-store lookup excluded cancelled appointments. Restoring the normal lookup allowed cancelled appointments to remain retrievable, and the regression test passed.

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason:
1. Cancelled appointments:
   This is a test defect. FR-07 requires cancelled appointments to be retained for history. Therefore, a test expecting cancelled appointments to be deleted is incorrect. The test should be changed to check that cancelled appointments remain stored and retrievable. The correct product behaviour should not be changed to satisfy an incorrect test.
2. Different practitioners at the same time:
   This is also a test defect. According to AC-04.2, the booking conflict rule applies when the same practitioner has another scheduled appointment at the same time. Different practitioners can have appointments at the same time. Therefore, the test should be corrected to allow this situation.
Conclusion: A failing test does not always mean the product code is wrong. Tests must be checked against the requirements before changing the implementation.

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.


Response and reason:
Part 1 — Code smells and proposed refactorings:
1. Long method: A 70-line method is difficult to read and maintain. Extract smaller helper methods for separate tasks.
2. Duplicate status strings: Repeated strings can cause mistakes. Replace them with the existing AppointmentStatus enum.
3. Direct collection manipulation: The service should use SmartCareDataStore methods instead of accessing stored collections directly. This keeps storage responsibilities inside the data-store layer.
4. Printing inside the service: Printing mixes business logic with user interface responsibilities. Keep output handling outside the service.
5. Mixed responsibilities: Validation, booking and status checks are combined in one method. Extract small helper methods to make the code easier to understand.
6. Four nested conditionals: Deep nesting makes the logic difficult to follow. Use simple guard clauses where appropriate.
Part 2 — Classification of proposed changes:
1. Rename appt to appointment:
   Classification: Refactoring.
   Reason: Improves readability without changing behaviour.
2. Extract a repeated conflict helper:
   Classification: Refactoring.
   Reason: Removes repeated logic while preserving the same booking conflict rules.
3. Add rescheduling:
   Classification: Feature.
   Reason: Introduces new functionality that was not previously available.
4. Restore retained cancellation lookup:
   Classification: Repair.
   Reason: Fixes a defect so cancelled appointments remain retrievable as required by FR-07.
5. Replace a magic status string with the existing enum:
   Classification: Refactoring.
   Reason: Improves code clarity and consistency without changing the meaning of the status.
Behaviour to preserve: Successful bookings, participant validation, duplicate appointment rejection, same-practitioner scheduling conflicts, cancellation behaviour and retained appointment history must remain unchanged. Existing tests and regression tests should pass after any refactoring.
Conclusion: Refactoring improves code structure without intentionally changing external behaviour. Repairs correct defects, while features introduce new functionality.


### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason:
Actual failure: F8-02 — Cancelled appointment lookup.
Exception/assertion: The failing regression test expected the cancelled appointment A1 to remain retrievable, but the lookup returned None. The service lookup also raised LookupError when the cancelled appointment was requested.
Expected value: The original Appointment object A1, with status CANCELLED.
Observed value: None from the data-store lookup, causing LookupError when accessed through the service.
Test location: tests/test_regressions.py, in test_f8_02_cancelled_appointment_still_retrievable(), at the assertion checking store.find_appointment("A1") is original.
Application call path: The test creates an appointment through AppointmentService.book_appointment(), cancels it through AppointmentService.cancel_appointment(), and checks retrieval through SmartCareDataStore.find_appointment(). The service lookup also calls the same data-store method.
Supporting requirement: FR-07 requires cancelled appointments to remain stored and retrievable for history.
Ranked hypotheses:
1. Most likely — The data-store lookup incorrectly filters out cancelled appointments.
   Check: Inspect find_appointment() in smartcare/data_store.py and check whether it excludes appointments with status CANCELLED.
2. Less likely — Cancellation removes the appointment from storage.
   Check: Inspect the cancellation method and the stored appointments after cancellation. The project has no public delete operation.
3. Least likely — The test uses an incorrect appointment ID.
   Check: Compare the ID used during booking, cancellation and lookup to confirm they all use A1.
Conclusion: The first hypothesis was supported by the code inspection and regression test. The faulty lookup excluded cancelled appointments. After repairing the lookup, the regression test passed.
A traceback identifies where a failure was detected, but it does not always identify the root cause. The developer must inspect the code, test hypotheses and compare the behaviour with the requirements before making changes.


### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?


Response and reason:
Changing code immediately after seeing a failure is a poor debugging strategy because the actual cause may not be known. The failure could come from incorrect code, an incorrect test or a misunderstanding of the requirements.
A better approach is to reproduce the failure, inspect the traceback, compare the expected and observed behaviour, and test possible causes before making a small repair.
This reduces unnecessary changes and helps prevent new defects.

Classification responses (1–5, each with reason): Completed in A.1. The five statements were classified as symptom, hypothesis/opinion, evidence, hypothesis/opinion and evidence, respectively. Each classification includes a reason.
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: Completed in A.2 using F8-02. FR-07 requires cancelled appointments to remain retrievable. The faulty lookup returned None for cancelled appointments. The record includes reproduction steps, the initial lookup-filtering hypothesis and evidence to inspect.
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: Completed in A.5 using F8-02. The record identifies the failed assertion, expected original appointment, observed None, regression test function, application call path and FR-07. Three possible causes were ranked, with a separate check for each.


## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: cb23711 (Stage 7 integrated into main through PR #9). Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2. Existing SmartCare project and earlier tests preserved.
- Baseline test command / working directory / observed result / evidence: Ran `python -m pytest` from `project/` at Stage 7 commit `c8d9e3a`. Result: 28 tests passed, 0 failed, in 0.02 seconds. Evidence: `stage07/stage07_activities_and_evidence.md`, Section G (test execution record) and completion summary. Stage 7 was subsequently merged into `main` at `cb23711`.
- Clean preparation SHA if a record-only commit followed Stage 7: Not applicable. No separate record-only commit was identified between the Stage 7 integration commit `cb23711` and the Stage 8 preparation commit `058e614`.
- Branch and preparer / how teammates obtained this branch: Stage 8 was prepared on branch `debug/stage08`. The preparation commit `058e614` was authored by Mohammed Aboset on 5 November 2026 at 14:54 +1100. The branch is available on `origin/debug/stage08`. Teammate branch retrieval has not yet been verified.
- Downloaded tool version, source SHA256 and --check outcome: The local preparation record confirms tool version 1.1. The original utility file was not found in the searched directories, so its source SHA256 and the exact `--check` outcome could not be independently verified.
- --apply and --verify output summaries / artefact references: The local `project/.stage8_faults/record.json` reports tool version 1.1 and status `prepared`. Git commit `058e614` contains the two intended changes in `project/smartcare/data_store.py`. The prepared test run produced 24 passed and 4 failed. The original `--apply` and `--verify` terminal outputs were not available, so their exact results could not be independently verified.
- Bounded diff inspected and recovery location (not committed): Compared `cb23711` with `058e614` using `git --no-pager diff cb23711 058e614 -- smartcare/data_store.py`. Only `project/smartcare/data_store.py` changed, limited to `find_appointment()` and `has_practitioner_conflict()` (11 insertions, 18 deletions). Local recovery files are in `project/.stage8_faults/`: `data_store.before.py` and `record.json`. The metadata records tool version 1.1, baseline SHA256 `b4a1993e878c59a9df5e9055320702b2d318c5b6055bb1693a3afc25cd8fd375`, faulty SHA256 `6b57a2d7f69df15373aa954c6d5e7a9758dcdd2c7e187b25304eacf5e52d09ce`, and status `prepared`.
- Prepared faulty-state commit SHA: 058e61401f57b3286558058ff3059b0438bd5509 (debug/stage08).
- Preparation or recovery issues and resolution, if any: No preparation errors have been identified in the available evidence. The recovery folder was located at `project/.stage8_faults/` and contains `data_store.before.py` and `record.json`. Both files were confirmed excluded from Git using `git check-ignore -v`. The preparation record reports status `prepared`.
- Initial prepared full-suite command / result / key failures: Ran `python -m pytest -q` from `project/` on branch `debug/stage08`, commit `058e61401f57b3286558058ff3059b0438bd5509`. Result: 24 passed, 4 failed (28 tests total). Two failures involved cancelled appointment lookup raising `LookupError`, and two involved same-practitioner booking conflicts not raising `ValueError`. The working tree was clean after the run.

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: The system allowed a second appointment for the same practitioner at the same date and time instead of rejecting it. The tests `test_practitioner_booking_conflict_preserves_original` and `test_conflict_rule_and_different_practitioner` failed because the expected `ValueError` was not raised.
- Expected behaviour: The system must reject a second scheduled appointment for the same practitioner at the same date and time by raising a ValueError. Appointments for different practitioners at the same time must still be allowed.
- Minimal synthetic reproduction steps: Create a practitioner and a patient, then schedule an appointment for that practitioner at a specific date and time. Attempt to schedule a second appointment for the same practitioner at the same date and time. The system should reject the second booking with a ValueError, but the prepared faulty version allows it.
- Meaningful failing test path/name and exact relevant failure: Created `project/tests/test_regressions.py` with `test_f8_01_same_practitioner_double_booking`. Ran `python -m pytest tests/test_regressions.py::test_f8_01_same_practitioner_double_booking -v` from `project/`. Result: 1 failed in 0.03 seconds. The failure occurred at line 20 with `Failed: DID NOT RAISE ValueError`. This confirms that the faulty implementation does not reject a second appointment for the same practitioner at the same time. The existing tests `test_practitioner_booking_conflict_preserves_original` and `test_conflict_rule_and_different_practitioner` also demonstrated this defect.
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: The root cause is an incorrect practitioner ID comparison in `project/smartcare/data_store.py`, inside `has_practitioner_conflict()`. The Git diff between `cb23711` and `058e614` shows that `== practitioner_id` was changed to `!= practitioner_id`. This makes the method check different practitioners instead of the same practitioner. The regression test `test_f8_01_same_practitioner_double_booking` confirmed the defect by failing with `Failed: DID NOT RAISE ValueError`.
- Smallest justified fix / diff / why other behaviour is preserved: Changed the practitioner ID comparison in `has_practitioner_conflict()` from `!= practitioner_id` to `== practitioner_id`. This ensures that appointments for the same practitioner at the same date and time are detected as conflicts. No other conditions in this method were changed.
- Repair SHA / focused verification result: Commit `6737a6f`. Ran `python -m pytest tests/test_regressions.py::test_f8_01_same_practitioner_double_booking -v` from `project/`. Result: 1 passed in 0.01 seconds.

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: After an appointment is cancelled, the system cannot retrieve it by its ID. The regression test confirmed that `store.find_appointment("A1")` returns `None` instead of the original appointment object.
- Expected behaviour: Cancelling an appointment must change its status to CANCELLED without deleting it from storage. The appointment must remain retrievable by its ID, and the lookup must return the same original appointment object.
- Minimal synthetic reproduction steps: Create a patient and practitioner, then book appointment A1. Cancel appointment A1 and attempt to retrieve it using store.find_appointment("A1"). The expected result is the original cancelled appointment, but the faulty version returns None.
- Meaningful failing test path/name and exact relevant failure: Created `project/tests/test_regressions.py` with `test_f8_02_cancelled_appointment_still_retrievable`. Ran `python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_still_retrievable -v` from `project/`. Result: 1 failed in 0.03 seconds. The failure occurred at line 38 with `AssertionError: assert None is original`. The data store returned None instead of the original cancelled appointment. This confirms that cancelled appointments cannot be retrieved correctly in the prepared faulty version.
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: The root cause is an incorrect status condition in `project/smartcare/data_store.py`, inside `find_appointment()`. The Git diff between `cb23711` and `058e614` shows that the original dictionary lookup was replaced with a loop containing `appointment.status.value != "cancelled"`. This incorrectly excludes cancelled appointments from lookup. The regression test `test_f8_02_cancelled_appointment_still_retrievable` confirmed the defect because `store.find_appointment("A1")` returned None instead of the original cancelled appointment.
- Smallest justified fix / diff / why other behaviour is preserved: Restored the original dictionary lookup in `find_appointment()` using `self._appointments.get(required_text(appointment_id, 'Appointment ID'))`. This removes the incorrect condition that excluded cancelled appointments. The method still validates appointment IDs and returns None for an unknown valid ID.
- Repair SHA / focused verification result: Commit `6737a6f`. Ran `python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_still_retrievable -v` from `project/`. Result: 1 passed in 0.01 seconds.

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: The has_practitioner_conflict() method may be comparing practitioner IDs incorrectly. This is plausible because the existing tests show that the system allows two appointments for the same practitioner at the same date and time instead of raising ValueError.
Evidence intended to inspect / competing explanation / discriminating check: Inspect the has_practitioner_conflict() method in project/smartcare/data_store.py and review the failing tests. Another possible cause is that the appointment date and time are compared incorrectly. Check whether the practitioner ID or date/time comparison explains the failure.
Member and saved sequence/time or commit showing this preceded consultation: Mohammed Aboset. Human-first hypotheses and intended checks were recorded before GitHub Copilot consultation in commit `1cf05ca` on branch `debug/stage08`.

### F8-02 human entry
Likely cause and why plausible: The find_appointment() method may be incorrectly excluding cancelled appointments when searching by appointment ID. This is plausible because the failing tests show that the system raises LookupError when attempting to retrieve an appointment after cancellation.
Evidence intended to inspect / competing explanation / discriminating check: Inspect the find_appointment() method in project/smartcare/data_store.py and review the failing cancellation tests. Another possible cause is that the cancellation process deletes the appointment from storage. Check whether the appointment remains stored but is excluded by the lookup method, or whether it is actually removed during cancellation.
Member and saved sequence/time or commit showing this preceded consultation: Mohammed Aboset. Human-first hypotheses and intended checks were recorded before GitHub Copilot consultation in commit `1cf05ca` on branch `debug/stage08`.

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: Mohammed Aboset used GitHub Copilot Chat after recording the human-first hypotheses in commit `1cf05ca`. The actual prompt asked Copilot to examine `has_practitioner_conflict()` in `smartcare/data_store.py`, investigate the failing test `test_f8_01_same_practitioner_double_booking` (`DID NOT RAISE ValueError`), provide three ranked possible causes with evidence checks, and avoid modifying code. Copilot returned three ranked suggestions: a reversed practitioner ID comparison, an incorrect booking-service call, and an appointment time/status mismatch. The response was reviewed during this debugging session.
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot suggested that the practitioner ID comparison is reversed (`!=` instead of `==`). Its suggested check was to call `has_practitioner_conflict()` with the same practitioner ID and time. The inspected Git diff between `cb23711` and `058e614` confirms the reversed comparison. The regression test also failed with `DID NOT RAISE ValueError`. Evaluation: Correct. Decision: Accept because the diagnosis matches the code, failing test and booking-conflict requirement. The direct method call was not separately performed.
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot suggested that the booking service might not call `has_practitioner_conflict()` correctly. Its suggested check was to trace the booking process and inspect the arguments passed to the method. Copilot reported that `AppointmentService.book_appointment()` calls the helper with the practitioner's ID and requested time. The Git diff also identifies the reversed comparison inside the helper. Evaluation: Unlikely based on the available evidence. Decision: Reject as the supported root cause because the reversed comparison already explains the observed failure. A separate runtime trace of the service call was not performed.
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot suggested that the existing appointment might not match the required date, time or scheduled status. Its suggested check was to inspect the stored appointment before attempting the second booking. The regression test creates a scheduled appointment and attempts a second booking using the same `booking_time` variable. The inspected code shows the incorrect practitioner comparison. Evaluation: Unlikely for this reproduction. Decision: Reject as the supported root cause because the test uses the same date and time and the reversed comparison explains the failure. A separate runtime inspection of the stored appointment was not performed.
Final human conclusion and comparison with initial hypothesis: Copilot's first suggestion agrees with the human-first hypothesis recorded in commit `1cf05ca`. The inspected Git diff and failing regression test support the conclusion that `has_practitioner_conflict()` incorrectly uses `!=` instead of `==` when comparing practitioner IDs. The second and third suggestions are not supported as the root cause by the available evidence. The human decision is to accept the first diagnosis and make the smallest necessary correction after completing the Copilot review. The application repair had not been performed at the time of this Copilot consultation. The defect was subsequently repaired in commit 6737a6f.

### F8-02 Copilot review
Actual prompt / output reference and member: Mohammed Aboset used GitHub Copilot Chat after recording the human-first hypotheses in commit 1cf05ca. The prompt described the observed behaviour, expected behaviour, reproduction steps, failing regression test, human-first hypothesis and relevant code. It requested three ranked possible causes with evidence checks and instructed Copilot not to modify files, rewrite the application or invent requirements. Copilot returned three suggestions but inspected the Stage 7 main branch at cb23711 rather than the faulty Stage 8 branch at 058e614. Its response was therefore evaluated against the actual Stage 8 Git diff and failing regression test.
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot suggested that the test might be running against a different or stale project version. Its proposed check was to verify the checkout, commit and imported package. Copilot inspected main at cb23711, where find_appointment() correctly retrieves appointments from the dictionary. However, our regression test was run on the prepared Stage 8 branch, where the Git diff confirms a faulty status filter. Evaluation: Partly correct because Copilot identified a version difference, but it inspected the wrong branch and did not identify the actual defect. Decision: Reject as the root cause of the observed Stage 8 failure.
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot suggested that booking, cancellation and lookup might use different data-store instances. Its proposed check was to inspect the test setup and confirm that the operations share one store. Our regression test creates one SmartCareDataStore instance, passes it to AppointmentService, and uses the same store for the final lookup. Evaluation: Wrong for this reproduction. Decision: Reject because the test uses the same data store throughout.
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot suggested that another part of the application might remove the appointment during cancellation. Its proposed check was to inspect the cancellation process for deletion or replacement operations. The Stage 8 Git diff shows that find_appointment() excludes appointments whose status is "cancelled". This explains why lookup returns None without requiring the appointment to be deleted. Evaluation: Not supported as the root cause by the inspected evidence. Decision: Reject because the faulty lookup condition already explains the observed failure.
Final human conclusion and comparison with initial hypothesis: Copilot's three suggestions did not identify the actual F8-02 defect because it inspected the Stage 7 main branch instead of the prepared Stage 8 branch. The human-first hypothesis recorded in commit 1cf05ca was supported by the Git diff between cb23711 and 058e614. The faulty find_appointment() method contains appointment.status.value != "cancelled", which incorrectly excludes cancelled appointments from lookup. The regression test confirmed this by failing with AssertionError: assert None is original. The human decision is to reject Copilot's three suggestions as explanations of the observed Stage 8 failure and accept the evidence-supported diagnosis. The application repair had not been performed at the time of this Copilot consultation. The defect was subsequently repaired in commit 6737a6f.

## G. Failing to passing regression evidence

| Checkpoint                                     | Code SHA or precise diff                                                                                        | Command and working directory                                                                                        | Actual result and artefact reference                                                                    |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| F8-01 before repair                            | Prepared faulty commit `058e614`; human-first evidence commit `1cf05ca`. No application repair performed.       | `python -m pytest tests/test_regressions.py::test_f8_01_same_practitioner_double_booking -v` from `project/`.        | FAILED: `Failed: DID NOT RAISE ValueError` at `tests/test_regressions.py:20`. 1 failed in 0.03s.        |
| F8-01 after repair                             | Repair commit `6737a6f`. Changed practitioner ID comparison in `has_practitioner_conflict()` from `!=` to `==`. | `python -m pytest tests/test_regressions.py::test_f8_01_same_practitioner_double_booking -v` from `project/`.        | PASSED: 1 passed in 0.01s. Same-practitioner double booking is rejected.                                |
| F8-02 before repair                            | Prepared faulty commit `058e614`; human-first evidence commit `1cf05ca`. No application repair performed.       | `python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_still_retrievable -v` from `project/`. | FAILED: `AssertionError: assert None is original` at `tests/test_regressions.py:38`. 1 failed in 0.03s. |
| F8-02 after repair                             | Repair commit `6737a6f`. Restored the original dictionary lookup in `find_appointment()`.                       | `python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_still_retrievable -v` from `project/`. | PASSED: 1 passed in 0.01s. Cancelled appointment remains retrievable as the original object.            |
| Full suite after both repairs, before refactor | Both repairs applied, subsequently committed as `6737a6f`. No refactoring performed yet.                        | `python -m pytest -v` from `project/`.                                                                               | PASSED: 30 passed, 0 failed in 0.02s. All 28 existing tests and both new regression tests passed.       |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: The F8-01 regression test uses `pytest.raises(ValueError)` to check that a second booking for the same practitioner at the same time is rejected. Before the repair, the test failed because no ValueError was raised, but after the repair, it passed. The F8-02 regression test checks that a cancelled appointment remains retrievable by its ID as the original object. Before the repair, the test failed because `find_appointment()` returned None, but after the repair, it passed. Both tests help prevent these defects from happening again.
Unrelated failures investigated / resolution: The initial full-suite run produced 4 failures, all related to F8-01 or F8-02. The two new regression tests also failed before the repairs, as expected. After both repairs, the full test suite was run using `python -m pytest -v`, and all 30 tests passed in 0.02 seconds with no remaining failures. No unrelated failures were observed. After refactoring, the full suite was run again using `python -m pytest -v` from `project/`. All 30 tests passed in 0.02 seconds, confirming that the existing tests and both regression tests still pass.


## H. Refactoring decision and before/after verification

Smell and exact location: The `book_appointment()` method in `project/smartcare/services.py`, inside `AppointmentService`, contains participant lookup and validation logic mixed with appointment creation and booking checks. This makes the method longer and gives it several responsibilities.
Small proposed structural change / why justified: Extract the patient and practitioner lookup and missing-participant checks into a private helper method named `_get_booking_participants()`. The `book_appointment()` method will call this helper before creating the appointment. This improves readability and separates participant validation from booking logic without changing the required behaviour.
External behaviour to preserve / relevant tests: The refactor must preserve patient and practitioner lookup, `LookupError` for missing participants, `ValueError` for invalid IDs, duplicate appointment IDs and practitioner conflicts, successful appointment creation, and the original stored objects. The existing tests in `tests/test_services.py` and `tests/test_starter.py`, together with the two regression tests in `tests/test_regressions.py`, will be used to check behaviour preservation.
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: Added the private helper method `_get_booking_participants()` to `AppointmentService` in `project/smartcare/services.py`. Replaced the repeated patient and practitioner lookup and validation code in `book_appointment()` with a call to the helper. Reviewed the changes using `git --no-pager diff -- smartcare/services.py`. The refactoring was committed separately as `2d85ff2` (`Refactor appointment booking participant lookup`).
Focused and full after-refactor commands / working directory / results / evidence: From the project/ directory, ran python -m pytest tests/test_regressions.py -v. Both Stage 8 regression tests passed in 0.01 seconds. Also ran python -m pytest -v from project/. All 30 tests passed in 0.02 seconds, including both regression tests and the 28 existing tests. The terminal outputs and Git diff provide verification evidence.
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: Accepted. The refactoring separates participant lookup and validation from appointment booking, improving readability without intentionally changing external behaviour. All 30 tests passed after the change, supporting behaviour preservation.

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: GitHub Issue #10 covers F8-01 (same-practitioner double-booking), Issue #11 covers F8-02 (cancelled appointment lookup), and Issue #12 covers the appointment booking refactoring. All three issues were created and assigned to Mohammed Aboset (MohammedAboset).
Branch / prepared, repair and refactor checkpoints: Stage 8 work was completed on branch `debug/stage08`. Prepared faulty-state commit: `058e614`. Human-first hypotheses: `1cf05ca`. Failing regression evidence: `d9b8c2e`. Repair commit: `6737a6f`. Refactoring commit: `2d85ff2`. Final pre-merge documentation commit: `2ad15e4`. See Sections B, C, D and H.
PR link and another member's reviewer identity: Mohammed Aboset created Pull Request #13 to merge `debug/stage08` into `main`. Fahad Almajeed (BigFa1), the repository owner and other group member, reviewed the PR. Link: https://github.com/BigFa1/st1-assignment-3/pull/13
Key human feedback, difference from Copilot findings and response/outcome: Fahad reviewed both defect repairs, the regression tests and the refactoring. He independently ran the full test suite on the review branch and reported that all 30 tests passed. He confirmed that both defects were addressed and that the refactoring separated participant lookup from booking. He found no blocking issues. Unlike Copilot's F8-02 consultation, which inspected the wrong branch, Fahad reviewed the Stage 8 changes. His feedback supported accepting the repairs and refactoring without further code changes.
Actual review approval / merge evidence: Fahad (BigFa1) approved PR #13 and merged it into `main`. GitHub confirms that the pull request was successfully merged and closed. Merge commit: `362e9ba`.
Integrated code SHA and team pull/retest command / working directory / result: Integrated code SHA: `362e9ba`. Mohammed Aboset switched to `main`, pulled the latest changes using `git pull origin main`, and confirmed the merge commit using `git log -1 --oneline`. He then ran `python -m pytest -v` from `project/`. Result: 30 passed, 0 failed in 0.03 seconds. Fahad also reported independently running the full suite on the review branch, with all 30 tests passing.
Evidence-only later SHA / explanation if different: The integrated code SHA is `362e9ba`. Final evidence documentation will be committed separately on branch `docs/stage08-final-evidence`. The evidence-only commit SHA will be recorded once created.
Each member's substantive contribution and artefact: Mohammed Aboset (MohammedAboset) completed the debugging, human-first hypotheses, Copilot evaluation, regression tests, defect repairs, refactoring, GitHub Issues #10–#12, PR #13 and evidence documentation. Relevant commits include `1cf05ca`, `d9b8c2e`, `6737a6f` and `2d85ff2`. Fahad Almajeed (BigFa1) independently reviewed the changes, ran the full test suite, provided feedback, approved PR #13 and merged it into `main` at commit `362e9ba`.


## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence?
Response: During F8-02, Copilot suggested possible causes for the cancelled appointment lookup failure. However, its suggestions were not supported by the faulty code because it inspected the Stage 7 main branch instead of the Stage 8 debugging branch. This showed that Copilot suggestions must be checked against the correct code and actual test evidence.
2. What evidence changed your group's view?
Response: The failing regression tests and code inspection helped identify the actual causes of F8-01 and F8-02. The evidence showed that the practitioner conflict comparison was incorrect and that cancelled appointments were being excluded from lookup. After repairing both defects, all 30 tests passed. This supported the debugging conclusions.
3. How did regression tests protect the refactoring?
Response: The two regression tests checked that the same practitioner could not be double-booked and that cancelled appointments remained retrievable. Both tests passed before and after the refactoring. The full suite of 30 tests also passed after the change, providing evidence that the refactoring preserved the tested behaviour.


## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: An engineer should reproduce the failure, check the requirements, inspect the traceback and test results, and investigate possible causes before changing code.

2. Where should expected behaviour come from during debugging?

Response: Expected behaviour should come from the project requirements and acceptance criteria, not from assumptions or failing tests alone.

3. What is a debugging hypothesis?

Response: A debugging hypothesis is a possible explanation for a failure that must be checked against evidence.

4. What is a regression test and why is it retained?

Response: A regression test checks that a previously identified defect does not happen again. It is retained to detect the same problem if future code changes reintroduce it.

5. What is meant by root cause?

Response: The root cause is the underlying problem responsible for a failure. Fixing it prevents the same defect from continuing.

6. What is refactoring?

Response: Refactoring means improving the internal structure of code without intentionally changing its external behaviour.

7. What is a swallowed exception?

Response: A swallowed exception happens when a program catches an error but ignores it without handling or reporting it properly. This can hide defects and make debugging difficult.

8. What is a code smell?

Response: A code smell is a sign that code may be difficult to understand, maintain or improve. Examples include long methods, duplicated code and deeply nested conditions.

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: Copilot diagnoses should be treated as suggestions, not confirmed facts. Engineers must check them against the actual code, requirements and test evidence before accepting them.

10. What is the Stage 8 engineering rule?

Response: Diagnose the failure using evidence, write a regression test that fails before the repair, make the smallest justified fix, confirm the test passes, and refactor separately while preserving behaviour.

## L. Completion and handover

- [x] Existing project, earlier tests and stage records preserved.
- [x] Passing Stage 7 SHA and safe preparation details recorded.
- [x] Both defects reproduced with meaningful failing tests.
- [x] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [x] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [x] One genuine refactor verified under passing before/after tests.
- [x] Human PR review, feedback resolution and integrated retest recorded.
- [x] Tutorial, three reflections and ten formative responses complete.
- [x] Local recovery metadata excluded from submitted source.
- [x] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: `362e9ba`. Pull Request #13 was approved by Fahad Almajeed and merged into `main`. After pulling the integrated code, Mohammed Aboset ran `python -m pytest -v` from `project/`. Result: 30 passed, 0 failed in 0.03 seconds.
Submitted SHA and evidence-only difference if any: Integrated code SHA is `362e9ba`. Final documentation updates are being completed on branch `docs/stage08-final-evidence`. The final evidence-only commit SHA will be recorded after committing and merging this documentation.
Unresolved issues or incomplete checks / owner / next action: No outstanding code defects or failing tests were identified. Final documentation commit and integration remain to be completed by Mohammed Aboset and reviewed by Fahad Almajeed.
Handover note: Stage 8 debugging, repairs, regression tests, refactoring and human review are complete. Both defects have been repaired, and all 30 tests pass on the integrated `main` branch. The project is ready to continue to Stage 9 after the final evidence documentation is integrated.