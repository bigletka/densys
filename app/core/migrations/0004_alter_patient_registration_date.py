# Generated by Django 3.2.16 on 2022-11-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_patient_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='registration_date',
            field=models.DateTimeField(null=True),
        ),
    ]