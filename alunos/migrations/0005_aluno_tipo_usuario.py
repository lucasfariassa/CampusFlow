# Generated by Django 4.2.7 on 2023-11-28 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0004_alter_aluno_curso_academico_alter_aluno_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='tipo_usuario',
            field=models.CharField(default='ALU', max_length=3),
        ),
    ]
