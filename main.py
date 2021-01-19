from funcionario import Funcionario, Funcionarios
import csv


funcionarios = Funcionarios()
arquivo = open("funcionarios.txt", "r")
leitor = csv.reader(arquivo)

for linha in leitor:
    funcionario = Funcionario(linha[0], linha[1], float(linha[2]))
    funcionarios.append(funcionario)

    print("salário - bonificação")
    for f in funcionarios:
        print(f"{f._salario} - {f.get_bonificacao()}")

arquivo.close()

#for f in funcionarios:
#    print(f._salario)