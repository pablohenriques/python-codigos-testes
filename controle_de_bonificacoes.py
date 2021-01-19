from funcionario import Funcionario

class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, objeto):
        if isinstance(objeto, Funcionario):
            self._total_bonificacoes += objeto.get_bonificacao()
        else:
            print(f"instância de {self.__class__.__name__} não implementa o método get_bonificacao()")

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

