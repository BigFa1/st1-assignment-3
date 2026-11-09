# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: Monday 9:30–11:30, Group 4.
Members and responsibilities: Fahad Almajeed (@BigFa1, UG) and Mohammed Aboset (@MohammedAboset, UG). Stage 9 responsibilities will be recorded as tasks are assigned and completed.
Stage 8 integrated SHA, command, working directory and actual result: 362e9ba222741ab893d0b7a7cb15305b50519168. Ran py -m pytest -q from project/. Result: 30 passed, 0 failed.

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity |Required session/domain state |Needed to register and find patients. |
| Appointment history |Required session/domain state |Cancelled appointments must remain available during the session. |
| Temporary menu choice |Transient state |Only needed for the current menu action. |
| Practitioner specialty |Required session/domain state |Stored as part of practitioner information. |
| Debug print output |Transient state |Used for debugging, not part of stored records. |
| Appointment status |Required session/domain state |Needed for cancellation and appointment filtering. |

What is intentionally lost on exit? All patient, practitioner and appointment records are lost when the program exits because the system only stores data in memory. Temporary menu choices and debug output are also not retained.

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| appointment_sort_key |appointment: Appointment |tuple (date_time, appointment_id) |Returns a sorting key without changing the appointment. |Uses Appointment.date_time and appointment_id. |
| select_appointments |appointments: list[Appointment], practitioner_id: str, status: AppointmentStatus or None |New list of Appointment objects |Filters by practitioner and optional status, then sorts by date/time and appointment ID. Does not change the original list. |Uses existing Appointment objects and AppointmentStatus enum. |
| Service listing |practitioner_id: str, status: AppointmentStatus or None |List of appointments or an error |Checks the practitioner exists, validates the status and calls select_appointments. |Uses SmartCareDataStore and existing validation rules. |
| Console |User menu choices and text input |Messages and displayed results |Reads input, converts date/time and status, calls services and handles expected errors. |Uses the existing services, date/time parser and appointment formatter. |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: Patients have an ID and name, and practitioners have an ID, name and specialty. Appointments have an ID, actual registered patient and practitioner objects, date/time and status. The system uses the existing domain classes and data store to manage these records. Services check valid participants and prevent booking conflicts. Queries only filter and sort existing appointments without changing their data.

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input |Domain object handles user input. |The console should ask the user for input. Appointment.cancel should only update the appointment status using domain rules. |
| Service prints/reads the menu |Service mixes business logic with user interaction. |The console handles menus and input. Services handle registration, booking, cancellation and validation. |
| Query sorts its source in place |The query changes the original collection. |Use sorted() to return a new list. Queries should not modify the original input. |
| Store prints Appointment saved |Data store handles display messages. |The store should save and return data. The console should display confirmation messages. |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check: appointments.sort(key=appointment_sort_key) changes the order of the original list and returns None. It does not create a new list.

result = sorted(appointments, key=appointment_sort_key) creates a new sorted list and leaves the original list unchanged. The result is a different list, but it contains references to the same Appointment objects.

To check for mutation, I would save the original appointment IDs in their original order before sorting. After calling sorted(), I would check that the original order is unchanged and that the result is a separate list. I would also check that the appointment fields have not changed.

Score-example prediction and explanation of passing the named key: The sorted result is [('Chen', 5), ('Ali', 8), ('Bea', 8)].

The function sorts by score first, then by name when the scores are equal. Chen comes first because the score is 5. Ali comes before Bea because both have a score of 8, and Ali comes first alphabetically.

The original scores list stays unchanged, and ordered is a new list.

We use key=score_key because Python needs to call the function for each item during sorting. Using key=score_key() would call the function immediately without an item and cause an error.

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion: Cancelling an appointment changes its status to CANCELLED, but the appointment is not deleted. This is required by FR-07 because the system must keep appointment history.

To check this, I would book an appointment, cancel it, and then search for it using the same appointment ID during the same session. The system should return the original appointment with status CANCELLED.

When listing all appointments for the practitioner without a status filter, the cancelled appointment should appear. However, when filtering by SCHEDULED only, the cancelled appointment should not appear.

This confirms that cancellation keeps the appointment history while allowing the appointment slot to be used again.

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: I will keep the existing SmartCare domain classes and data store without adding new fields or storage. The query functions will only filter and sort appointments using the inputs provided.

The service will check that the practitioner exists and that the status filter is valid before calling the query. The console will handle user input, display results and recover from expected errors.

Cancelled appointments must stay in the same session for history, and failed operations must not change stored records.

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| QRY-01 | Appointments, practitioner ID | Query filters by practitioner. | Only matching practitioner's appointments. | Test D1 and D2. |
| QRY-02 | Appointments, optional status | Query filters by AppointmentStatus. | All statuses by default, or matching status only. | Test scheduled, cancelled and completed. |
| QRY-03 | Appointment dates, times and IDs | Query sorts using appointment_sort_key. | Correct order without changing the original list. | Test date/time and ID tie-break. |
| QRY-04 | Practitioner ID and status | Service validates and calls query. | Empty list, LookupError or ValueError as appropriate. | Service listing tests. |
| FP-01 | Same inputs | Pure query with no hidden state. | Repeated calls give the same result. | Repeat query tests. |
| FP-02 | Empty, sorted and unsorted lists | Query returns a new list. | Original list and objects unchanged. | Identity and mutation tests. |
| FP-03 | Appointment object | Named sorting key. | Returns date_time and appointment_id. | Key and sorting tests. |
| UI-01 | Menu choices and records | Console calls services. | Complete workflow works in one session. | Interactive menu test. |
| UI-02 | Invalid input | Console handles expected errors. | Error message and menu continues. | Invalid-input tests. |
| FR-01–09 | Existing SmartCare records | Domain, store and services. | Existing rules remain working. | Previous and workflow tests. |
| FR-07 | Cancelled appointment | Cancellation and lookup. | History remains retrievable. | Cancel, find and list test. |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: A known practitioner with no matching appointments should return an empty list. An unknown practitioner ID should raise LookupError, while an invalid or blank ID should raise ValueError.

The console will convert valid status text into AppointmentStatus before calling the service. The service should reject an invalid status instead of returning an empty list.

Queries will return a new list containing the same Appointment objects, not copies. This means the original appointment identity is preserved.

The console will catch expected ValueError and LookupError cases, display a message and continue running. Failed bookings, duplicate IDs and invalid inputs must not change the existing records. I will check this in the workflow tests.

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| QRY-01 | smartcare/queries.py | test_practitioner_filter_and_order checks D1 and D2 separately. | Passed | project/tests/test_queries.py |
| QRY-02 | smartcare/queries.py | test_status_filters checks SCHEDULED, CANCELLED, COMPLETED and no matches. | Passed | project/tests/test_queries.py |
| QRY-03 | smartcare/queries.py | Checks date/time sorting and appointment ID tie-break. | Passed | project/tests/test_queries.py |
| FP-01, FP-02 | smartcare/queries.py | test_new_list_and_no_mutation checks repeated calls, new lists, unchanged order and fields. | Passed | project/tests/test_queries.py |
| FP-03 | smartcare/queries.py | Tests the named sorting key directly and checks its reuse. | Passed | project/tests/test_queries.py |
| QRY-04 | smartcare/services.py | Tests known-empty, unknown practitioner, blank ID and invalid status. | Passed | project/tests/test_queries.py |
| FR-07 | smartcare/services.py | Tests retained cancelled history, object identity and status listing. | Passed | project/tests/test_queries.py |
| Full regression suite | project/tests/ | Ran py -m pytest -q from project/. | 37 passed in 0.09s | Local pytest output; PR link pending |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: The query functions use the inputs provided and return results without changing the original list or Appointment objects. They do not use a global store, read user input or print anything. The select_appointments function uses sorted() to create a new list and the named sorting key to order appointments.
What the tests do and do not establish: The tests check practitioner filtering, status filtering, sorting, new list identity, unchanged source data and service validation. All 37 tests passed. However, passing tests do not guarantee that every possible case is correct. The interactive console and full workflow still need to be implemented and tested.

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | Register P1, D1 and D2. Book A1 with D1 at 2026-11-19 08:00. Attempt A3 at the same time. Book A2 with D2. Cancel A1, find and list it, then book A3 in the freed slot. | Registration, valid bookings, cancellation, retrieval and filtering work. Same-practitioner conflicts are rejected. | Manual workflow succeeded. A3 conflict was rejected, A2 was accepted, cancelled A1 remained retrievable, and A3 was later booked successfully. | project/smartcare/console.py; project/tests/test_workflows.py |
| UI-02 invalid-input recovery | Unknown menu choice, blank/unknown IDs, duplicate registration, invalid date/status, unknown appointment, repeated cancellation and unknown booking participant. | Errors are reported without crashing or changing records. The menu continues. | Manual tests succeeded as reported. The menu continued after errors, and A4 was successfully booked after rejected attempts. | project/smartcare/console.py; manual terminal verification |
| Automated service workflow | Run py -m pytest tests/test_workflows.py -q from project/. | Verify valid bookings, conflict rejection, cancellation history, filtering and unchanged state after failures. | 2 passed in 0.04s. The complete test suite also passed: 39 passed in 0.07s. | project/tests/test_workflows.py |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: Sections A2 and B of this Stage 9 evidence file. The query, service and console responsibilities, validation rules and expected tests were planned before the Copilot reviews.
Actual prompt/context supplied: Tow Copilot Chat reviews were requested. The first supplied queries.py, services.py and test_queries.py to review QRY-01–04 and FP-01–03. The second supplied console.py, main.py and test_workflows.py to review UI-01 and UI-02. Both prompts requested evidence-based findings ranked Critical, Important or Optional, without changing files or adding unnecessary features. The reported test result was 39 passed.
Actual response: The first review reported no Critical issues, one Important uncertainty about blank practitioner ID validation because data_store.py was not supplied, and three Optional test improvements. The second review found no confirmed Critical or Important defects and suggested three Optional automated console tests. Both responses were reviewed against the existing tests and manual verification.

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| Blank practitioner ID validation | Existing test checks that a blank practitioner ID raises ValueError. Copilot could not inspect data_store.py. | Important | Modify. The required behaviour is already tested, but the data-store implementation was not inspected by Copilot. | No code change. | Existing test passed in the 39-test suite. |
| Default all-status filtering | test_practitioner_filter_and_order already includes appointments with different statuses. | Optional | Reject. This behaviour is already covered by an existing test. | No change. | Query tests passed. |
| Equal-time appointment ID sorting | A1 and A3 have the same date/time, and the test checks their ID order. | Optional | Reject. The existing test already covers the tie-break rule. | No change. | Query tests passed. |
| Appointment object identity | Existing tests check original object identity in query results and cancellation history. | Optional | Reject for now. More identity assertions would be useful but are not essential. | No change. | Query and workflow tests passed. |
| Automated menu loop test | run_menu was tested manually, but no automated menu-level test exists. | Optional | Reject for now. Manual menu verification was completed, and automated console testing is not compulsory. | No change. | Manual UI-01 test succeeded. |
| Invalid menu choice recovery test | Console handles unknown choices and returns to the menu. | Optional | Reject for now. This was already tested manually. | No change. | Manual UI-02 test succeeded. |
| Invalid status console test | Console converts status text to AppointmentStatus and catches ValueError. | Optional | Reject for now. Manual UI recovery and automated service validation were tested. | No change. | Manual UI-02 succeeded; full suite 39 passed. |
Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: The domain objects enforce their own rules. SmartCareDataStore manages the shared in-memory records. Services handle registration, lookup, booking, cancellation and validation. Query functions only filter and sort supplied appointments without changing them. The console handles user input, output and expected errors. All services use the same store during one session, and cancelled appointments remain available for history.

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? The main architectural concern was keeping responsibilities separate. The console handles user input, services manage operations, the data store keeps records, and queries only filter and sort appointments. All services also need to share the same data store during one session.
2. Which Copilot suggestion did you reject as over-engineering, and why? Copilot did not suggest any major over-engineering. We rejected some optional extra tests because the existing tests already covered those cases. We decided to keep the implementation simple and avoid unnecessary changes.
3. How did you prove cancelled appointments remain retrievable and listable in the same session? I booked appointment A1 and cancelled it. Then I searched for A1 and confirmed it still existed with status CANCELLED. It also appeared when listing all appointments, but not when filtering by SCHEDULED. The automated workflow test confirmed the same behaviour.

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? It uses only the given inputs and returns a new list without changing the original appointments. Changing the original list, printing or reading user input would break purity.
2. Which explicit inputs are needed, and why avoid a global store? The function needs the appointment list, practitioner ID and optional status. A global store should be avoided because it creates hidden dependencies and makes testing harder.
3. How can a new list reuse Appointment objects safely? The query creates a new list containing references to the original Appointment objects. This is safe because the query does not change those objects.
4. Why use a named key, and what breaks equal-time ties? A named sorting key makes the sorting logic easier to reuse and understand. Appointments are sorted by date_time first, then appointment_id when the times are equal.
5. How do default and explicit status filters differ? The default status is None, which includes all appointment statuses. An explicit AppointmentStatus filter returns only appointments with that status.
6. How do empty, unknown practitioner and invalid filter cases differ? A registered practitioner with no matching appointments returns an empty list. An unknown practitioner raises LookupError. An invalid ID or non-enum status raises ValueError.
7. Which console errors recover, and how is unchanged state checked? The console handles invalid IDs, duplicate records, booking conflicts, invalid dates, invalid statuses and unknown menu choices. It displays an error and continues. Tests compare records before and after rejected operations to check that nothing changed.
8. What is data integrity for registered participants, conflicts and history? Appointments must use registered patient and practitioner objects. The system must reject bookings for the same practitioner at the same time and keep cancelled appointments available for history.
9. What is Copilot's review role, and who verifies findings? Copilot helps identify possible problems and suggest improvements. The team checks its suggestions against the code, requirements and tests before accepting or rejecting them.
10. How do pure functions and OOP responsibilities work together? Domain objects manage their own rules, the data store keeps records, and services coordinate operations. Pure query functions filter and sort appointments. The console handles user input and output without controlling the domain rules.

## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
