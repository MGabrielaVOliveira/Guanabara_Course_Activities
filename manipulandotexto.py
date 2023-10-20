'''
nome=str(input('Digite o seu nome completo:\n'))
print('O seu nome em letras maiusculas é:')
print(nome.upper())
print('O seu nome com letras minusculas é:')
print(nome.lower())
print('O seu nome tem',(len(nome)-nome.count(' ')),'letras')
#print('O seu nome tem {} letras'.format(nome.find(' ')))
separa=nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
'''

'''
num=int(input('Digite um número\n'))
U=num//1%10
D=num//10%10
C=num//100%10
M=num//1000%10
print('A unidade deste número é {}'.format(U))
print('A dezena deste número é {}'.format(D))
print('A centeza deste número é {}'.format(C))
print('O milhar deste número é {}'.format(M))
'''

'''
cid=str(input('Em que cidade você nasceu?\n')).strip()
print(cid[:5].upper() == 'SANTO')
'''

'''
nome = input('Como é o seu nome?\n')
print('SILVA' in nome.upper())
'''

'''
nome=input('Digite seu nome completo: \n').upper().strip()
print('A letra A aparece {} vezes na frase'.format(nome.count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.rfind('A')+1))
'''

n=str(input('Digite o seu nome completo:\n').strip())
nome=n.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

