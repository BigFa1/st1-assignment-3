# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Mon 9:30 - 11:30 Group 4
- Members, GitHub usernames and cohorts: Member 1: Fahad Almajeed, BigFa1, UG. Member 2: Mohammed Aboset, MohammedAoset, UG. 
- Repository URL: https://github.com/BigFa1/st1-assignment-3
- Starting SHA: 61b3457

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Implement Patient Search by ID
- Context: The SmartCare system needs to allow users to find a registered patient using their patient ID.
- Requirement: FR-02: Patient Search
- Acceptance criteria: Return the existing patient when a valid registered ID is provided.
Raise ValueError for blank or invalid IDs.
Raise LookupError when the patient ID does not exist.
Remove surrounding spaces from IDs and keep searches case-sensitive.
- Scope: Implement PatientService.find_patient() in services.py and add relevant tests.
- Definition of Done: Implement PatientService.find_patient() in services.py and add relevant tests.
- Owner: Fahad Almajeed
- Actual issue link: https://github.com/BigFa1/st1-assignment-3/issues/1#issue-5940275008

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: Implement Appointment Cancellation
- Context: SmartCare needs to allow users to cancel scheduled appointments while keeping appointment history.
- Requirement: FR-06: Appointment Cancellation, FR-07: Retained Appointment History
- Acceptance criteria: Allow cancellation of scheduled appointments.
Change the appointment status to CANCELLED.
Keep cancelled appointments in the system.
Raise ValueError for invalid IDs or repeated cancellation.
Raise LookupError if the appointment does not exist.
Do not allow cancellation of completed appointments.
- Scope: Implement AppointmentService.cancel_appointment() in services.py and add relevant tests.
- Definition of Done: Appointment cancellation works correctly.
All tests pass.
Another team member reviews the Pull Request.
Changes are approved and merged into main.
- Owner: Fahad Almajeed
- Actual issue link: https://github.com/BigFa1/st1-assignment-3/issues/2#issue-5940307434

## B Commit quality

| Original example | Strong or Weak | Reason |
|---|----------------|-------|
| changes | Weak           | It does not explain what was Changed |
| final version | Weak           | It is unclear what was completed |
| Add patient search by ID | Strong         | It clearly describes the feature added.      |
| fix stuff | Weak           | It does not explain what was fixed.      |
| Prevent cancellation of completed appointments | Strong         | It clearly describes the behaviour being changed.      |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: The PR includes unrelated changes. It should focus only on appointment cancellation.
- Responsibility and architecture concerns: Unrelated code changes may affect other parts of SmartCare. Each class should keep its own responsibility.
- Testing and review concerns: The changes make the PR harder to review and test. Passing tests does not guarantee that everything is correct.
- Changes to remove or separate, with reasons: Remove the unrelated patient field changes, unnecessary code restructuring and new dependency. They should be handled separately if needed, so the PR stays focused on appointment cancellation.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: Copilot did not explain which tests passed, what code was reviewed, or whether all requirements were met.
- Follow-up review question 1: Did you check the code against the requirements?
- Follow-up review question 2: Are there tests for invalid and unknown IDs?
- Follow-up review question 3: Does appointment cancellation keep the appointment history?
- Follow-up review question 4: Does the code prevent cancelling completed or already cancelled appointments?
- Follow-up review question 5: Are there any unrelated changes in the Pull Request?
- Additional questions if useful: What test results or code lines support your review?

## E Team workflow agreement

| Practice | Team agreement                                                                                                          |
|---|-------------------------------------------------------------------------------------------------------------------------|
| Branch naming | Use clear feature branch names based on each task, such as feature/patient-lookup and feature/appointment-cancellation. |
| Commit message convention | Use short and specific commit messages that explain what was changed.                                                   |
| PR size | Keep each Pull Request small and focused on one issue, without unrelated changes.                                       |
| Another-member review requirement | Each Pull Request must be reviewed by a different team member before merging.                                           |
| Merge rule | Merge only when requirements are met, tests pass, feedback is resolved, and another member approves.                    |
| Significant Copilot disclosure rule | Disclose significant Copilot use in the PR and record how its suggestions were checked.                                 |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link                                                                             | Requirement | Owner          | Acceptance criteria or precise link | Status |
|----------------------------------------------------------------------------------------|--|----------------|--|--------|
| https://github.com/BigFa1/st1-assignment-3/issues/1#issue-5940275008                   | FR-02: Patient Search | Fahad Almajeed | Find a registered patient by ID. Raise ValueError for invalid IDs and LookupError for unknown IDs. | Open   |
| https://github.com/BigFa1/st1-assignment-3/issues/2#issue-5940307434                   | FR-06 / FR-07 Appointment Cancellation and Retained History | Fahad Almajeed | Cancel scheduled appointments, keep their history, and prevent invalid cancellation. | Open   |
 | https://github.com/BigFa1/st1-assignment-3/issues/3#issue-6030550671                   |Supporting Practitioner Lookup for FR-03.  | Fahad Almajeed | Return the stored practitioner by ID. Raise ValueError for invalid IDs and LookupError for unknown IDs. | Open   |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: https://github.com/BigFa1/st1-assignment-3/pull/4#issue-6056505414 , Add patient search by ID
- Linked issue and requirement: https://github.com/BigFa1/st1-assignment-3/issues/1#issue-5940275008 , FR-02: Patient Search
- Feature branch: feature/patient-lookup
- Changed behaviour: The system can now find a registered patient by ID and return the same stored patient. It raises LookupError for unknown IDs and ValueError for invalid IDs.
- Meaningful commits: [ba748368bf8cfd948f3f9663fe07c9ad35e54ef1]
- Test command, directory and observed result: py -m pytest in project, all 13 tests past
- Another-member reviewer: MohammadAboset 
- Human observations recorded before Copilot: Pending, awaiting Mohammed 
- Requirement, responsibilities, test assertions and unrelated-scope checks: FR-02 Patient Search implementation completed. ,PatientService uses the shared data store to find patients. ,Five patient search tests passed. ,Pending confirmation from Mohammed's review of the PR diff.
- Key feedback: awaiting Mohammed 
- Author response/change and verification: Awaiting reviewer
- Reviewer recheck and approval: Awaiting Mohammed review and approval
- Merge outcome and SHA: Not marge yet 
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: Fahad Almajeed, @BigFa1
- Implementation: PatientService.find_patient() on feature/patient-lookup. Commit: ba74836.
- Testing: Added five patient search tests. Ran the full test suite and observed 13 passed.
- Review: Inspected Git changes before committing. Another-member PR review is pending.
- Issue refinement: Created GitHub issues for patient search, appointment cancellation and practitioner lookup.
- Design and responsibility discussion: Used the existing SmartCareDataStore lookup method and kept the change focused on PatientService.
- Debugging or integration: Corrected a Git file-path error during staging. Integration into main is pending.
- Documentation or team support: Completed the initial Stage 6 activities and recorded Patient Search PR evidence.

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

A high commit count does not always mean strong contribution because some commits may be small or unnecessary. Good contribution depends on the quality of the work, testing, code review, teamwork and solving problems, not only the number of commits.

## L Stage 6 formative questions

1. What is version control?

Version control is a system that tracks changes to code and allows team members to work together and manage different versions.

2. Why is a feature branch useful?

A feature branch allows developers to work on a specific task without affecting the main branch.

3. What makes a commit a good engineering commit?

A good commit contains a clear, focused change with a meaningful message explaining what was changed.

4. What is a pull request?

A pull request is a request to review and merge changes from a feature branch into the main branch.

5. What is the purpose of code review?

Code review helps find mistakes, check requirements, improve code quality and ensure changes are correct before merging.

6. What does a Git diff show?

A Git diff shows the differences between versions of code, including added, removed and changed lines.

7. What is a Definition of Done?

A Definition of Done is a set of conditions that must be completed before a task is considered finished, including testing, review and approval.

8. What is the appropriate role of GitHub Copilot in pull-request review?

GitHub Copilot can help identify possible problems and suggest improvements, but humans must check its suggestions and make the final decisions.

9. Why should individual contribution not be judged only by commit count?

Because the number of commits does not show the quality of the work. Testing, reviewing, problem-solving and helping the team are also important.

10. What is the Stage 6 engineering rule?

A change is not complete just because the code works. It must meet the requirements, pass meaningful tests, receive human review, and be merged and verified on main.

## M Completion and handover

- Starting SHA: 
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
