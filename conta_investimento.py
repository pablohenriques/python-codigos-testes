from conta import Conta


class ContaInvestimento(Conta):

    def atualiza(self, taxa):
        return super().atualiza(taxa) * 5
