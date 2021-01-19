from historico import Historico
from excecoes import SaldoInsuficienteError
import abc


class Conta(abc.ABC):
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', '_tipo']

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._tipo = self
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    def deposita(self, valor):
        if valor < 0:
            raise ValueError("Você tentou depositar um valor negativo.")
        else:
            self._saldo += valor

    def saca(self, valor):
        if self._saldo < valor:
            raise ValueError('Você tentou sacar um valor negativo.')
        if self._saldo < valor:
            raise SaldoInsuficienteError('Saldo insuficiente.')
        else:
            self._saldo -= valor
            self._historico.transacoes.append(f"saque de {valor}")  #

    def extrato(self):
        print(f"Número: {self._numero} - Saldo: {self._saldo}")
        self._historico.transacoes.append(f"tirou extrato - saldo de {self._saldo}.")

    def transfere_para(self, destino, valor):

        if self.saca(valor):
            return False
        else:
            destino.deposita(valor)
            self._historico.transacoes.append(f"transferencia de {valor} para conta {destino.numero}")

    @abc.abstractmethod
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

    def __str__(self):
        return f"Dados da Conta: Número: {self._numero} - Titular: {self._titular} - Saldo: {self._saldo} - Limite: {self._limite}"


class TributavelMinIn:

    def get_valor_imposto(self):
        pass


class ContaCorrente(Conta):

    def atualiza(self, taxa):
        super().atualiza(taxa) * 2
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10

    def get_valor_imposto(self):
        return self._saldo * 0.01

    def saca(self, valor):
        if valor < 0:
            raise ValueError("Você tentou sacar um valor negativo.")
        if self._saldo < valor:
            raise SaldoInsuficienteError("Saldo insuficiente")
        self._saldo -= (valor + 0.10)


class ContaPoupanca(Conta):

    def deposita(self, valor):
        if valor < 0:
            raise ValueError("Você tentou depositar um valor negativo.")
        else:
            self._saldo += valor

    def atualiza(self, taxa):
        super().atualiza(taxa) * 3
        return self._saldo

    def get_valor_imposto(self):
        return self._saldo * 0.01


class SeguroDeVida():

    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05
