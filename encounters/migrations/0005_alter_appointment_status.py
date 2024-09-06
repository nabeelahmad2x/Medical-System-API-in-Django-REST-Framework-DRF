# Generated by Django 5.1 on 2024-09-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encounters', '0004_alter_appointment_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Missed', 'Missed')], max_length=20),
        ),
    ]
