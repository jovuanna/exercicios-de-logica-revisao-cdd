numeros = []
soma = 0
cont1 = 0
#índice 1: encontrar os números pares no vetor
for a in range(5):
    numeros.append(int(input("Digite um valor: ")))
    '''adicionar os números ao vetor (numeros) 5 vezes.'''
for b in range(5):
    if numeros[b] % 2 == 0:
        '''se no vetor numeros na posição b tiver o resto da divisão por 2 igual a 0'''
        cont1 += 1
        print(f"Esse número é par {numeros[b]}.")
#índice 2: maior e menor número dentro do vetor.
maior = numeros[0]
menor = numeros[0]
for c in range(5):
    if numeros[c] > maior:
        '''vai passar por cada posição e identificar se ele é maior. Exemplo: posição 0 = 2, posição 1 = 3 
        (O número da posição 1 é maior que o da posição 0, então agora ele vai aparecer como maior.)'''
        maior = numeros[c]
    elif numeros[c] < menor:
        menor = numeros[c]
print(f"O maior valor dentro do vetor é: {maior}.")
print(f"O menor valor dentro do vetor é: {menor}.")
#índice 3: quantidade de número maior no vetor.
cont2 = 0
for e in range(5):
    '''Esse for serve pra somar todos os elementos numerais dentro do vetor'''
    soma += numeros[e]
print(f"A soma dos valores é: {soma}")
media = soma / 5
'''A variável media vai fazer a média desses números'''
print(f"A média dos valores é: {media}")
for f in range(5):
    if numeros[f] > media:
        '''Esse if vai passar por cada posição e identificar se o número é maior que a média'''
        cont2 += 1
        '''O contador vai passar por cada posição também e contar 
        quantos números maiores que a média existem dentro do vetor'''
print(f"A quantidade de número maiores dentro do vetor é {cont2}.")
