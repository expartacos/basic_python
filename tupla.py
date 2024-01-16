# São imutáveis

halogenios = ('F', 'Cl', 'Br', 'I')
gases_nobres = ('He', 'Ne', 'Ar', 'Kr')
elementos = halogenios + gases_nobres
print(elementos)

# Operações não disponiveis em tuplas: .sort(), .append(), .pop(), .reverse() ...

for elemento in elementos:
    print(f'Elemento: {elemento}')

grupo17 = list(halogenios)
print(grupo17)

grupo1= ['li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne']
alcalinos = tuple(grupo1)
print(type(alcalinos))

print(sorted(alcalinos))