from enum import Enum

class Employee_type_enums(Enum):
    manager = "MANAGER"
    technician = "TECHNICIAN"
    developer = "DEVELOPER"
    sales_member = "SALES_MEMBER"

EMPLOYEES_TYPE = [i.value for i in Employee_type_enums]
