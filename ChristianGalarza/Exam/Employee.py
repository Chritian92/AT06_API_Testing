from ChristianGalarza.Exam.Person import *


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('application.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Employee(Person):
    def __init__(self, name, employee_id, department):
        super().__init__(name)
        self.employee_id = employee_id
        self.department = department
        self.global_salary = 0
        self.totalDiscount = self.calculate_discount()

    def calculate_discount(self):
        return (self.global_salary * 12.5)/100

    def print_employee(self):
        print("Employee ID | NAME | Department | Global Salary | Total Discount | Net Salary")
        print("{} | {} | {} | {} | {} | {}".format(self.employee_id, self.name, self.department,
                                                   self.global_salary, self.total_discount, self.net_salary))

    def net_salary(self):
        return self.global_salary - self.totalDiscount

    def department(self):
        return self.department

    def global_salary(self):
        return self.global_salary

    def total_discount(self):
        return self.totalDiscount

    def employee_id(self, ):
        return self.employee_id
