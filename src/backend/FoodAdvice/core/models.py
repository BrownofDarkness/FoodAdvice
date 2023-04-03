from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birthday = models.DateField()
    phone = models.IntegerField()
    disease = models.CharField(max_length=200)
    image = models.ImageField(upload_to='client/')


class Localisation(models.Model):
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)


class Restaurant(models.Model):
    user = models.OneToOneField(User, related_name='resto', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='resto/')
    phone_1 = models.IntegerField()
    phone_2 = models.IntegerField()
    localisation = models.OneToOneField(Localisation, on_delete=models.CASCADE)


class Carte(models.Model):
    resto = models.OneToOneField(Restaurant, related_name="carte", on_delete=models.CASCADE)
    intitule = models.CharField(max_length=200)


class Plat(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='plats/')
    carte = models.OneToOneField(Carte, related_name='plats', on_delete=models.CASCADE)


class Like(models.Model):
    client = models.ForeignKey(Client, related_name='liked', on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, related_name='likes', on_delete=models.CASCADE)


class Reservation(models.Model):
    client = models.ForeignKey(Client, related_name="reservations", on_delete=models.CASCADE)
    resto = models.ForeignKey(Restaurant, related_name="reserves", on_delete=models.CASCADE)
    reserved_for = models.DateTimeField()
    places = models.IntegerField()


class ReservedPlate(models.Model):
    reservation = models.ForeignKey(Reservation, related_name="plates", on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)


class FavMenu(models.Model):
    title = models.CharField(max_length=200)


class FavMenuPlate(models.Model):
    favMenu = models.ForeignKey(FavMenu, related_name="plats", on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)



