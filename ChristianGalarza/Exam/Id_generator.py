CE = "CE_0"
PE = "PE_0"


def generate_id(identifier, number: int):
    if identifier is CE or identifier is PE:
        return identifier + str(number)


def calculate_discount(self):
    return (self.global_salary * 12.5)/100


def calculate_net_salary(global_salary, discount):
   return global_salary - discount
