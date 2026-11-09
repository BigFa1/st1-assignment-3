from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    PatientService,
    PractitionerService,
    AppointmentService,
)


def test_complete_appointment_workflow():
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patient = patients.register_patient("P1", "Ahmed")
    d1 = practitioners.register_practitioner("D1", "Sara", "GP")
    d2 = practitioners.register_practitioner("D2", "Omar", "Cardiology")

    assert patients.find_patient("P1") is patient
    assert practitioners.find_practitioner("D1") is d1
    assert practitioners.find_practitioner("D2") is d2

    booking_time = datetime(2026, 11, 19, 8, 0)

    a1 = appointments.book_appointment(
        "A1", "P1", "D1", booking_time
    )

    original_records = list(store.list_appointments())

    # Same practitioner and time must be rejected.
    with pytest.raises(ValueError):
        appointments.book_appointment(
            "A3", "P1", "D1", booking_time
        )

    assert store.list_appointments() == original_records
    assert store.find_appointment("A3") is None

    # Another practitioner can use the same time.
    a2 = appointments.book_appointment(
        "A2", "P1", "D2", booking_time
    )

    assert a2.practitioner is d2

    # Cancellation must keep the original appointment.
    appointments.cancel_appointment("A1")

    assert appointments.find_appointment("A1") is a1
    assert a1.status is AppointmentStatus.CANCELLED

    assert a1 in appointments.list_practitioner_appointments("D1")

    assert appointments.list_practitioner_appointments(
        "D1", AppointmentStatus.SCHEDULED
    ) == []

    with pytest.raises(ValueError):
        appointments.cancel_appointment("A1")

    # The cancelled slot can be booked again.
    a3 = appointments.book_appointment(
        "A3", "P1", "D1", booking_time
    )

    assert a3.status is AppointmentStatus.SCHEDULED

    assert appointments.list_practitioner_appointments(
        "D1", AppointmentStatus.SCHEDULED
    ) == [a3]

    assert appointments.list_practitioner_appointments(
        "D1", AppointmentStatus.CANCELLED
    ) == [a1]


def test_invalid_requests_preserve_records():
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patient = patients.register_patient("P1", "Ahmed")
    practitioners.register_practitioner("D1", "Sara", "GP")

    booking_time = datetime(2026, 11, 19, 9, 0)

    with pytest.raises(ValueError):
        patients.register_patient("P1", "Another Name")

    with pytest.raises(LookupError):
        appointments.book_appointment(
            "A4", "P99", "D1", booking_time
        )

    with pytest.raises(ValueError):
        appointments.book_appointment(
            "", "P1", "D1", booking_time
        )

    with pytest.raises(ValueError):
        appointments.list_practitioner_appointments(
            "D1", "scheduled"
        )

    with pytest.raises(LookupError):
        appointments.list_practitioner_appointments("D99")

    assert store.list_appointments() == []
    assert patients.find_patient("P1") is patient

    # A failed attempt must not reserve the appointment ID.
    a4 = appointments.book_appointment(
        "A4", "P1", "D1", booking_time
    )

    assert appointments.find_appointment("A4") is a4