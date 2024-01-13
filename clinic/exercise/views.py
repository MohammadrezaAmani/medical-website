from rest_framework import generics
from utils.auth import get_doctor_from_token

from .models import (
    Displacement,
    Equipment,
    Exercise,
    Goal,
    Organ,
    PlacementPosition,
    Target,
)
from .serializers import (
    DisplacementSerializer,
    EquipmentSerializer,
    ExerciseSerializer,
    GoalSerializer,
    OrganSerializer,
    PlacementPositionSerializer,
    TargetSerializer,
)


class EquipmentListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating Equipment objects.
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    http_method_names = ["get"]

    # def get_queryset(self,request):
    #     patient = get_patient_from_token(request)
    #     doctor = get_doctor_from_token(request)
    #     if not (patient or doctor):
    #         return Response({
    #             'bad':'not logged in'
    #         })
    #     return


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a single Equipment object.
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    http_method_names = ["get"]


class GoalListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating Goal objects.
    """

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    http_method_names = ["get"]


class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a single Goal object.
    """

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    http_method_names = ["get"]


class DisplacementListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating Displacement objects.
    """

    queryset = Displacement.objects.all()
    serializer_class = DisplacementSerializer
    http_method_names = ["get"]


class DisplacementDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a single Displacement object.
    """

    queryset = Displacement.objects.all()
    serializer_class = DisplacementSerializer
    http_method_names = ["get"]


class PlacementPositionListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating PlacementPosition objects.
    """

    queryset = PlacementPosition.objects.all()
    serializer_class = PlacementPositionSerializer
    http_method_names = ["get"]


class PlacementPositionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a single PlacementPosition object.
    """

    queryset = PlacementPosition.objects.all()
    serializer_class = PlacementPositionSerializer
    http_method_names = ["get"]


class TargetListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating Target objects.
    """

    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    http_method_names = ["get"]


class TargetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a single Target object.
    """

    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    http_method_names = ["get"]


class OrganListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating Organ objects.
    """

    queryset = Organ.objects.all()
    serializer_class = OrganSerializer
    http_method_names = ["get"]


class OrganDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a single Organ object.
    """

    queryset = Organ.objects.all()
    serializer_class = OrganSerializer
    http_method_names = ["get"]


class ExerciseListView(generics.ListCreateAPIView):
    """
    View for listing and creating Exercise objects.
    """

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        """
        Return a queryset of Exercise objects that are public if the user is not authenticated,
        otherwise return a queryset of all Exercise objects.
        """
        doctor = get_doctor_from_token(self.request)
        if doctor:
            return Exercise.objects.all()
        return Exercise.objects.filter(is_public=True)
