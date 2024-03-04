from person import Person
from employee import Employee
from entrepreneur import Enterpreneur

marco = Person('Marco', 51, '12/03/1976', 'M')
petro = Employee('Petro', 21, '30/07/1999', 'M', 1239, "B")
lalu = Enterpreneur('Lalu', 34, '20/11/1980', 'F', 4765, "B", "HIGHT")

print("Names:")
print(marco.name) # Marco
print(petro.name) # Petro
print(lalu.name) # Lalu


# they all have the 'talk()' method, because they all are from the Person class, so
print("\nTalking:")

marco.talk("Hello")
petro.talk("How are u?")
lalu.talk("I'll do this ASAP!")

# but, a person does not have the 'go_vacation()' and 'dimiss_employee()' methods, so
# marco, who is a person, cant use these methods

print("\nVacation:")
petro.go_vacation(30)
lalu.go_vacation(60)

# marco.go_vacation(10) # if uncommented, it will make an error


# and, petro, an employee, cant use the 'dimiss_employee()' method
print("\nDimiss:")
lalu.dimiss_employee('Pietra')

# petro.dimiss_employee("someone") # if uncommented, it will make an error