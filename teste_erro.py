
def divisao(x, y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("Divisão por zero")
    else:
        print(f"o resultado é {resultado}")
    finally:
        print("executando o finally")


if __name__ == "__main__":
    divisao(2, 1)
    divisao(2, 0)
    divisao('2', '1')