'''
n1=int(input('digite um numero:'))
n2=int(input('digite mais um numero:'))
s= n1 + n2
print('a soma vale', s)
'''

#input é considerado string, então o int é utilizado para tornar numero inteiro
#int é numero inteiro
#float é numero com . como 4.5
#bool aceita true e false, precisa usar a primeira letra maiuscula,
#str, ou string é usado como palavras, entre aspas.

'''
n1=int(input('digite um valor:'))
n2= int(input('digite outro:'))
s = n1+n2
#print('a soma entre',n1,'e',n2,'vale',s)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
'''

'''
n=float(input('Digite um valor:'))
print(n)
'''
#se eu colocar 2 vai virar 2.0
#se eu colocar bool, vai dizer true ou false.

'''
n=input('Digite algo:')
print(n.isnumeric())
'''
#pra dizer se é numerico, isalpha seria letra.

'''
n1= int(input('Digite um numero:'))
n2= int(input('Digite outro numero'))
s= n1+n2
print('O valor da soma é', s)
'''

'''
n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
'''

'''
n= int(input('Digite um número:'))
d=n*2
t=n*3
m=n/2
print('O dobro de {} vale {}' .format(n,d))
print('O triplo de {} vale {}' .format(n,t))
print('A metade de {} vale {}' .format(n,m))
'''

'''
n1=int(input('Digite a primeira nota do aluno:'))
n2=int(input('Digite a segunda nota:'))
s=(n1+n2)/2
print('A média entre {} e {} é {}' .format(n1,n2,s))
'''

'''
n=int(input('Digite uma distância em metros: '))
print('A medida de ',n,' m corresponde a:')
print((n/1000), 'km')
print((n/100), 'hm')
print((n/10), 'dam')
print((n*10), 'dm')
print((n*100), 'cm')
print((n*1000), 'mm')
'''

'''
n=float(input('Digite um número para ver sua tabuada\n'))
x1 = n*1
x2 = n*2
x3 = n*3
x4 = n*4
x5 = n*5
x6 = n*6
x7 = n*7
x8 = n*8
x9 = n*9
x10 = n*10
print('-----------')
print('{} x 1 = {}' .format(n,x1))
print('{} x 2 = {}' .format(n,x2))
print('{} x 3 = {}' .format(n,x3))
print('{} x 4 = {}' .format(n,x4))
print('{} x 5 = {}' .format(n,x5))
print('{} x 6 = {}' .format(n,x6))
print('{} x 7 = {}' .format(n,x7))
print('{} x 8 = {}' .format(n,x8))
print('{} x 9 = {}' .format(n,x9))
print('{} x 10 = {}' .format(n,x10))
print('-----------')
'''

'''
n=float(input('Quanto de dinheiro você tem na carteira?\n'))
dolar=n/3.27
print('Com {:.2f} reais você consegue comprar {:.2f} dolares'.format(n,dolar))
'''

'''
n1=float(input('Digite a Largura da parede em metros\n'))
n2=float(input('Digite a altura da parede em metros\n'))
area=n1*n2
litro=area/2
print('A área da parede que você quer pintar é {:.2f} m², portanto será necessário {:.2f} litros de tinta para pintar a parede'.format(area,litro))
'''

'''
n=float(input('O preço do produto é: \n'))
desconto= n*0.05
vd=n-desconto
print('O preço do produto sem desconto é {:.2f} reais e com o desconto de 5% fica {:.2f} reais'.format(n,vd))
'''

'''
n=float(input('Qual o salário do funcionário? \n'))
aumento=n*15/100
va=n+aumento
print('O salário do funcionário é {} reais, com o aumento de {} reais, o novo salário será de: {} reais'.format(n,aumento,va))
'''

'''
C=float(input('A temperatura em Celsius é de: \n'))
F= (1.8*C)+32
print('Convertendo esta temperatura, {}°C ,para farenheit fica de {}°F'.format(C,F))
'''

'''
km=float(input('Qual foi a quantidade km percorridos pelo carro alugado? \n'))
d=float(input('Qual a quantidade de dias que ele foi alugado? \n'))
p=(60*d)+(0.15*km)
print('O preço a pagar de acordo com {:.2f}km percorridos e {:.2f} dias alugados foi de {}'.format(km,d,p))
'''

'''
import math
num=float(input('Digite um valor: \n'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,math.trunc(num)))
'''

import math
co=float(input('qual é o valor do cateto oposto?'))
ca=float(input('Qual é o valor do cateto adjacente'))
h= (((co**2)+ (ca**2))**(1/2))
print('A hipotenusa vai medir {:.2f}'.format(h))