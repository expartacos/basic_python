elemento = {
    'Z': 3,
    'nome' : 'Lítio',
    'simbolo' : 'Li',
    'grupo' : 'Metais Alcalinos',
    'densidade' : 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')

print(f'O dicionário possui {len(elemento)} elementos')

# Atualizar uma entrada
elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionando uma entrada 
# elemento['período'] = 1
# print(elemento)

# # Exclusão de itens em dicionários
# del elemento['período']
# print(elemento)

# # apagar todos os itens 
# elemento.clear()
# print(elemento)

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i}:{j}')