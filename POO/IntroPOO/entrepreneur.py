from employee import Employee

# An enterpreneur is a employee, so..
# everything a employee have, an enterpreneur has
class Enterpreneur(Employee):
    def __init__(self, name, age, datebirth, sex, salary, sector, hierarchy):
        super().__init__(name, age, datebirth, sex, salary, sector)
        # when we inherit a class, we need to use the 'super().__init__()'
        # with the values of the inherited class
        self.hierarchy = hierarchy

    def dimiss_employee(self, employee_name):
        print(f"{self.name} is dimissing {employee_name}")