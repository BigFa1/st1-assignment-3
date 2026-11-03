import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService
from datetime import datetime
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import PractitionerService, AppointmentService

def test_find_existing_patient():
    store = SmartCareDataStore()
    service = PatientService(store)
    patient = service.register_patient('P1', 'Ahmed')

    assert service.find_patient('P1') is patient

def test_find_patient_with_spaces():
    store = SmartCareDataStore()
    service = PatientService(store)
    patient = service.register_patient('P1', 'Ahmed')

    assert service.find_patient(' P1 ') is patient


def test_find_unknown_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(LookupError):
        service.find_patient('P99')


def test_find_invalid_patient_id():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(ValueError):
        service.find_patient('')


def test_find_patient_case_sensitive():
    store = SmartCareDataStore()
    service = PatientService(store)
    service.register_patient('P1', 'Ahmed')

    with pytest.raises(LookupError):
        service.find_patient('p1')

def test_find_practitioner_success():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    doctor = service.register_practitioner("DR1", "Sara", "GP")
    assert service.find_practitioner(" DR1 ") is doctor


def test_find_practitioner_errors():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    service.register_practitioner("DR1", "Sara", "GP")

    with pytest.raises(LookupError):
        service.find_practitioner("DR99")

    with pytest.raises(LookupError):
        service.find_practitioner("dr1")

    with pytest.raises(ValueError):
        service.find_practitioner("")


def test_cancel_appointment_success():
    store = SmartCareDataStore()
    PatientService(store).register_patient("P1", "Ahmed")
    PractitionerService(store).register_practitioner("DR1", "Sara", "GP")

    service = AppointmentService(store)
    appointment = service.book_appointment(
        "A1", "P1", "DR1", datetime(2026, 11, 5, 10, 0)
    )

    result = service.cancel_appointment(" A1 ")

    assert result is appointment
    assert appointment.status is AppointmentStatus.CANCELLED
    assert service.find_appointment("A1") is appointment

    with pytest.raises(ValueError):
        service.cancel_appointment("A1")


def test_cancel_appointment_errors():
    store = SmartCareDataStore()
    service = AppointmentService(store)

    with pytest.raises(LookupError):
        service.cancel_appointment("A99")

    with pytest.raises(ValueError):
        service.cancel_appointment("")
