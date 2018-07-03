from ChristianGalarza.Python.Exam.Employee import *


class ProductionEmployee(Employee):

    def __init__(self, id, name, department, pieces_produced, defective_pieces):
        super().__init__(id, name, department)
        self.pieces_produced = pieces_produced
        self.defective_pieces = defective_pieces

    def calculate_global_salary(self):
        self.global_salary = (self.pieces_produced * 10) - (self.defective_pieces * 1.3)
        return self.global_salary
