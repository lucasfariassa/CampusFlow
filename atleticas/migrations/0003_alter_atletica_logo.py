# Generated by Django 4.2.7 on 2023-11-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atleticas', '0002_atletica_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atletica',
            name='logo',
            field=models.ImageField(upload_to='static/images/logos_atleticas'),
        ),
    ]