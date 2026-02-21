# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError.
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

print("CONVERSOR DE TEMPERATURA")

while True:
    try:
        print("\nEscolha qual temperatura você deseja converter:\n1-Celsius\n2-Fahrenheit\n")
        temperatura = str(input("Sua escolha: "))
        if temperatura == "1":
            valor = float(input("\nDigite o valor da temperatura: "))
            fahrenheit = round((valor * (9/5)) + 32,2)
            print(f"\nA conversão de {valor} º celsius é equivalente a {fahrenheit} º fahrenheit.")
            break
        elif temperatura == "2":
            valor = float(input("\nDigite o valor da temperatura: "))
            celsius = round((valor - 32) * (5/9),2)
            print(f"\nA conversão de {valor} º fahrenheit é equivalente a {celsius} º celsius.")
            break
        elif temperatura.isspace():
            print("Você digitou espaços em branco!")
        else:
            print("Digite uma opção válida!")
    except ValueError as e:
        print("\nOps! Esse não é um número válido para a conversão de temperatura. Tente novamente..\n")
