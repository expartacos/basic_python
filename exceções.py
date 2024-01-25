# Exceção é um objeto que representa um erro que ocorreu ao executar o programa
# Bloco try ... except

def div(k, j):
    return round(k/j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite um número: '))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor. tente novamente. ')
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print('Erro: divisão por zero')
    except:
        print('Ocorreu um erro desconhecido ')
    else:
        print(f'Resultado: {r}')
    finally:
        print(f'\n Fim do programa')





