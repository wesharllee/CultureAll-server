# Generated by Django 4.1.1 on 2022-09-07 15:55

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
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('contact_by_phone', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CultUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('terms_signed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cult_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultureallapi.cultuser')),
                ('question_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultureallapi.questiontype')),
            ],
        ),
        migrations.AddField(
            model_name='questiontype',
            name='companies',
            field=models.ManyToManyField(related_name='question_types', through='cultureallapi.UserQuestionType', to='cultureallapi.cultuser'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=100)),
                ('question_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_type_id', to='cultureallapi.questiontype')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('in_person', models.BooleanField()),
                ('address', models.CharField(max_length=50)),
                ('cult_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='cultureallapi.cultuser')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cult_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='cultureallapi.cultuser')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='cultureallapi.question')),
            ],
        ),
    ]
