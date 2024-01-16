# Lista: representa uma sequência de valores 

# Sintaxe: nome_lista = [valores]

notas = [5,7,8,9]
notas2 = [10,9,8,7,6,5,4,3,2,1]
valores = notas2 + notas

# print(valores[-3])
# print(valores[5:5])
# print(len(valores))
# print(sorted(valores, reverse=True))
# print(sum(valores))
# print(min(valores))
# print(max(valores))

# valores.append(13)
# print(valores)
# valores.pop(1)
# print(valores)
# valores.insert(3, 21)
# print(valores)

# print(1 in valores)

planetas = ['Venus', 'Terra', 'Marte', 'Jupiter']
# planetas.append('Plutão')
# print(planetas)
# planetas.remove('Terra')
# print(planetas)

for planeta in planetas:
    print(planeta)