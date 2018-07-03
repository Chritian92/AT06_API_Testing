from ChristianGalarza.Exam.EmployeeComercial import *
from ChristianGalarza.Exam.EmployeeProduction import *
from ChristianGalarza.Exam.Id_generator import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('application.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

dictionary = []


class Main:

    def create_dictionary(self):
        logger.info("Executing main program")
        employees_quantity = int(input("Insert the quantity of employees to be registered: "))
        if 2 < employees_quantity < 16:
            for i in range(employees_quantity):
                employee_name = input("Insert the name of the employee: ")
                employee_department = input("Insert the departament: ")
                if employee_department.lower() == "commercial":
                    pieces_sell = int(input("Employee amount of pieces sell?: "))
                    commercial_emplo = CommercialEmployee(generate_id("CE_0", i), employee_name, employee_department
                                                          , pieces_sell)
                    commercial_emplo.calculate_global_salary()
                    commercial_emplo.calculate_discount()
                    commercial_emplo.net_salary()
                    logger.debug('Registrys: %s', commercial_emplo.print_employee())
                    dictionary.append(commercial_emplo)
                elif employee_department.lower() == "production":
                    logger.info("Creating production_employee")
                    pieces_produced = int(input("Insert the quantity of pieces produced?: "))
                    defective_pieces = int(input("Insert the quantity of defective pieces?: "))
                    production_emplo = ProductionEmployee(generate_id("PE_0", i), employee_name, employee_department
                                                          , pieces_produced, defective_pieces)
                    production_emplo.calculate_global_salary()
                    production_emplo.calculate_discount()
                    production_emplo.net_salary()
                    logger.debug('Registrys: %s', production_emplo.print_employee())
                    dictionary.append(production_emplo)
        else:
            print("Invalid quantity please insert again")
            logger.info("Invalid quantity please insert again")


main = Main()
main.create_dictionary()
