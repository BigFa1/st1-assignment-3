# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.


| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | Register a patient using valid details. | Try to register a patient with an ID that already exists. | Check that the patient is stored correctly and a duplicate is rejected. |
| FR-05 Prevent practitioner conflict | Book a practitioner at an available time. | Try to book the same practitioner for two active appointments at the same time. | Check that the second booking is rejected and the original booking remains unchanged. |
| FR-06 Cancel appointment | Cancel an existing scheduled appointment. | Try to cancel an appointment that is already cancelled. | Check that the status changes to CANCELLED and repeated cancellation is rejected. |
| FR-07 Retain cancelled history | Cancel an appointment and view its history. | Check whether a cancelled appointment is missing from history. | Check that the cancelled appointment remains in history with the CANCELLED status. |


### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.


`assert True`
Judgement: Weak/unclear  Why: It always passes and does not check any behaviour.

`assert appointment is not None`
Judgement: Weak/unclear  Why: It only checks that an appointment exists, not whether its details are correct.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: Strong for stated behaviour  Why: It checks the cancelled status but does not prove that the appointment remains in history.

`assert len(results) > 0`
Judgement: Weak/unclear  Why: It checks that results exist but not whether they are correct.

`assert data_store.find_appointment('A1') is appointment`
Judgement: Strong for stated behaviour  Why: It checks that the stored appointment is the exact expected object but does not verify all its details.

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: 
1. Blank identifiers
Input: A patient ID is empty.
Expected result: The system rejects the ID with a ValueError.
Supporting contract: Patient identifiers must not be blank.

2. Whitespace-only names
Input: A patient name contains only spaces.
Expected result: The system rejects the name with a ValueError.
Supporting contract: Patient names must contain valid text.

3. Same-time practitioner bookings
Input: Two active appointments use the same practitioner and time.
Expected result: The second booking is rejected, and the first appointment remains unchanged.
Supporting contract: FR-05 prevents practitioner booking conflicts.

4. Cancelled appointments
Input: An appointment has already been cancelled.
Expected result: A second cancellation is rejected, and the appointment remains CANCELLED.
Supporting contract: FR-06 prevents repeated cancellation.

5. Invalid status transitions
Input: Attempt to change a CANCELLED appointment back to SCHEDULED.
Expected result: The change is rejected, and the status remains CANCELLED.
Supporting contract: Cancelled appointments cannot return to SCHEDULED.


### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong                                               | Rewritten test intention                                               |
|-----------|-------------------------------------------------------------|------------------------------------------------------------------------|
| 1         | Only checks that an object is not None.                     | Check that a registered patient has the correct ID and name.           |
| 2         | Only checks that an object is not None.                     | Check that a booked appointment has the correct practitioner and time. |
| 3         | Uses assert True, which always passes.                      | Check that cancelling an appointment changes its status to CANCELLED.  |
| 4         | Assumes SMS notifications exist, but they are not required. | Check that the system rejects conflicting practitioner bookings.       |
| 5         | Assumes SMS notifications exist, but they are not required. | Check that cancelled appointments remain in appointment history.       |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
100% code coverage means all code was executed during testing, but it does not mean the tests checked the correct results. Weak assertions and missing test scenarios can allow defects to go undetected.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement                         | Acceptance criterion                                                                    | Test ID | Test type          | Test name / location                                                                 | Expected behaviour                                                                                                                                     | Result / observed status   | Supplied or student-authored |
|-------------------------------------|-----------------------------------------------------------------------------------------|---------|--------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| FR-01 Register patient              | AC-01.1                                                                                 | TEST-01 | Service / Positive | test_register_valid_patient / project/tests/test_services.py (planned)               | A patient with valid details and a unique ID is stored successfully.                                                                                   | Not implemented or run yet | Student-authored (planned)   |
| FR-01 Register patient              | AC-01.2                                                                                 | TEST-02 | Service / Negative | test_duplicate_patient_id_is_rejected / project/tests/test_services.py (planned)     | Registering a patient with an existing ID raises ValueError, and the original patient remains stored.                                                  | Not implemented or run yet | Student-authored (planned)   |
| FR-02 Find patient                  | AC-02.1                                                                                 | TEST-03 | Service / Positive | test_find_existing_patient / project/tests/test_services.py (planned)                | Looking up a registered patient ID returns the correct patient.                                                                                        | Not implemented or run yet | Student-authored (planned)   |
| FR-02 Find patient                  | AC-02.2                                                                                 | TEST-04 | Service / Negative | test_find_unknown_patient_is_rejected / project/tests/test_services.py (planned)     | Looking up a valid but unknown patient ID raises LookupError.                                                                                          | Not implemented or run yet | Student-authored (planned)   |
| FR-04 Book appointment              | AC-03.1                                                                                 | TEST-05 | Service / Positive | test_book_valid_appointment / project/tests/test_services.py (planned)               | Booking registered participants with a unique appointment ID and available time creates a stored SCHEDULED appointment.                                | Not implemented or run yet | Student-authored (planned)   |
| FR-04 Book appointment              | AC-03.2                                                                                 | TEST-06 | Service / Negative | test_book_with_unknown_participant / project/tests/test_services.py (planned)        | Booking with an unknown patient or practitioner raises LookupError, and no appointment is stored.                                                      | Not implemented or run yet | Student-authored (planned)   |
| FR-05 Prevent practitioner conflict | AC-04.1                                                                                 | TEST-07 | Service / Negative | test_practitioner_booking_conflict / project/tests/test_services.py (planned)        | Booking the same practitioner at the same time as an existing SCHEDULED appointment raises ValueError, and the original appointment remains unchanged. | Not implemented or run yet | Student-authored (planned)   |
| FR-05 Prevent practitioner conflict | AC-04.2                                                                                 | TEST-08 | Service / Positive | test_different_practitioner_same_time / project/tests/test_services.py (planned)     | Two different practitioners can each have a SCHEDULED appointment at the same time.                                                                    | Not implemented or run yet | Student-authored (planned)   |
| FR-06 Cancel appointment            | AC-05.1                                                                                 | TEST-09 | Service / Positive | test_cancel_scheduled_appointment / project/tests/test_services.py (planned)         | Cancelling a SCHEDULED appointment changes its status to CANCELLED.                                                                                    | Not implemented or run yet | Student-authored (planned)   |
| FR-07 Appointment history           | AC-05.2                                                                                 | TEST-10 | Service / Positive | test_cancelled_appointment_history / project/tests/test_services.py (planned)        | A cancelled appointment remains stored and can be retrieved from appointment history during the current session.                                       | Not implemented or run yet | Student-authored (planned)   |
| FR-06 Cancel appointment            | AC-05.3                                                                                 | TEST-11 | Service / Negative | test_cancel_already_cancelled_appointment / project/tests/test_services.py (planned) | Attempting to cancel an already CANCELLED appointment raises ValueError, and its status remains CANCELLED.                                             | Not implemented or run yet | Student-authored (planned)   |
| FR-08 Find appointment              | AC-06.1                                                                                 | TEST-12 | Service / Positive | test_find_existing_appointment / project/tests/test_services.py (planned)            | Looking up an existing appointment ID returns the correct appointment.                                                                                 | Not implemented or run yet | Student-authored (planned)   |
| FR-01 Register patient              | Revision 2 validation contract: Patient names must contain valid text (no canonical AC) | TEST-21 | Domain / Negative  | test_whitespace_only_patient_name_rejected / project/tests/test_domain.py (planned)  | ValueError is raised, and no valid Patient object is created.                                                                                          | Not implemented or run yet | Student-authored (planned)   |

The traceability matrix includes 13 planned tests covering patient registration, patient lookup, appointment booking, practitioner conflicts, cancellation, appointment history, and appointment lookup. The tests include positive and negative scenarios. These tests have not been implemented or executed yet because Stage 6 integration is still pending.

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement                         | Acceptance criterion                                                                    | Positive / Negative / Boundary | Test intention                                                                                                        | Observable result expected                                                                                    | Added evidence beyond supplied tests                                                                                           |
|---------|-------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| TEST-01 | FR-01 Register patient              | AC-01.1                                                                                 | Positive                       | Check that a patient with valid details and a unique ID can be registered.                                            | The patient is stored and can be retrieved using the same ID.                                                 | Confirms that registration actually saves the correct patient, rather than only checking that no error occurs.                 |
| TEST-02 | FR-01 Register patient              | AC-01.2                                                                                 | Negative                       | Check that registering a patient with an existing ID is rejected.                                                     | ValueError is raised, and the original patient remains stored without changes.                                | Confirms that duplicate registration is rejected without overwriting existing patient information.                             |
| TEST-03 | FR-02 Find patient                  | AC-02.1                                                                                 | Positive                       | Check that searching for a registered patient ID returns the correct patient.                                         | The system returns the patient with the matching ID and details.                                              | Confirms that patient lookup returns the correct record, rather than just any patient.                                         |
| TEST-04 | FR-02 Find patient                  | AC-02.2                                                                                 | Negative                       | Check that searching for a patient ID that does not exist is handled correctly.                                       | The system raises LookupError because the patient cannot be found.                                            | Confirms that the system reports a missing patient instead of returning an incorrect record.                                   |
| TEST-05 | FR-04 Book appointment              | AC-03.1                                                                                 | Positive                       | Check that an appointment can be booked with registered participants, a unique appointment ID, and an available time. | The appointment is stored with the status SCHEDULED.                                                          | Confirms that booking creates and stores an appointment with the correct status, rather than only completing without an error. |
| TEST-06 | FR-04 Book appointment              | AC-03.2                                                                                 | Negative                       | Check that booking an appointment with an unknown patient or practitioner is rejected.                                | The booking is rejected, and no appointment is stored.                                                        | Confirms that the system checks whether both participants are registered before creating an appointment.                       |
| TEST-07 | FR-05 Prevent practitioner conflict | AC-04.1                                                                                 | Negative                       | Check that a practitioner cannot have two SCHEDULED appointments at exactly the same time.                            | The second booking raises ValueError, and the original appointment remains unchanged.                         | Confirms that the system prevents double-booking without affecting an existing appointment.                                    |
| TEST-08 | FR-05 Prevent practitioner conflict | AC-04.2                                                                                 | Positive                       | Check that two different practitioners can have appointments at the same time.                                        | Both appointments are successfully stored with the status SCHEDULED.                                          | Confirms that the system prevents conflicts only for the same practitioner, without blocking valid bookings for others.        |
| TEST-09 | FR-06 Cancel appointment            | AC-05.1                                                                                 | Positive                       | Check that a SCHEDULED appointment can be cancelled successfully.                                                     | The appointment status changes from SCHEDULED to CANCELLED.                                                   | Confirms that cancellation updates the appointment status correctly instead of deleting the appointment.                       |
| TEST-10 | FR-07 Appointment history           | AC-05.2                                                                                 | Positive                       | Check that a cancelled appointment remains available in the appointment history.                                      | The cancelled appointment can still be retrieved during the current session with its status set to CANCELLED. | Confirms that cancellation keeps the appointment record instead of removing it from the system.                                |
| TEST-11 | FR-06 Cancel appointment            | AC-05.3                                                                                 | Negative                       | Check that an already CANCELLED appointment cannot be cancelled again.                                                | The system raises ValueError, and the appointment status remains CANCELLED.                                   | Confirms that repeated cancellation is rejected without changing the existing appointment record.                              |
| TEST-12 | FR-08 Find appointment              | AC-06.1                                                                                 | Positive                       | Check that searching for an existing appointment ID returns the correct appointment.                                  | The system returns the appointment with the matching ID and details.                                          | Confirms that appointment lookup retrieves the correct record rather than an unrelated appointment.                            |
| TEST-21 | FR-01 Register patient              | Revision 2 validation contract: Patient names must contain valid text (no canonical AC) | Boundary / Negative            | Check that creating a Patient with a whitespace-only name is rejected.                                                | ValueError is raised, and no valid Patient object is created.                                                 | Adds evidence that whitespace-only names are rejected, not just blank patient IDs.                                             |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange                                                                                                               | Act                                                                                      | Assert                                                                                                                          | Why meaningful / why assertion proves criterion                                                                      |
|---------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| TEST-01 | Create a patient with valid details and a unique ID.                                                                  | Register the patient using the registration service.                                     | Check that the patient can be found using the same ID and that the stored details match.                                        | Proves that registration saves the correct patient, not just that the function runs without an error.                |
| TEST-02 | Register a patient with a unique ID, then prepare another patient using the same ID.                                  | Attempt to register the second patient.                                                  | Use pytest.raises(ValueError) to confirm the duplicate is rejected. Check that the original patient's details remain unchanged. | Proves that duplicate patient IDs are rejected without overwriting existing information.                             |
| TEST-03 | Register a patient with a known ID and valid details.                                                                 | Search for the patient using the patient lookup service.                                 | Check that the returned patient has the correct ID and details.                                                                 | Proves that the lookup service retrieves the correct registered patient rather than an unrelated record.             |
| TEST-04 | Prepare a valid patient ID that is not registered in the system.                                                      | Search for the unknown patient using the patient lookup service.                         | Use pytest.raises(LookupError) to confirm that the patient cannot be found.                                                     | Proves that the lookup service correctly reports an unknown patient instead of returning an incorrect record.        |
| TEST-05 | Register a patient and practitioner, then prepare a unique appointment ID and an available time.                      | Book an appointment using the booking service.                                           | Check that the appointment is stored with the correct patient, practitioner, time, and SCHEDULED status.                        | Proves that booking creates the correct appointment and stores all required information.                             |
| TEST-06 | Register a valid patient and practitioner, then prepare an unknown patient ID or practitioner ID.                     | Attempt to book an appointment using the unknown participant.                            | Confirm that the booking raises LookupError and that no appointment is stored.                                                  | Proves that the system rejects bookings involving unregistered participants without creating an invalid appointment. |
| TEST-07 | Register a patient and practitioner, then create a SCHEDULED appointment at a specific time.                          | Attempt to book another appointment with the same practitioner at exactly the same time. | Use pytest.raises(ValueError) to confirm the conflict is rejected. Check that the original appointment remains unchanged.       | Proves that the system prevents double-booking without affecting an existing appointment.                            |
| TEST-08 | Register two practitioners and the required patients, then create a SCHEDULED appointment for the first practitioner. | Book another appointment with the second practitioner at exactly the same time.          | Check that both appointments are stored with the status SCHEDULED.                                                              | Proves that the system allows appointments at the same time when the practitioners are different.                    |
| TEST-09 | Register a patient and practitioner, then create a SCHEDULED appointment.                                             | Cancel the appointment using the cancellation service.                                   | Check that the appointment status changes from SCHEDULED to CANCELLED.                                                          | Proves that cancellation correctly updates the appointment status rather than deleting the record.                   |
| TEST-10 | Register a patient and practitioner, create a SCHEDULED appointment, then cancel it.                                  | Retrieve the cancelled appointment from the appointment history during the same session. | Check that the appointment is still stored with the correct ID and CANCELLED status.                                            | Proves that cancelled appointments remain available in the history instead of being deleted.                         |
| TEST-11 | Register a patient and practitioner, create a SCHEDULED appointment, then cancel it once.                             | Attempt to cancel the same appointment again.                                            | Use pytest.raises(ValueError) to confirm the second cancellation is rejected. Check that the appointment remains CANCELLED.     | Proves that repeated cancellation is prevented without changing the existing appointment record.                     |
| TEST-12 | Register a patient and practitioner, then create an appointment with a known ID.                                      | Search for the appointment using the appointment lookup service.                         | Check that the returned appointment has the correct ID, patient, practitioner, time, and status.                                | Proves that the lookup service retrieves the correct appointment rather than an unrelated record.                    |
| TEST-21 | Prepare a Patient using a valid ID but a name containing only spaces.                                                 | Attempt to create the Patient object.                                                    | Use pytest.raises(ValueError) to confirm that construction is rejected.                                                         | Proves that whitespace-only patient names cannot create invalid Patient objects.                                     |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour                                                                                                               | Test file/function                                                                  | Result                     |
|---------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------|
| TEST-13 | Check that a Patient object can be created with valid details and that its attributes are stored correctly.             | project/tests/test_domain.py / test_valid_patient_construction (planned)            | Not implemented or run yet |
| TEST-14 | Check that creating a Patient with a blank patient ID is rejected.                                                      | project/tests/test_domain.py / test_blank_patient_id_is_rejected (planned)          | Not implemented or run yet |
| TEST-15 | Check that a Practitioner object can be created with valid details and that its attributes are stored correctly.        | project/tests/test_domain.py / test_valid_practitioner_construction (planned)       | Not implemented or run yet |
| TEST-16 | Check that creating a Practitioner with a blank practitioner ID raises ValueError.                                      | project/tests/test_domain.py / test_blank_practitioner_id_is_rejected (planned)     | Not implemented or run yet |
| TEST-17 | Check that an Appointment object can be created with valid details and starts with the status SCHEDULED.                | project/tests/test_domain.py / test_valid_appointment_construction (planned)        | Not implemented or run yet |
| TEST-18 | Check that cancelling a SCHEDULED Appointment changes its status to CANCELLED.                                          | project/tests/test_domain.py / test_appointment_cancellation (planned)              | Not implemented or run yet |
| TEST-19 | Check that attempting to cancel an already CANCELLED Appointment raises ValueError and leaves its status unchanged.     | project/tests/test_domain.py / test_repeated_appointment_cancellation (planned)     | Not implemented or run yet |
| TEST-20 | Check that attempting an illegal status transition on an Appointment raises ValueError and leaves its status unchanged. | project/tests/test_domain.py / test_invalid_appointment_status_transition (planned) | Not implemented or run yet |
| TEST-21 | Check that creating a Patient with a whitespace-only name raises ValueError.                                            | project/tests/test_domain.py / test_whitespace_only_patient_name_rejected (planned) | Not implemented or run yet |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour                                                                                                                                                        | Requirement / criterion | Test file/function                                                                   | Result                     |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------|----------------------------|
| TEST-01 | Register a patient with valid details and a unique ID, then confirm the patient is stored.                                                                       | FR-01 / AC-01.1         | project/tests/test_services.py / test_register_valid_patient (planned)               | Not implemented or run yet |
| TEST-02 | Attempt to register a patient using an existing patient ID and confirm the duplicate is rejected without changing the original record.                           | FR-01 / AC-01.2         | project/tests/test_services.py / test_duplicate_patient_id_is_rejected (planned)     | Not implemented or run yet |
| TEST-03 | Search for a registered patient using their ID and confirm the correct patient is returned.                                                                      | FR-02 / AC-02.1         | project/tests/test_services.py / test_find_existing_patient (planned)                | Not implemented or run yet |
| TEST-04 | Search for a valid patient ID that is not registered and confirm the system raises LookupError.                                                                  | FR-02 / AC-02.2         | project/tests/test_services.py / test_find_unknown_patient_is_rejected (planned)     | Not implemented or run yet |
| TEST-05 | Book an appointment with registered participants, a unique appointment ID, and an available time. Confirm it is stored with SCHEDULED status.                    | FR-04 / AC-03.1         | project/tests/test_services.py / test_book_valid_appointment (planned)               | Not implemented or run yet |
| TEST-06 | Attempt to book an appointment using an unknown patient or practitioner ID and confirm the booking is rejected without storing an appointment.                   | FR-04 / AC-03.2         | project/tests/test_services.py / test_book_with_unknown_participant (planned)        | Not implemented or run yet |
| TEST-07 | Attempt to book a second appointment with the same practitioner at exactly the same time as an existing SCHEDULED appointment. Confirm the conflict is rejected. | FR-05 / AC-04.1         | project/tests/test_services.py / test_practitioner_booking_conflict (planned)        | Not implemented or run yet |
| TEST-08 | Book two appointments at exactly the same time with different registered practitioners. Confirm both bookings are accepted and stored with SCHEDULED status.     | FR-05 / AC-04.2         | project/tests/test_services.py / test_different_practitioner_same_time (planned)     | Not implemented or run yet |
| TEST-09 | Cancel an existing SCHEDULED appointment and confirm its status changes to CANCELLED.                                                                            | FR-06 / AC-05.1         | project/tests/test_services.py / test_cancel_scheduled_appointment (planned)         | Not implemented or run yet |
| TEST-10 | Cancel a SCHEDULED appointment, then retrieve it from appointment history during the same session. Confirm the record is still available with CANCELLED status.  | FR-07 / AC-05.2         | project/tests/test_services.py / test_cancelled_appointment_history (planned)        | Not implemented or run yet |
| TEST-11 | Attempt to cancel an already CANCELLED appointment and confirm that ValueError is raised while its status remains CANCELLED.                                     | FR-06 / AC-05.3         | project/tests/test_services.py / test_cancel_already_cancelled_appointment (planned) | Not implemented or run yet |
| TEST-12 | Search for an existing appointment using its ID and confirm that the correct appointment and its details are returned.                                           | FR-08 / AC-06.1         | project/tests/test_services.py / test_find_existing_appointment (planned)            | Not implemented or run yet |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour                             | Boundary/invalid input                                                                              | Expected result                                                                                             | Test ID |
|---------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------|
| Duplicate patient registration        | Attempt to register a patient using an ID that already exists.                                      | ValueError is raised, and the original patient remains stored without changes.                              | TEST-02 |
| Unknown patient lookup                | Search using a valid patient ID that does not exist in the system.                                  | LookupError is raised, and the existing patient records remain unchanged.                                   | TEST-04 |
| Booking with an unknown participant   | Attempt to book an appointment using an unregistered patient ID or practitioner ID.                 | LookupError is raised, no appointment is created, and existing appointments remain unchanged.               | TEST-06 |
| Practitioner booking conflict         | Attempt to book a second SCHEDULED appointment with the same practitioner at exactly the same time. | ValueError is raised, the second appointment is not stored, and the original appointment remains unchanged. | TEST-07 |
| Repeated appointment cancellation     | Attempt to cancel an appointment that already has the status CANCELLED.                             | ValueError is raised, and the appointment remains stored with the status CANCELLED.                         | TEST-11 |
| Blank patient ID validation           | Attempt to create a Patient using an empty or whitespace-only patient ID.                           | ValueError is raised, and no valid Patient object is created.                                               | TEST-14 |
| Blank practitioner ID validation      | Attempt to create a Practitioner using an empty or whitespace-only practitioner ID.                 | ValueError is raised, and no valid Practitioner object is created.                                          | TEST-16 |
| Invalid appointment status transition | Attempt to change an appointment from CANCELLED back to SCHEDULED.                                  | ValueError is raised, and the appointment remains CANCELLED.                                                | TEST-20 |
| Whitespace-only patient name          | Attempt to create a Patient using a name containing only spaces. A ValueError should be raised.     | ValueError is raised, and no valid Patient object is created.                                               | TEST-21 |


## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: FR-06 Cancel appointment
Acceptance criterion: AC-05.3 — Attempting to cancel an already CANCELLED appointment must be rejected.
Behaviour to test: Check that attempting to cancel an already CANCELLED appointment raises ValueError and leaves the appointment status unchanged.
Human-first test idea/categories: Negative test. Create a valid SCHEDULED appointment and cancel it once. Attempt to cancel it again using pytest.raises(ValueError). Check that the appointment remains CANCELLED and is still stored.
Prompt and purpose: GitHub Copilot was asked to propose pytest test candidates for FR-06 / AC-05.3, covering valid, invalid and boundary cases. The prompt required observable outcomes, the current SmartCare public contracts, the shared SmartCareDataStore, synthetic data and no invented features. Purpose: To compare Copilot's suggestions with my human-first test design and evaluate their correctness and assertion quality.

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: GitHub Copilot suggested three candidates: (1) valid appointment cancellation, (2) rejection of repeated cancellation, and (3) rejection when the appointment status is exactly CANCELLED. Candidate 2 directly targets FR-06 / AC-05.3. Candidate 1 relates to AC-05.1, while Candidate 3 duplicates Candidate 2.
- What it claims to verify: Candidate 1 checks that a SCHEDULED appointment can be cancelled successfully (FR-06 / AC-05.1). Candidate 2 checks that cancelling an already CANCELLED appointment is rejected and its status remains unchanged (FR-06 / AC-05.3). Candidate 3 checks the same CANCELLED status condition as Candidate 2, so it does not provide additional verification.
- Requirement trace: Candidate 1 relates to FR-06 / AC-05.1 (TEST-09), which covers successful cancellation. Candidate 2 directly relates to FR-06 / AC-05.3 (TEST-11), which requires repeated cancellation to be rejected. Candidate 3 also relates to FR-06 / AC-05.3 (TEST-11), but duplicates Candidate 2 without adding new evidence.
- Assertion quality: Candidate 1 checks that cancellation succeeds and the appointment becomes CANCELLED, but its suggested is_successful() method is not confirmed by the SmartCare contract. Candidate 2 checks that repeated cancellation is rejected and the appointment remains CANCELLED, which is meaningful for AC-05.3. However, Copilot incorrectly suggested ContractError instead of ValueError. Candidate 3 repeats the same assertions as Candidate 2 without adding useful evidence. Candidate 2 should use pytest.raises(ValueError) and verify that the stored appointment remains CANCELLED.
- Human critique: Copilot suggested relevant cancellation tests, but the examples need corrections before implementation. Candidate 1 assumes an unconfirmed success-result method and is related to AC-05.1 rather than the selected AC-05.3. Candidate 2 correctly targets repeated cancellation but uses ContractError instead of the required ValueError. It also includes placeholder functions that must be replaced with actual SmartCare public methods. Candidate 3 duplicates Candidate 2 and does not add meaningful test coverage. Candidate 2 is the strongest suggestion, but it must be modified and checked against the actual project code before use.
- Decision: Candidate 1 — Modify. Candidate 2 — Modify. Candidate 3 — Reject. Candidate 1 needs changes to match the actual SmartCare public methods. Candidate 2 needs the correct ValueError assertion and actual project methods. Candidate 3 is rejected because it duplicates Candidate 2 without providing additional verification.
- Reason: Candidate 1 requires modification because it assumes a success-result method that may not exist in SmartCare. Candidate 2 requires modification because the actual contract specifies ValueError for repeated cancellation, not ContractError. Its assertions must also verify that the stored appointment remains CANCELLED. Candidate 3 is rejected because it tests the same condition as Candidate 2 without adding meaningful evidence. These decisions ensure the tests follow the actual requirements and use strong assertions.
- Final test reference if accepted/modified: Candidate 1 — proposed modification relates to TEST-09, project/tests/test_services.py / test_cancel_scheduled_appointment (planned). Candidate 2 — proposed modification relates to TEST-11, project/tests/test_services.py / test_cancel_already_cancelled_appointment (planned). Candidate 3 — rejected; no separate test will be added. Candidates 1 and 2 have been reviewed, but their code has not yet been adapted, implemented or executed.
- Actual verification result: GitHub Copilot generated three test candidates, which were reviewed against the SmartCare requirements. Candidate 1 was marked Modify, Candidate 2 was marked Modify, and Candidate 3 was marked Reject. No Copilot-generated test code has been implemented or executed. The planned modifications will be verified against the actual SmartCare implementation after Stage 6 integration. Test results will be recorded after running pytest.

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? Candidate 2, test_cancel_appointment_rejects_already_cancelled_appointment, looked convincing because it checked that repeated cancellation was rejected and the appointment remained CANCELLED. However, it used ContractError instead of the required ValueError and included placeholder methods that were not verified against the actual SmartCare implementation.
Why was it weak? The test used pytest.raises(ContractError), but the SmartCare contract requires ValueError when cancelling an already CANCELLED appointment. It also used placeholder functions and methods that may not exist in the project. Therefore, the test could fail because of incorrect test code rather than a genuine defect in the cancellation feature.
How did you strengthen it? I reviewed Candidate 2 and identified the changes needed to make it more reliable. The revised test design uses pytest.raises(ValueError) instead of ContractError and checks that the appointment remains stored with the CANCELLED status after the rejected cancellation. The placeholder methods will be replaced with the actual SmartCare public methods during implementation. These improvements are planned and have not yet been implemented or executed.
Accepted / modified / rejected test decisions and evidence: Three GitHub Copilot test candidates were reviewed. Candidate 1 was marked Modify because it assumed an unconfirmed success-result method. Candidate 2 was marked Modify because it used ContractError instead of ValueError and included unverified placeholder methods. Candidate 3 was marked Reject because it duplicated Candidate 2 without adding meaningful verification. The original Copilot response and the evaluation in Section H provide evidence of these decisions. No generated tests have been implemented or executed yet.

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command                    | Working directory | Code SHA                           | Passed  | Failed  | Failure summary                        | Product defect / test defect / unresolved | Evidence and interpretation                                                                 |
|----------------------------|-------------------|------------------------------------|---------|---------|----------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------|
| python -m pytest (planned) | project/          | Pending — record actual commit SHA | Not run | Not run | Pending — tests have not been executed | Unresolved — awaiting actual test results | Regression run will be completed after Stage 6 integration and Stage 7 test implementation. |


Individual test runs and changed-order independence evidence: Pending — individual tests and changed-order runs have not been executed yet. Commands, actual results, and evidence will be recorded after Stage 6 integration and Stage 7 test implementation.
Optional tutor-led demonstration notes: 
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: Pending — the Stage 7 tests have not been implemented or executed yet. Actual observations, any identified defects, corrections, and verification results will be recorded after testing.

## K What the Suite Still Does Not Prove

What does your test suite still not prove? The planned tests cover the main SmartCare requirements, but they cannot prove that the application is completely free of errors. Even if all tests pass, some unexpected inputs or situations may not have been tested. The actual limitations will be reviewed after the tests are implemented and executed.
Coverage if used: Not used yet. No coverage measurement has been performed for the Stage 7 tests.
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? Important areas include invalid inputs, duplicate IDs, appointment conflicts, and repeated cancellation. These cases matter because errors could lead to incorrect patient or appointment records. A high coverage percentage only shows that code was executed, not that the tests checked the correct results. Strong assertions and meaningful test cases are still necessary.
Optional fixtures/parametrisation used and why, if any: Not used yet. Fixtures and parametrisation may be considered during test implementation to reduce repeated setup and test different inputs.


## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task                                | Branch                          | PR                                                         | Reviewer                          | Key feedback                                | Outcome                             |
|-------------------------------------------|---------------------------------|------------------------------------------------------------|-----------------------------------|---------------------------------------------|-------------------------------------|
| Stage 6 documentation and review evidence | feature/stage06-review-evidence | [PR #5](https://github.com/BigFa1/st1-assignment-3/pull/5) | Fahad (review requested; pending) | Pending — no reviewer feedback received yet | PR open — awaiting review and merge |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member          | Actual contribution                                                                                                                                          | Evidence link                                                                                           |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Mohammed Aboset | Prepared Stage 7 test designs, acceptance-criteria traceability, planned test cases, and testing documentation. Also prepared Stage 6 documentation and review evidence. | [Stage 6 PR #5](https://github.com/BigFa1/st1-assignment-3/pull/5); Stage 7 documentation (local, not pushed yet) |
| Fahad | Worked on Stage 6 patient lookup implementation and submitted PR #4 for review.| [Stage 6 PR #4](https://github.com/BigFa1/st1-assignment-3/pull/4) |

## N Formative Questions

1. What question does verification answer?
Verification answers: "Are we building the product right?" It checks whether the software follows the specified requirements and design.

2. What question does validation answer?
Validation answers: "Are we building the right product?" It checks whether the software meets the user's needs and expectations.

3. What is a unit test?
A unit test checks one small part of a program, such as a function or method, to make sure it works correctly.

4. What is a pytest fixture?
A pytest fixture provides reusable test data or setup before a test runs. It helps avoid repeating the same setup code.

5. What is parametrisation in pytest?
Parametrisation allows the same test to run with different input values. It helps test multiple cases without writing separate test functions.

6. What is regression testing?
Regression testing checks that existing features still work correctly after changes have been made to the software.

7. What does code coverage tell us, and what does it not prove?
Code coverage shows how much of the code is executed during testing. However, it does not prove that the code works correctly or that all possible errors have been found.

8. What makes an assertion weak?
An assertion is weak when it only checks that something exists or that code runs without errors, instead of checking the actual expected result.

9. What is the appropriate role of GitHub Copilot as a test assistant?
GitHub Copilot can suggest test ideas and help write test code. However, the developer must review, verify, and correct its suggestions before accepting them.

10. What is the Stage 7 engineering rule?
Tests must be linked to real requirements, use meaningful assertions, and verify actual behaviour. All tests must be reviewed and their results recorded accurately.

## O Stage Completion

Tested Stage 7 main SHA: Pending — Stage 7 tests have not yet been implemented or executed.
Full-suite result: Not run yet — awaiting Stage 6 integration and Stage 7 test implementation.
Unresolved defects and effect on baseline: Pending — Stage 6 integration and Stage 7 testing are not yet complete. Any identified defects and their effect on the baseline will be recorded after testing.
Clean working tree and integration evidence: Pending — final integration, Git status verification, and evidence of the tested commit will be recorded after Stage 6 review and Stage 7 implementation.
Stage 8 handover status: Not ready — Stage 7 testing and verification must be completed before proceeding to Stage 8. No Stage 8 work has been assigned yet.
All tutorial/formative responses and traceability/Copilot decisions complete: Tutorial exit question and formative responses completed. Test designs and traceability prepared. Copilot decisions remain pending until an actual Copilot-generated test is reviewed.
