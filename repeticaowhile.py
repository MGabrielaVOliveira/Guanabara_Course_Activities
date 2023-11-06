'''
n=1
par = impar = 0
while n != 0:
    n=int(input('Digite um valor: \n'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
'''

#programa que pergunta o sexo do indivíduo
'''
n=1
while n !=  'M' and n != 'F':
    n=str(input('Se você tiver o sexo masculino digite M e se tiver feminino digite F')).upper()
    if n == 'M':
        print('Você é do sexo Masculino!')
    elif n == 'F':
        print('Você é do sexo Feminino!')
    else:
        print('Opção Inválida, digite M ou F')
'''

#adivinhar numero entre 0 e 10 que o computador vai 'pensar'
'''
import random
n=1
p=0
c = random.randint(0,11)
while n != c:
    n=int(input('Digite um número entre 0 e 10 para descobrir qual o número que o computador pensou:'))
    p += 1
    if n == c:
        print('Você acertou o número foi {}'.format(c))
    else:
        print('Você não acertou!')
print('Fim! Foram necessários {} palpites para vencer'.format(p))
'''

#menu com opções do que fazer com o número
'''
import random
n1=(int(input('Digite um valor:\n')))
n2=(int(input('Digite um valor:\n')))
c=0
while c!= 5:
    print('Menu')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    c= int(input('Digite a opção desejada:'))
    if c == 1:
        print('A soma de {} e {} é igual a {}'.format(n1,n2,(n1+n2)))
    elif c == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1,n2,(n1*n2)))
    elif c == 3:
        if n1>n2:
            print('O número {} é maior que {}'.format(n1,n2))
        elif n1==n2:
            print('Os números são iguais!')
        else:
            print('O número {} é maior que {}'.format(n2,n1))
    elif c == 4:
        a = random.randint(0, 100)
        b = random.randint(0, 100) 
        b != a
        print('Seus novos números são {} e {}'.format(a,b))
        n1=a
        n2=b
    else:
        print('Número está incorreto, digite um número entre 1 e 5, de acordo com o menu')
'''

#calculando fatorial
'''
from math import factorial
n=int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end= '')
while c > 0:
    print('{}'.format(c), end= '')
    print(' x ' if c>1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))
'''

print('Gerador de PA')
print('-=' * 10)
primeiro=int(input('Primeiro termo:'))
razão=int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont<= 10:
    print('{} ➔  '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')