from clinic.utils.base import ROUTER

from .views import (
    DoctorDetailViewSet,
    DoctorViewSet,
    PatientDetailViewSet,
    PatientViewSet,
)

router = ROUTER()

router.register(r"doctors", DoctorViewSet, basename="doctors")
router.register(r"patients", PatientViewSet, basename="patients")
router.register(r"doctor", DoctorDetailViewSet, basename="doctor")
router.register(r"patient", PatientDetailViewSet, basename="patient")
