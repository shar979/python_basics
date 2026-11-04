from mimetypes import init


class Employee:
    def __init__(self,name, email, department, salary):
        self.name= name
        self.email =email
        self.department= department
        self.salary = salary
    def show_details(self):
        print(self.name, self.email, self.department)

              #  inheritance
class PermanentEmployee(Employee):
    def __init__(self, name, email, department, salary,cover,increment):
        super().__init__(name, email, department, salary)
        self.cover = cover
        self.increment = increment

class ContractEmployee(Employee):
    def __init__(self, name, email, department, salary, tenure):
        super().__init__(name, email, department, salary)
        self.tenure= tenure


p1= PermanentEmployee("Mary Jane", "dhfj@gmail.com", "HR",100_000, "Britam", 3)
c1 = ContractEmployee("Hoerut Mil", "gg@gmail.com", "Sales", 34_900,2)

p1.show_details()
