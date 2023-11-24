# Generated by Django 4.2.7 on 2023-11-15 03:41

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
            name='Aluno',
            fields=[
                ('matricula', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=100)),
                ('curso_academico', models.CharField(max_length=3)),
                ('status_monitor', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Aluno(a)',
                'verbose_name_plural': 'Alunos',
            },
        ),
    ]