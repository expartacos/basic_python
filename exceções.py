# Exceção é um objeto que representa um erro que ocorreu ao executar o programa
# Bloco try ... except

def div(k, j):
    return round(k/j, 2)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

try:
    r = round(n1/n2, 2)
except ZeroDivisionError:
    print('Erro: divisão por zero')
else:
    print(f'Resultado: {r}')



