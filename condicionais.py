#simples, composto ou encadeado 

n1 = n2 = 0.0

media = 0 

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#calcular a média aritmética das notas

media = (n1+n2)/2

if (media >= 7):
    print('Aprovado!')
    print('Parabéns!')
elif (media >= 5):
    print('Aluno em recuperação!')
else:
    print('Aluno reprovado!')

print('Sua média é {}'.format(media))