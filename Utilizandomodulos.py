'''
import math
num=float(input('Digite um valor: \n'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,math.trunc(num)))
'''

'''
import math
co=float(input('qual é o valor do cateto oposto?'))
ca=float(input('Qual é o valor do cateto adjacente'))
h= (((co**2)+ (ca**2))**(1/2))
print('A hipotenusa vai medir {:.2f}'.format(h))
'''

'''
import math
num=int(input('Digite um número: \n'))
raiz=math.sqrt(num) #raiz quadrada
print('A raiz de {} é igual a {:.2f}'.format(num,math.ceil(raiz))) #vai aumentar o elemento raiz para cima
'''

'''
import random
num = random.randint(1,10)
print(num)
'''

'''
import math
an=int(input('Digite o ângulo que você deseja: \n'))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an,cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an,tangente))
'''
#tambem pode ser utilizado from math import radians,sin, cos, tan
#como ficaria> tangente = tan(radians(an))

'''
import random import choice
n1=str(input('Primeiro aluno:\n'))
n2=str(input('Segundo aluno:\n'))
n3=str(input('Terceiro aluno:\n'))
n4=str(input('Quarto aluno:\n'))
lista=[n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
'''

import random 
n1=str(input('Primeiro aluno:\n'))
n2=str(input('Segundo aluno:\n'))
n3=str(input('Terceiro aluno:\n'))
n4=str(input('Quarto aluno:\n'))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)

