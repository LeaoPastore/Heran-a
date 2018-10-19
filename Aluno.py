from Heranca.Pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, turma):
        super(). __init__(nome, cpf, idade)
        self.matricula = matricula
        self.turma = turma


    def __str__ (self):
        return f"{super().__str__()}, Disciplina: {self.disciplina}"
