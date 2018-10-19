from Heranca.Pessoa import Pessoa
from Heranca.Funcionario import Funcionario


class Professor(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, salario, disciplina):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.salario = salario
        self.disciplina = disciplina

    def __str__(self):
        return f"{super().__str__()},Matricula: {self.matricula} Salário: {self.salario},  Disciplina: {self.disciplina}"
