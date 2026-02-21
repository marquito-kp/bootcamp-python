# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

print("VERIFICADOR DE PALÍNDROMO")

while True:
    is_palindromo = input("Digite uma palavra ou frase: ")
    if isinstance(is_palindromo,str):
        formatado = is_palindromo.replace(" ","").lower()
        if formatado == formatado[::-1]:
            print("É um palindromo!")
            break
        else:
            print("Não é um palindromo!")
            break
    else:
        print("Entrada invalida, digite uma palavra ou frase!")