# Generated by Django 4.1.1 on 2022-09-07 19:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultureallapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='rating_value',
            field=models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
