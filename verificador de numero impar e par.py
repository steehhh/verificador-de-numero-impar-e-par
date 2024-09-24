num1 = "num1"

teste = "teste"

num1 = int(input("Olá! Sou um progama que verifica se o número digitado é ímpar. Por favor, digite um número: "))

teste = num1 % 2

if teste == 1: 
    print("o numero", num1, "é impar")

elif teste == 0:
    print("o numero", num1, "é par")

else:
    print("expressao invalida")