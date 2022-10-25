from rest_framework import serializers
from EmployeeApp.models import Departments, Dictaminador, Egresado,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Egresado
        fields=('EgresadoId','EgresadoFullName','EgresadoCOD','FechaN','PhotoFileName')
        
class DictaminadorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dictaminador 
        fields=('EgresadoId','EgresadoFullName','EgresadoCOD','FechaN','PhotoFileName')