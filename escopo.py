# Escopo Global e Escopo Local 

# Variáveis globais são declaradas e da pra usar em toda parte do código 
# Variáveis locais são declaradas e da pra usar apenas dentro do bloco onde foi declarada

var_global = 'Global' # Variável global

def escreve_texto():
    global var_global
    var_global = 'Banco de dados com SQL'
    var_local = 'Local' # Variável local
    print(f'Variável local: {var_local}')
    print(f'Variável global: {var_global}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    # print(f'Variável local: {var_local}')
    print(f'Variável global: {var_global}')