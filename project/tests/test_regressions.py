
import pytest
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService, AppointmentService


def test_f8_01_same_practitioner_double_booking():
    store = SmartCareDataStore()

    PatientService(store).register_patient("P1", "Ahmed")
    PractitionerService(store).register_practitioner("DR1", "Sara", "GP")

    appointments = AppointmentService(store)
    booking_time = datetime(2026, 11, 5, 10, 0)

    appointments.book_appointment("A1", "P1", "DR1", booking_time)

    with pytest.raises(ValueError):
        appointments.book_appointment("A2", "P1", "DR1", booking_time)


def test_f8_02_cancelled_appointment_still_retrievable():
    store = SmartCareDataStore()

    PatientService(store).register_patient("P1", "Ahmed")
    PractitionerService(store).register_practitioner("DR1", "Sara", "GP")

    appointments = AppointmentService(store)

    original = appointments.book_appointment(
        "A1", "P1", "DR1", datetime(2026, 11, 5, 10, 0)
    )

    appointments.cancel_appointment("A1")

    assert store.find_appointment("A1") is original
    assert appointments.find_appointment("A1") is original
