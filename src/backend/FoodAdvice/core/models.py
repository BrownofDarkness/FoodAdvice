from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    birthday = models.DateField()
    phone = models.IntegerField()
    disease = models.CharField(max_length=200)
    image = models.ImageField(upload_to='client/')


class Localisation(models.Model):
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)


class Restaurant(models.Model):
    user = models.OneToOneField(User, related_name='resto')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='resto/')
    phone_1 = models.IntegerField()
    phone_2 = models.IntegerField()
    localisation = models.OneToOneField(Localisation)


class Carte(models.Model):
    resto = models.OneToOneField(Restaurant, related_name="carte")
    intitule = models.CharField(max_length=200)


class Plat(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='plats/')
    carte = models.OneToOneField(Carte, related_name='plats')


class Like(models.Model):
    client = models.ForeignKey(Client, related_name='liked')
    plat = models.ForeignKey(Plat, related_name='likes')


class Reservation(models.Model):
    client = models.ForeignKey(Client, related_name="reservations")
    resto = models.ForeignKey(Restaurant, related_name="reserves")
    reserved_for = models.DateTimeField()
    places = models.IntegerField()


class ReservedPlate(models.Model):
    reservation = models.ForeignKey(Reservation, related_name="plates")
    plat = models.ForeignKey(Plat)



