# Generated by Django 4.2.7 on 2023-11-29 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_alter_curso_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='static/images/thumbs_cursos'),
        ),
    ]
