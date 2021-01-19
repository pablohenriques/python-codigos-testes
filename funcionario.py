# import abc
from collections.abc import MutableSequence

class Funcionario:

    _dados = []

    def __init__(self, nome, cpf, salario=0):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario + 1000

    def __str__(self):
        return f"Nome: {self._nome} - Tipo: {type(self)}"


class Funcionarios(MutableSequence):
    _dados = []

    def __len__(self):
        return len(self._dados)

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __setitem__(self, posicao, valor):
        if (isinstance(valor, Funcionario)):
            self._dados[posicao] = valor
        else:
            raise TypeError('Valor atribuído não é um Funcionario')

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def insert(self, posicao, valor):
        if (isinstance(valor, Funcionario)):
            return self._dados.insert(posicao, valor)
        else:
            raise TypeError('Valor inserido não é um Funcionario')