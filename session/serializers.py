from rest_framework import serializers
from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Session model.
    """

    class Meta:
        model = Session
        fields = "__all__"
