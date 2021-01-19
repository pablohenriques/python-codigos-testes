class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributavies):
        total = 0
        for t in lista_tributavies:
            total += t.get_valor_imposto()
        return total

if __name__ == "__main__":
    from conta import ContaCorrente, SeguroDeVida, TributavelMinIn
    from tributavel import Tributavel

    cc1 = ContaCorrente("123-4", "Joao", 1000)
    cc2 = ContaCorrente("123-4", "Jose", 1000)
    seguro1 = SeguroDeVida(100, "Jose", "345-77")
    seguro2 = SeguroDeVida(200, "Maria", "237-98")

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(total)