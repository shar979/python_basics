class School:
    def __init__(self, name, country):
        self.name = name
        self.country= country
    def print_details(self):
        print(self.name)
        print(self.country)
class Student(School):
    def __init__(self, name, country,admission, form):
        super().__init__(name, country)
        self.admission = admission
        self.form= form

class Teacher(School):
    def __init__(self, name, country, department, subject):
        super().__init__(name, country)
        self.department = department
        self.subject = subject

st= Student("Mark Lue", "USA", 1000, "1")
tr = Teacher("Drek Wayne", "USA", "Science", "BIO")

print(tr.department)
tr.print_details()
