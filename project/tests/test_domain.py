import pytest
from datetime import datetime, timezone
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.domain import Patient, Practitioner


def test_valid_patient_construction():
    patient = Patient("P1", "Ahmed")
    assert patient.patient_id == "P1"
    assert patient.name == "Ahmed"


def test_blank_patient_id_is_rejected():
    with pytest.raises(ValueError):
        Patient(" ", "Ahmed")

def test_whitespace_patient_name_is_rejected():
    with pytest.raises(ValueError):
        Patient("P1", "   ")


def test_valid_practitioner_construction():
    doctor = Practitioner("DR1", "Sara", "GP")
    assert doctor.practitioner_id == "DR1"
    assert doctor.name == "Sara"
    assert doctor.specialty == "GP"


def test_blank_practitioner_id_is_rejected():
    with pytest.raises(ValueError):
        Practitioner(" ", "Sara", "GP")


def test_valid_appointment_construction():
    patient = Patient("P1", "Ahmed")
    doctor = Practitioner("DR1", "Sara", "GP")
    appointment = Appointment(
        "A1", patient, doctor, datetime(2026, 10, 1, 9)
    )

    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is doctor
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_appointment_rejects_seconds():
    patient = Patient("P1", "Ahmed")
    doctor = Practitioner("DR1", "Sara", "GP")

    with pytest.raises(ValueError):
        Appointment(
            "A1", patient, doctor, datetime(2026, 10, 1, 9, 0, 1)
        )


def test_appointment_rejects_timezone():
    patient = Patient("P1", "Ahmed")
    doctor = Practitioner("DR1", "Sara", "GP")

    with pytest.raises(ValueError):
        Appointment(
            "A1", patient, doctor,
            datetime(2026, 10, 1, 9, tzinfo=timezone.utc)
        )


def test_completed_appointment_cannot_be_cancelled():
    patient = Patient("P1", "Ahmed")
    doctor = Practitioner("DR1", "Sara", "GP")
    appointment = Appointment(
        "A1", patient, doctor,
        datetime(2026, 10, 1, 9),
        AppointmentStatus.COMPLETED
    )

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status is AppointmentStatus.COMPLETED
