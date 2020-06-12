from rest_framework import serializers

from rest_framework.renderers import JSONRenderer

from rest_framework.parsers import JSONParser

import io

class Employee(object):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired,
                 is_best_employee=None, last_name=None):
        self.employee_id = employee_id                  # UUID
        self.age = age                                  # INT
        self.date_of_joining = date_of_joining          # DATE
        self.last_logged_in = last_logged_in            # DATETIME
        self.salary_in_inr = salary_in_inr              # FLOAT
        self.employee_type = employee_type              # ENUM - Possible values MANAGER,TECHNICIAN,DEVELOPER,SALES_MEMBER
        self.first_name = first_name                    # CHAR
        self.last_name = last_name                      # CHAR
        self.is_retired = is_retired                    # BOOL
        self.is_best_employee = is_best_employee        # BOOL - Can be None as well



class Company(object):
    def __init__(self, name, registration_id):
        self.name = name                                # CHAR
        self.registration_id = registration_id          # UUID


class EmployeeWithCompanyDetails(Employee):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired, company,
                 is_best_employee=None, last_name=None):
        super().__init__(employee_id, age, date_of_joining, last_logged_in,
                         salary_in_inr, employee_type, first_name, is_retired,
                         is_best_employee, last_name)
        self.company = company                          # Company class instance

class CompanyWithEmployeesDetails(Company):
    def __init__(self, name, registration_id, employees):
        super().__init__(name, registration_id)
        self.employees = employees        # List of Employee class instances
        

from .constants import *

class EmployeeSerializer(serializers.Serializer):
    employee_id = serializers.UUIDField()
    age = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    last_logged_in = serializers.DateTimeField()
    salary_in_inr = serializers.FloatField()
    employee_type = serializers.ChoiceField(choices=EMPLOYEES_TYPE)
    first_name = serializers.CharField()
    last_name = serializers.CharField(allow_null=True, required=False)
    is_retired = serializers.BooleanField()
    is_best_employee = serializers.NullBooleanField(required=False)
    
    def create(self, validated_data):
         return Employee(**validated_data)
    

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    registration_id = serializers.UUIDField()
    
    def create(self, validated_data):
         return Company(**validated_data)
    

class EmployeeWithCompanyDetailsSerializer(EmployeeSerializer):
    company = CompanySerializer()
    
    def create(self, validated_data):
        company_data=validated_data.pop("company")
        company=Company(**company_data)
        employee_with_company_object=EmployeeWithCompanyDetails(company=company, **validated_data)
        return employee_with_company_object


class CompanyWithEmployeeDetailsSerializer(CompanySerializer):
    employees = EmployeeSerializer(many=True)

    def create(self, validated_data):
        employees_data = validated_data.pop('employees')
        employees = [Employee(**item) for item in employees_data]
        company_employee = CompanyWithEmployeesDetails(employees=employees, **validated_data)
        
        return company_employee


def serialize_employee_object(employee_object):
    serializer = EmployeeSerializer(employee_object)
    json_data = serializer.data
    return json_data
    
def deserialize_data_to_employee_object(employee_data):
    #json_data = employee_data 
    #stream = io.BytesIO(json_data)
    #data = JSONParser().parse(stream)
    serializer = EmployeeSerializer(data=employee_data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        instance = serializer.save()
        return instance
    return serializer.errors
        
def serialize_list_of_employee_objects(list_of_employee_objects):
    serializer = EmployeeSerializer(list_of_employee_objects, many=True)
    json_data = serializer.data
    return json_data
    
def deserialize_data_to_list_of_employee_objects(employees_data):
    serializer = EmployeeSerializer(data=employees_data, many=True)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        instance = serializer.save()
        return instance
    return serializer.errors

def serialize_employee_with_company_object(employee_with_company_object):
    serializer = EmployeeWithCompanyDetailsSerializer(employee_with_company_object)
    json_data = serializer.data
    return json_data
    
def deserialize_data_to_employee_with_company_object(employee_with_company_data):
    serializer = EmployeeWithCompanyDetailsSerializer(data=employee_with_company_data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        instance = serializer.save()
        return instance
    return serializer.errors
    
def serialize_company_with_employees_object(company_with_employees_object):
    serializer = CompanyWithEmployeeDetailsSerializer(company_with_employees_object)
    json_data = serializer.data
    return json_data

def deserialize_data_to_company_with_employees_object(company_with_employees_data):
    serializer = CompanyWithEmployeeDetailsSerializer(data=company_with_employees_data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        instance = serializer.save()
        return instance
    return serializer.errors
