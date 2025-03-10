# Generated by Django 5.0.7 on 2024-07-26 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_width', models.BigIntegerField()),
                ('aspect_ratio', models.BigIntegerField()),
                ('rim_size', models.BigIntegerField()),
                ('vehicle_type', models.CharField()),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='car_app.car')),
            ],
        ),
    ]
