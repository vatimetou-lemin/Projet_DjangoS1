# Generated by Django 4.1.7 on 2023-02-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applic', '0003_voiture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='image',
            field=models.ImageField(blank=True, upload_to='imgs/'),
        ),
    ]
