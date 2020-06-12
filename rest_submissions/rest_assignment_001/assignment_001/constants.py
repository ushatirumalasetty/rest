from enum import Enum

class Employee_type_enums(Enum):
    MANAGER = "MANAGER"
    TECHNICIAN = "TECHNICIAN"
    DEVELOPER = "DEVELOPER"
    SALES_MEMBER = "SALES_MEMBER"

EMPLOYEES_TYPE = [(i.name,i.value) for i in Employee_type_enums]
