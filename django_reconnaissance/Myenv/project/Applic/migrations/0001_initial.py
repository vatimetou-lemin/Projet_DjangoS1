# Generated by Django 4.1.7 on 2023-02-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propriete',
            fields=[
                ('NNI', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Prenom', models.CharField(max_length=50)),
                ('Nom', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('plaque', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('marque', models.CharField(max_length=15)),
                ('genre', models.CharField(max_length=15)),
                ('couleur', models.CharField(max_length=10)),
            ],
        ),
    ]