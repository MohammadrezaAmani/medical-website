from rest_framework import serializers

from clinic.users.models import CustomUser, Doctor, PateintDoctor, Patient
from clinic.utils.base import BaseSerializer


class CustomUserSerializer(BaseSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "is_active",
            "photo",
            "birth_date",
            "bio",
            "address",
            "username",
        ]


class CustomUserDetailSerializer(BaseSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        exclude = [
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "last_login",
            "groups",
            "user_permissions",
            "is_verified",
        ]


class DoctorSerializer(BaseSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(BaseSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Patient
        fields = "__all__"


class DoctorDetailSerializer(BaseSerializer):
    user = CustomUserDetailSerializer()

    class Meta:
        model = Doctor
        fields = "__all__"


class PatientDetailSerializer(BaseSerializer):
    user = CustomUserDetailSerializer()

    class Meta:
        model = Patient
        fields = "__all__"


class PatientDoctorSerializer(BaseSerializer):
    class Meta:
        model = PateintDoctor
        fields = "__all__"
