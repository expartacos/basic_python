# Funções lambda (anÔnimas)
# Sintaxe: 
# lambda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(1, 11):
#     print(quadrado(i))

# par = lambda x: x % 2 == 0
# print(par(9))

# f_c = lambda f: (f-32)*5/9
# print(f_c(212))

# Função map()
# Sintaxe:
# map(função, iterável)

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# Função de ordem superir a map() 
# palavras = ['python', 'é', 'uma']
# maiúsculas = list(map(str.upper, palavras))
# print(maiúsculas)

# Função filter()
# Sintaxe:
# filter(função, iterável)

def numeros_pares(n):
    return n % 2 == 0

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(numeros_pares, num))
print(pares)