from person import Person

# An employee is a person, so..
# everything a person have, an employee has
class Employee(Person):
    def __init__(self, name, age, datebirth, sex, salary, sector):
        super().__init__(name, age, datebirth, sex)
        # when we inherit a class, we need to use the 'super().__init__()'
        # with the values of the inherited class
        self.salary = salary
        self.sector = sector
        
    def go_vacation(self, time):
        # Time as days
        print(f"{self.name} is going to vacation for {time} days")