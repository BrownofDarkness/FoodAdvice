from abc import ABC

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import fields
from rest_framework.serializers import ValidationError
from .models import Client, Restaurant, Localisation, Carte, Plat, Like, Reservation, ReservedPlate, FavMenu, FavMenuPlate

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
            },
            'email': {
                'required': True,
            },
            'username': {
                'required': True,
            },
        }


class LoginSerializer(serializers.Serializer):
    username = fields.CharField(required=True, max_length=120, help_text='User\'s username')
    password = fields.CharField(required=True, max_length=120, help_text='User\'s password')


class ClientSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ['id', 'user', 'birthday', 'phone', 'disease', 'image']
        extra_kwargs = {
            'phone': {
                'required': True,
            },
            'birthday': {
                'required': True,
            },

        }

    def create(self, validated_data):

        usr = validated_data.pop('user')
        print(usr)
        serializer = UserSerializer(data=usr)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.create(usr)
        print(user_instance.password)
        validated_data['user'] = user_instance

        client = Client(**validated_data)
        client.user = user_instance
        client.save()

        return client


class LocalisationSerializer(serializers.Serializer):

    class Meta:
        model = Localisation

        fields = '__all__'


class RestaurantSerializer(serializers.Serializer):
    localistion = LocalisationSerializer()

    class Meta:
        model = Restaurant
        fields = ['id', 'user', 'name', 'localisation', 'phone_1', 'phone_1', 'image']

    def create(self, validated_data):
        user = validated_data.pop('user')
        print(user)
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.create(user)
        print(user_instance.password)
        validated_data['user'] = user_instance

        resto = Restaurant(**validated_data)
        resto.user = user_instance
        resto.save()

        return resto


class CarteSerializer(serializers.Serializer):

    class Meta:
        model = Carte
        fields = '__all__'


class PlateSerializer(serializers.Serializer):

    class Meta:
        model = Plat
        fields = '__all__'


class LikeSerializer(serializers.Serializer):

    class Meta:
        model = Like
        fields = '__all__'


class ReservationSerializer(serializers.Serializer):

    class Meta:
        model = Reservation
        fields = '__all__'

    def create(self, validated_data):

        plats = validated_data.pop('plate')
        print(plats)
        """serializer = UserSerializer(data=usr)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.create(usr)
        print(user_instance.password)
        validated_data['user'] = user_instance

        client = Client(**validated_data)
        client.user = user_instance
        client.save()

        return client"""


class FavMenuSerializer(serializers.Serializer):

    class Meta:
        model = FavMenu
        fields = '__all__'

    def create(self, validated_data):

        plats = validated_data.pop('plate')
        print(plats)
        """serializer = UserSerializer(data=usr)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.create(usr)
        print(user_instance.password)
        validated_data['user'] = user_instance

        client = Client(**validated_data)
        client.user = user_instance
        client.save()

        return client"""