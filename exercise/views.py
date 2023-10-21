from rest_framework import generics
from .models import (
    Equipment,
    Goal,
    Displacement,
    PlacementPosition,
    Target,
    Organ,
)
from .serializers import (
    EquipmentSerializer,
    GoalSerializer,
    DisplacementSerializer,
    PlacementPositionSerializer,
    TargetSerializer,
    OrganSerializer,
)


class EquipmentListCreateView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    http_method_names = ["get"]


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    http_method_names = ["get"]


class GoalListCreateView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    http_method_names = ["get"]


class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    http_method_names = ["get"]


class DisplacementListCreateView(generics.ListCreateAPIView):
    queryset = Displacement.objects.all()
    serializer_class = DisplacementSerializer
    http_method_names = ["get"]


class DisplacementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Displacement.objects.all()
    serializer_class = DisplacementSerializer
    http_method_names = ["get"]


class PlacementPositionListCreateView(generics.ListCreateAPIView):
    queryset = PlacementPosition.objects.all()
    serializer_class = PlacementPositionSerializer
    http_method_names = ["get"]


class PlacementPositionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlacementPosition.objects.all()
    serializer_class = PlacementPositionSerializer
    http_method_names = ["get"]


class TargetListCreateView(generics.ListCreateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    http_method_names = ["get"]


class TargetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    http_method_names = ["get"]


class OrganListCreateView(generics.ListCreateAPIView):
    queryset = Organ.objects.all()
    serializer_class = OrganSerializer
    http_method_names = ["get"]


class OrganDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organ.objects.all()
    serializer_class = OrganSerializer
    http_method_names = ["get"]
