# Generated by Django 4.1.2 on 2022-10-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Dictaminador',
            fields=[
                ('DictaminadorID', models.AutoField(primary_key=True, serialize=False)),
                ('DictaminadorFullName', models.CharField(max_length=500)),
                ('DictaminadorCOD', models.CharField(max_length=500)),
                ('FechaN', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Egresado',
            fields=[
                ('EgresadoID', models.AutoField(primary_key=True, serialize=False)),
                ('EgresadoFullName', models.CharField(max_length=500)),
                ('EgresadoCOD', models.CharField(max_length=500)),
                ('FechaN', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=500)),
                ('Department', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=500)),
            ],
        ),
    ]
