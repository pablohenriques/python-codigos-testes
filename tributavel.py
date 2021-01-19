import abc


class Tributavel(abc.ABC):
    """ Classe que contém operações de um objeto autenticavel
    As subclasses concretas devem sobrescrever o método get_valor_imposto
    """

    @abc.abstractmethod
    def get_valor_imposto(self, valor):
        pass

