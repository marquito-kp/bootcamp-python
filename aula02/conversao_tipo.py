# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string 
# de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada 
# elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem 
# de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

print("# CONVERSÃO DE TIPO COM VALIDAÇÃO #")

number = input("Digite uma lista de número inteiros separados por virgulas: ")
number_str = number.split(",")
number_array = []

try:
    for num in number_str:
        number_array.append(int(num.strip()))
    print("Lista de inteiros: ", number_array)
except ValueError:
    print("Valor não inteiro inserido incorretamente, verifique!")