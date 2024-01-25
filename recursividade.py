# Recursividade 

# Fórmula geral para o fatorial:
# fatorial(num) = 1, se num = 0 ou se num = 1 'Caso-Base'
# fatorial(num) = num * fatorial(num-1), se num > 1 'Caso Recursivo'
# fatorial 4! = 4 * fatorial(3)  = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1) = 4 * 3 * 2 * 1 = 24

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)
    
if __name__ == '__main__':
    x = int(input('Digite um número inteiro positivo para calcular seu fatorial: '))
    try:
        res = fatorial(x)
    except RecursionError:
        print(f'O numero é muito grande ou é negativo ') 
    else:
        print(f'O fatorial de {x} = {res}')
