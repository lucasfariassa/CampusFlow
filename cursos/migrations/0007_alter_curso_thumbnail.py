# Generated by Django 4.2.7 on 2023-11-29 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_curso_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='thumbnail',
            field=models.ImageField(default='static/images/global/thumb_curso_default.png', upload_to='static/images/thumbs_cursos'),
        ),
    ]
