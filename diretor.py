from funcionario import Funcionario


class Diretor (Funcionario):

    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)