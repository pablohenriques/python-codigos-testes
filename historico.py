import datetime


class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"data abertura: {self.data_abertura}")
        print("transacoes")

        for t in self.transacoes:
            print("-", t)
