# Generated by Django 4.1 on 2022-12-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_doctor_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_photo',
            field=models.ImageField(default='static/image.profile.png', null=True, upload_to='static/images/'),
        ),
    ]