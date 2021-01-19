from collections import namedtuple

Conta = namedtuple('Conta', 'numero titular saldo limite')
conta = Conta('123-4', 'João', 1000.0, 1000.0)

print(conta)
print(conta.titular)
conta.titular = "José"