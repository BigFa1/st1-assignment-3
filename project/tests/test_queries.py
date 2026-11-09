from datetime import datetime

import smartcare.queries as queries
from smartcare.domain import Appointment, AppointmentStatus, Patient, Practitioner
from smartcare.queries import appointment_sort_key, select_appointments


def make_appointments():
    patient = Patient("P1", "Ahmed")
    d1 = Practitioner("D1", "Sara", "GP")
    d2 = Practitioner("D2", "Omar", "Cardiology")

    a3 = Appointment("A3", patient, d1, datetime(2026, 10, 1, 10, 0),
                     AppointmentStatus.CANCELLED)
    a4 = Appointment("A4", patient, d2, datetime(2026, 10, 1, 8, 0))
    a1 = Appointment("A1", patient, d1, datetime(2026, 10, 1, 10, 0),
                     AppointmentStatus.COMPLETED)
    a2 = Appointment("A2", patient, d1, datetime(2026, 10, 1, 9, 0))

    return [a3, a4, a1, a2]


def test_named_sort_key():
    appointments = make_appointments()
    assert appointment_sort_key(appointments[0]) == (
        datetime(2026, 10, 1, 10, 0), "A3"
    )


def test_practitioner_filter_and_order():
    appointments = make_appointments()
    result = select_appointments(appointments, "D1")

    assert [a.appointment_id for a in result] == ["A2", "A1", "A3"]
    assert [a.appointment_id for a in select_appointments(appointments, "D2")] == ["A4"]


def test_status_filters():
    appointments = make_appointments()

    expected = [
        (AppointmentStatus.SCHEDULED, "A2"),
        (AppointmentStatus.CANCELLED, "A3"),
        (AppointmentStatus.COMPLETED, "A1"),
    ]

    for status, expected_id in expected:
        result = select_appointments(appointments, "D1", status)
        assert [a.appointment_id for a in result] == [expected_id]

    assert select_appointments(appointments, "D99") == []


def test_new_list_and_no_mutation():
    appointments = make_appointments()
    original_order = list(appointments)
    original_fields = [
        (a.appointment_id, a.date_time, a.status)
        for a in appointments
    ]

    first = select_appointments(appointments, "D1")
    second = select_appointments(appointments, "D1")

    assert first is not appointments
    assert first is not second
    assert first == second
    assert first[0] is appointments[3]
    assert appointments == original_order
    assert [
        (a.appointment_id, a.date_time, a.status)
        for a in appointments
    ] == original_fields

    empty = []
    assert select_appointments(empty, "D1") is not empty

    already_sorted = [appointments[3]]
    assert select_appointments(already_sorted, "D1") is not already_sorted


def test_query_reuses_named_key(monkeypatch):
    appointments = make_appointments()
    called = []

    def tracking_key(appointment):
        called.append(appointment.appointment_id)
        return appointment.date_time, appointment.appointment_id

    monkeypatch.setattr(queries, "appointment_sort_key", tracking_key)

    queries.select_appointments(appointments, "D1")

    assert set(called) == {"A1", "A2", "A3"}

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def test_service_listing_empty_and_errors():
    store = SmartCareDataStore()
    practitioners = PractitionerService(store)
    service = AppointmentService(store)

    practitioners.register_practitioner("D1", "Sara", "GP")

    first = service.list_practitioner_appointments("D1")
    second = service.list_practitioner_appointments("D1")
    assert first == []
    assert second == []
    assert first is not second

    with pytest.raises(LookupError):
        service.list_practitioner_appointments("D99")

    with pytest.raises(ValueError):
        service.list_practitioner_appointments("")

    with pytest.raises(ValueError):
        service.list_practitioner_appointments("D1", "scheduled")


def test_service_listing_after_cancellation():
    store = SmartCareDataStore()
    PatientService(store).register_patient("P1", "Ahmed")

    practitioners = PractitionerService(store)
    practitioners.register_practitioner("D1", "Sara", "GP")
    practitioners.register_practitioner("D2", "Omar", "Cardiology")

    service = AppointmentService(store)
    booking_time = datetime(2026, 10, 1, 9, 0)

    a1 = service.book_appointment("A1", "P1", "D1", booking_time)
    a2 = service.book_appointment("A2", "P1", "D2", booking_time)

    service.cancel_appointment("A1")

    assert service.list_practitioner_appointments(" D1 ")[0] is a1
    assert service.list_practitioner_appointments(
        "D1", AppointmentStatus.CANCELLED
    ) == [a1]

    assert service.list_practitioner_appointments(
        "D1", AppointmentStatus.SCHEDULED
    ) == []

    assert service.list_practitioner_appointments("D2") == [a2]
    assert service.find_appointment("A1") is a1
    assert a1.status is AppointmentStatus.CANCELLED