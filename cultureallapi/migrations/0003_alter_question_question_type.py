# Generated by Django 4.1.1 on 2022-09-08 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cultureallapi', '0002_answer_rating_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultureallapi.questiontype'),
        ),
    ]