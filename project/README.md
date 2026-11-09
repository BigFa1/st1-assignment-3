# SmartCare v1.0 - Course Release Candidate

## Project Overview

SmartCare is a simple Python appointment management application developed for Software Technology 1 Assignment 3 at the University of Canberra.

It allows users to register patients and practitioners, book appointments, cancel appointments and search appointment records.

This release covers the undergraduate requirements from Stages 6, 7, 8 and 9, with final verification in Stage 12.

## Requirements

- Python 3.13 (teaching baseline)
- Python 3.14.7 (locally tested)
- pytest 9.2.0 (locally tested)
- GitHub Copilot was the permitted coding assistant.

The application uses the Python standard library. pytest is used for testing.

## Installation

Open a terminal in the project/ directory.

Install the testing dependency:

```sh
python -m pip install -r requirements-dev.txt
```

## Running SmartCare

Run the original demonstration:

```sh
python main.py
```

Run the interactive application:

```sh
python main.py --interactive
```

Run all automated tests:

```sh
python -m pytest -q
```

## Features

- Register and find patients.
- Register and find practitioners.
- Book appointments.
- Prevent conflicting appointments for the same practitioner.
- Allow different practitioners to have appointments at the same time.
- Cancel scheduled appointments.
- Keep cancelled appointments available for lookup.
- List practitioner appointments.
- Filter appointments by status.
- Sort appointments by date, time and appointment ID.
- Handle invalid user inputs.

## Project Structure

- main.py: Starts the application.
- smartcare/domain.py: Defines patients, practitioners and appointments.
- smartcare/data_store.py: Stores records in memory.
- smartcare/services.py: Handles registration, booking, cancellation and lookup.
- smartcare/queries.py: Filters and sorts appointments.
- smartcare/console.py: Provides the interactive menu.
- tests/: Contains automated tests.

## Testing

The Stage 12 regression test was performed using Python 3.14.7 and pytest 9.2.0.

Command:

```sh
python -m pytest -q
```

Result: 39 tests passed, 0 failed.

Starting release SHA:
26a6195ac76a66298b98a3e383fb0a6406f2b918

Final tested release SHA: Pending final verification.

## Known Limitations

- All data is stored in memory and disappears when the application closes.
- There is no database or permanent storage.
- Appointment rescheduling is not supported.
- Appointment times use local minute precision without timezone information.
- There is no user authentication or role management.
- The application does not include patient portals, notifications, billing or clinical decision support.
- The application is intended for coursework and demonstration, not real healthcare use.
- Only synthetic patient and practitioner information should be used.

## Responsible AI Use

GitHub Copilot was the permitted coding assistant during development. AI-assisted work must be reviewed and verified by the team. The application is tested using automated tests and manual demonstrations.

## Release Information

Release: SmartCare v1.0 course release candidate.

Repository:
https://github.com/BigFa1/st1-assignment-3

Final release approval and submitted SHA will be recorded in the Stage 12 evidence document.