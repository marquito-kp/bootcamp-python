# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação 
# matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

print("# CALCULDORA SIMPLES #")

while True:
    while True:
        try:
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite outro número: "))
            break
        except ValueError:
            print("Insira um número válido!\n Tente novamente")
    try:
        operador = input("Selecione o operador da conta:\n (+) - soma\n (-) - Subtração\n (*) - Multiplicação\n (/) - Divisão\nSua escolha: ")
        if operador not in ['+','-','*','/']:
            raise ValueError("Operador inválido.")
    except ValueError as e:
        print(f"{e}\nsTente novamente!")
    if operador == "+":
        soma = num1 + num2
        print(f"Resultado: {soma}")
        break
    elif operador == "-":
        subtração = num1 - num2
        print(f"Resultado: {subtração}")
        break
    elif operador == "*":
        multiplicacao = num1 * num2
        print(f"Resultado: {multiplicacao}")
        break
    elif operador == "/":
        try:
            divisao = num1 / num2
            print(f"Resultado: {divisao}")
            break
        except ZeroDivisionError:
            print("O número não pode ser dividido por 0 (zero).")
