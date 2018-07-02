from ChristianGalarza.Python.Session5.modules.Person import Person


class Employee(Person):
    def __init__(self, name, last_name, age, ci, employee_id, departament):
        super().__init__(name, last_name, age, ci)
        self.employee_id = employee_id
        self.departament = departament


employee1 = Employee("Homero", "Simpson", 53, 59625483, 10, "IS")

print("My name is {} {} I am {} years old and my C.I. is {}"
      .format(employee1.name, employee1.last_name, employee1.age, employee1.ci))
print("My name is {} with C.I. is {}, my id is {} and I work in {} departament"
      .format(employee1.name, employee1.ci, employee1.employee_id, employee1.departament))
