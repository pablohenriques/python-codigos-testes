class Banco:


    _lista_contas = []

    def __init__(self, nome="brasil"):
        self._nome = nome

    def adiciona(self, conta):
        self._lista_contas.append(conta)

    def pegaConta(self, posicao):
        conta = self._lista_contas[posicao]
        return conta.__str__()

    def pegaTotalDeContas(self):
        return len(self._lista_contas)

    def contas(self):
        return self._lista_contas