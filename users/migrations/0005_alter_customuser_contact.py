# Generated by Django 5.1 on 2024-08-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_doctor_customuser_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contact',
            field=models.CharField(max_length=20),
        ),
    ]
