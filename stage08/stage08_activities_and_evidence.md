# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [complete]
Members and UG/PG cohorts: [complete]
Record owner / contribution links for each member: [complete]

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

Response and reason: [complete]

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: [complete]

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason: [complete]

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason: [complete]

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason: [complete]

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: [complete]


Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

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
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: After an appointment is cancelled, the system cannot retrieve it by its ID. The regression test confirmed that `store.find_appointment("A1")` returns `None` instead of the original appointment object.
- Expected behaviour: Cancelling an appointment must change its status to CANCELLED without deleting it from storage. The appointment must remain retrievable by its ID, and the lookup must return the same original appointment object.
- Minimal synthetic reproduction steps: Create a patient and practitioner, then book appointment A1. Cancel appointment A1 and attempt to retrieve it using store.find_appointment("A1"). The expected result is the original cancelled appointment, but the faulty version returns None.
- Meaningful failing test path/name and exact relevant failure: Created `project/tests/test_regressions.py` with `test_f8_02_cancelled_appointment_still_retrievable`. Ran `python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_still_retrievable -v` from `project/`. Result: 1 failed in 0.03 seconds. The failure occurred at line 38 with `AssertionError: assert None is original`. The data store returned None instead of the original cancelled appointment. This confirms that cancelled appointments cannot be retrieved correctly in the prepared faulty version.
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

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
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint                                     | Code SHA or precise diff                                                                                  | Command and working directory                                                                                        | Actual result and artefact reference                                                                    |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| F8-01 before repair                            | Prepared faulty commit `058e614`; human-first evidence commit `1cf05ca`. No application repair performed. | `python -m pytest tests/test_regressions.py::test_f8_01_same_practitioner_double_booking -v` from `project/`.        | FAILED: `Failed: DID NOT RAISE ValueError` at `tests/test_regressions.py:20`. 1 failed in 0.03s.        |
| F8-01 after repair                             | [complete]                                                                                                | [complete]                                                                                                           | [complete]                                                                                              |
| F8-02 before repair                            | Prepared faulty commit `058e614`; human-first evidence commit `1cf05ca`. No application repair performed. | `python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_still_retrievable -v` from `project/`. | FAILED: `AssertionError: assert None is original` at `tests/test_regressions.py:38`. 1 failed in 0.03s. |
| F8-02 after repair                             | [complete]                                                                                                | [complete]                                                                                                           | [complete]                                                                                              |
| Full suite after both repairs, before refactor | [complete]                                                                                                | [complete]                                                                                                           | [complete]                                                                                              |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: The F8-01 regression test uses pytest.raises(ValueError) to check that a second booking for the same practitioner at the same time is rejected. The F8-02 regression test checks that a cancelled appointment remains retrievable by its ID and that the returned object is the original appointment. These tests protect the existing booking conflict and cancellation requirements from being broken by future changes.
Unrelated failures investigated / resolution: Not applicable at this stage. The initial full-suite run had 4 failures, all related to F8-01 or F8-02. The two new regression tests also failed for their expected defects. No unrelated failures have been observed so far. The full suite will be run again after both repairs to check for additional problems.

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [complete]

2. Where should expected behaviour come from during debugging?

Response: [complete]

3. What is a debugging hypothesis?

Response: [complete]

4. What is a regression test and why is it retained?

Response: [complete]

5. What is meant by root cause?

Response: [complete]

6. What is refactoring?

Response: [complete]

7. What is a swallowed exception?

Response: [complete]

8. What is a code smell?

Response: [complete]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [complete]

10. What is the Stage 8 engineering rule?

Response: [complete]

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
