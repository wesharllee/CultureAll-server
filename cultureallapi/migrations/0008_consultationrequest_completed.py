# Generated by Django 4.1.1 on 2022-09-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultureallapi', '0007_rename_complete_contactrequest_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationrequest',
            name='completed',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]
