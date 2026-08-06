
from dataclasses import dataclass
@dataclass
class Employee:
    employee_id: int
    name: str
    role: str
    salary: float
    
employees = [
    Employee(1,"Anas","Developer",100000),
    Employee(2,"Alyan","")
]