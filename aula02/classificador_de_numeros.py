# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada 
# seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, 
# identifique se o número é "par" ou "ímpar".

print("# CLASSIFICADOR DE NÚMEROS #")
while True:
    try:
        number = float(input("Digite um número: "))
        break
    except ValueError:
        print("Digite um número válido!\nTente novamente.\n")

if number > 0:
    print(f"O número {number} é positivo!")
elif number < 0:
    print(f"O número {number} é negativo!")
else:
    print(f"O número digitado é zero!")

if number%2 == 0:
    print("O número é par!")
elif number%2 == 1:
    print("O número é impar!")