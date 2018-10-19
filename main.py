from Heranca.Pessoa import Pessoa
from Heranca.Funcionario import Funcionario
from Heranca.Professor import Professor

p1 = Pessoa("João", "123", 20)
print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())
print(p1)

f1 = Funcionario("José","456", 40, "0099", 2526.45, "Biblioteca")
print(f1)

p1 = Professor("Jorge","456", 45, "852456", 10.000, "Biologia")
print(p1)