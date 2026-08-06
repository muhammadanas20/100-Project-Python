
from dataclasses import dataclass
@dataclass
class Employee:
    employee_id: int
    name: str
    role: str
    salary: float
    
employees = [
    Employee(1,"Anas","Developer",100000),
    Employee(2,"Alyan","Designer",80000),
]
target = int(input(("Employee ID to update: ")))
employee = next((e for e in employees if e.employee_id == target),None)

if employee:
    employee.salary = float(input("New salary:"))
for employee in employees:
    print(employee)
                