# Generated by Django 4.1 on 2022-12-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_doctor_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_photo',
            field=models.ImageField(default='static/images/profile.png', null=True, upload_to='static/images/'),
        ),
    ]