import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService


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

