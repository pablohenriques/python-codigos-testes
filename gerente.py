from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self,nome, cpf, salario, senha, quantidade_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._quantidade_funcionarios = quantidade_funcionarios


    def autentica(self, senha):
        if self._senha == senha:
            print("-acesso permitido-")
            return True
        else:
            print("-acesso negado-")
            return False


    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

    def __str__(self):
        return super().__str__()