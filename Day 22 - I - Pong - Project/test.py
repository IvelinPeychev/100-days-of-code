class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self,amount):
        self.salary += amount


class Manager(Employee):
    def __init__(self, name, salary, runs_department):
        super().__init__(name, salary)
        self.runs_department = runs_department


m1 = Manager('Lotty', 2000, 'Logistics')
m1.raise_salary(150)
print(m1.name, m1.salary, m1.runs_department)