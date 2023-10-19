from rest_framework import generics
from .models import (
    Equipment,
    Goal,
    Displacement,
    PlacementPosition,
    Target,
    Organ,
    Exercise,
)
from .serializers import (
    EquipmentSerializer,
    GoalSerializer,
    DisplacementSerializer,
    PlacementPositionSerializer,
    TargetSerializer,
    OrganSerializer,
    ExerciseSerializer,
)


class EquipmentListCreateView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class GoalListCreateView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class DisplacementListCreateView(generics.ListCreateAPIView):
    queryset = Displacement.objects.all()
    serializer_class = DisplacementSerializer


class DisplacementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Displacement.objects.all()
    serializer_class = DisplacementSerializer


class PlacementPositionListCreateView(generics.ListCreateAPIView):
    queryset = PlacementPosition.objects.all()
    serializer_class = PlacementPositionSerializer


class PlacementPositionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlacementPosition.objects.all()
    serializer_class = PlacementPositionSerializer


class TargetListCreateView(generics.ListCreateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class TargetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class OrganListCreateView(generics.ListCreateAPIView):
    queryset = Organ.objects.all()
    serializer_class = OrganSerializer


class OrganDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organ.objects.all()
    serializer_class = OrganSerializer


class ExerciseListCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
