# Generated by Django 5.1.3 on 2024-11-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careproapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('doctors_name', models.CharField(max_length=100)),
                ('department_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('symptoms', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
