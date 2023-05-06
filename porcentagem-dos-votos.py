VotosBrancos = int(input('Quantidade de votos em branco: '))
Nulos = int(input('Quantidade de votos nulos: '))
Validos = int(input('Quantidade de votos válidos: '))
Total = VotosBrancos + Nulos + Validos
print('O total de votos é: ', Total)
VotosBrancosP = (VotosBrancos * Total) / 100
print('A porcentagem dos votos brancos é', VotosBrancosP, '%.')
NulosP = (Nulos * Total) / 100
print('A porcentagem dos votos nulos é', NulosP,'%.')
ValidosP = (Validos * Total) / 100
print('A porcentagem dos votos válidos é', ValidosP,'%.')
