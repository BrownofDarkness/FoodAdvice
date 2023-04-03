# Generated by Django 3.2 on 2023-04-03 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('phone', models.IntegerField()),
                ('disease', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='client/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='plats/')),
                ('carte', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plats', to='core.carte')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved_for', models.DateTimeField()),
                ('places', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='resto/')),
                ('phone_1', models.IntegerField()),
                ('phone_2', models.IntegerField()),
                ('localisation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.localisation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReservedPlate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plat')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plates', to='core.reservation')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='resto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserves', to='core.restaurant'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='core.client')),
                ('plat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.plat')),
            ],
        ),
        migrations.AddField(
            model_name='carte',
            name='resto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carte', to='core.restaurant'),
        ),
    ]