# Funções 
# Modularização, Reúso de código, Legibilidade,

# def mensagem():
#     print('Ola mundo!')

# mensagem()

# Função com argumentos
# def soma(a, b):
#     print(a + b)

# soma(12, 7)

# def mult(x, y):
#     return x*y

# a = 5
# b = 6
# c = mult(a, b)
# print(c)

# def div(x, y):
#     if y != 0:
#         return x/y
#     else:
#         return 'Erro'
    
# if __name__ == '__main__':
#     a = int(input('Primeiro valor: '))
#     b = int(input('Segundo valor: '))

#     c = div(a, b)
#     print(f'{a} dividido por {b} é = {c}')

def quadrado(val):
    quadrados = []
    for x in val: 
        quadrados.append(x ** 2)
    return quadrados

def contar(num=11, caractere ='0-'):
    for i in range(1, num):
        print(caractere)
if __name__ == '__main__':
    # valores = [1, 2, 3, 4, 5]
    # resultados = quadrado(valores)
    # for g in resultados:
    #     print(g)
    contar(num=9, caractere='*')
