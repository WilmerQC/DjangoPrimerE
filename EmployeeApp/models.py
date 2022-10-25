from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

class Egresado(models.Model):
    EgresadoID = models.AutoField(primary_key=True)
    EgresadoFullName = models.CharField(max_length=500)
    EgresadoCOD = models.CharField(max_length=500)
    FechaN = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

class Dictaminador(models.Model):
    DictaminadorID = models.AutoField(primary_key=True)
    DictaminadorFullName = models.CharField(max_length=500)
    DictaminadorCOD = models.CharField(max_length=500)
    FechaN = models.DateField()
    PhotoFileName = models.CharField(max_length=500)