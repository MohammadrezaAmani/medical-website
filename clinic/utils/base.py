from django.conf import settings
from rest_framework import status

# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination

# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class BaseViewSet(ReadOnlyModelViewSet):
    authentication_classes = []
    # authentication_classes = [
    #     JWTAuthentication,
    #     SessionAuthentication,
    #     BasicAuthentication,
    # ]
    # permission_classes = [IsAuthenticated]
    permission_classes = []
    # filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = LimitOffsetPagination
    search_fields = None
    ordering_fields = None
    ordering = None

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BaseSerializer(ModelSerializer):
    ...


ROUTER = DefaultRouter if settings.DEBUG else SimpleRouter


def authenticate(request, raise_exception=True):
    try:
        jwt = JWTAuthentication()
        token = (
            request.headers["Authorization"].split(" ")[0]
            if "Authorization" in request.headers
            else None
        )
        user = jwt.get_user(jwt.get_validated_token(token))
        return user
    except Exception as e:
        if raise_exception:
            raise InvalidToken(e)
        return None
