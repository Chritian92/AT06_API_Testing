from ChristianGalarza.Exam.Employee import *


class CommercialEmployee(Employee):

    def __init__(self, id, name, departament, pieces_selled):
        super().__init__(id, name, departament)
        self.pieces_selled = pieces_selled

    def calculate_global_salary(self):
        self.global_salary = self.pieces_selled * 2.5
        return self.global_salary


