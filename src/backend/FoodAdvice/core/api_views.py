from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin,
                                   RetrieveModelMixin)
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model, authenticate, logout
from rest_framework import status
from django.http import JsonResponse, request
from rest_framework.authtoken.models import Token

from .models import Client, Restaurant
from .serializers import LoginSerializer, ClientSerializer,RestaurantSerializer

User = get_user_model()


class LoginViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token = user.auth_token.key
            context = {
                'Token': token,
            }
            return Response(context)
        else:
            return Response({'detail': 'username or password invalid'}, status=status.HTTP_400_BAD_REQUEST)


# @method_decorator(swagger_auto_schema(
#     request_body=ClientSerializer()
# ), 'create')
class ClientViewSet(CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return ClientSerializer

    def get_queryset(self):
        user = self.request.user
        if user:
            print(user)
            queryset = Client.objects.filter(user=user.id)
        else:
            queryset = "you must be authenticated"
            print("not found")
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(ClientSerializer(instance).data, status=201)

    def update(self, request, *args, **kwargs):
        instance: Client = self.get_object()
        user = self.get_user()
        if instance.user == user:
            return super().update(request, *args, **kwargs)
        return JsonResponse({'detail': 'you are nor allow to update this client_profile'})

    def partial_update(self, request, *args, **kwargs):
        instance: Client = self.get_object()
        user = self.get_user()
        if instance.user == user:
            return super().partial_update(request, *args, **kwargs)
        return Response({'detail': 'you are not allow to update this client_profile'})


class RestaurantViewSet(CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return RestaurantSerializer

    def get_queryset(self):
        user = self.request.user
        if user:
            print(user)
            queryset = Restaurant.objects.filter(user=user.id)
        else:
            queryset = "you must be authenticated"
            print("not found")
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(ClientSerializer(instance).data, status=201)

    def update(self, request, *args, **kwargs):
        instance: Client = self.get_object()
        user = self.get_user()
        if instance.user == user:
            return super().update(request, *args, **kwargs)
        return JsonResponse({'detail': 'you are nor allow to update this restaurant_profile'})

    def partial_update(self, request, *args, **kwargs):
        instance: Client = self.get_object()
        user = self.get_user()
        if instance.user == user:
            return super().partial_update(request, *args, **kwargs)
        return Response({'detail': 'you are not allow to update this restaurant_profile'})
