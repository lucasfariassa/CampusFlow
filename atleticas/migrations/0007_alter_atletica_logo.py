# Generated by Django 4.2.7 on 2023-11-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atleticas', '0006_alter_atletica_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atletica',
            name='logo',
            field=models.ImageField(default='static/images/global/logo_atletica_default.png', upload_to='static/images/logos_atleticas'),
        ),
    ]
