from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from clinic.users.models import Doctor, Patient
from clinic.utils.base import BaseViewSet, authenticate

from .serializers import (
    DoctorDetailSerializer,
    DoctorSerializer,
    PatientDetailSerializer,
    PatientSerializer,
)


class DoctorViewSet(BaseViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    search_fields = ["name", "email"]
    ordering_fields = ["name", "email"]
    ordering = ["name", "email"]

    http_method_names = ["get"]


class PatientViewSet(BaseViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    search_fields = ["name", "email"]
    ordering_fields = ["name", "email"]
    ordering = ["name", "email"]
    http_method_names = ["get"]


class UserDetailViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    search_fields = ["name", "email"]
    ordering_fields = ["name", "email"]
    ordering = ["name", "email"]

    http_method_names = ["get", "post", "put", "delete"]

    def auth(self, request, *args, **kwargs):
        user = authenticate(request)
        if not user:
            raise Response(status=401)

        return user

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        user = self.auth(request=request, *args, **kwargs)
        user = self.queryset.get(user__pk=user.pk)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = self.auth(request=request, *args, **kwargs)

        # user = self.queryset.get(user__pk=request.user.pk)
        user = get_object_or_404(self.queryset, user__pk=request.user.pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = self.auth(request=request, *args, **kwargs)

        if isinstance(request.user, AnonymousUser):
            return Response(status=401)
        # user = self.queryset.get(user__pk=request.user.pk)
        user = get_object_or_404(self.queryset, user__pk=request.user.pk)
        user.delete()
        return Response(status=204)


class DoctorDetailViewSet(UserDetailViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer


class PatientDetailViewSet(UserDetailViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer

    @action(detail=False, methods=["get"], url_path="doctors")
    def doctors(self, request, pk=None):
        user = self.auth(request=request)

        # patient = self.queryset.get(user__pk=request.user.pk)
        patient = get_object_or_404(self.queryset, user__pk=request.user.pk)
        doctors = patient.doctors.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="doctor")
    def doctor(self, request, pk=None):
        user = self.auth(request=request)

        # patient = self.queryset.get(user__pk=request.user.pk)
        patient = get_object_or_404(self.queryset, user__pk=request.user.pk)
        doctor = patient.doctors.get(pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
