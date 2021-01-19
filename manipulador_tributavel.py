from tributavel import Tributavel
class ManipuladorDeImpostos:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, Tributavel):
                total += t.get_valor_imposto()
            else:
                print('Não tributável!')
        return total