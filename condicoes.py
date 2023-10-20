'''
tempo=int(input('Quantos anos o seu carro tem?\n'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')
'''
'''
nome=str(input('Qual é o seu nome?\n'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
'''

'''
import random
n1=int(input('Digite um número entre 0 e 5 e descubra o número que o computador pensou\n'))
n2=random.randint(0,5)
if n2 == n1:
    print('O número foi {}, parabéns! Você venceu!'.format(n2))
else:
    print('O número foi {}, Você perdeu!'.format(n2))
'''

'''
n1 = float(input('Qual foi a velocidade do seu carro?\n'))
velocidade = n1 - 80.00
multa = velocidade * 7.00
if n1 > 80.00:
    print('Sua velocidade foi {:.2f} km, portanto você foi multado em {:.2f} reais'.format(n1, multa))
else:
    print('Parabéns! Você está dentro do limite, não foi multado!')
'''


'''
n1=float(input('Qual a distância da sua viagem em km?\n'))
if n1<=200:
    preco=n1*0.5
    print('O valor da sua passagem é {:.2f} reais'.format(preco))
else:
    preco=n1*0.45
    print('O valor da sua passagem é {:.2f} reais'.format(preco))
'''

#ex32

#ex33

'''
n1=float(input('Qual é o seu salário?\n'))
if n1>1250.00:
    aumento=(n1*(10/100))
    novo_salario=n1+aumento
    print('O seu aumento foi de {:.2f} reais, portanto, seu novo salário será de {:.2f} reais'.format(aumento,novo_salario))
else:
    aumento=(n1*(15/100))
    novo_salario=n1+aumento
    print('O seu aumento foi de {:.2f} reais, portanto, seu novo salário será de {:.2f} reais'.format(aumento,novo_salario))
'''

'''
n1=int(input('Digite o primeiro lado do triângulo:\n'))
n2=int(input('Digite o segundo lado do triângulo:\n'))
n3=int(input('Digite o terceiro lado do triângulo:\n'))
if (n1>0) and (n2>0) and (n3>0) and (n1+n2)>n3 and (n2+n3)>n1 and (n3+n1)>n2:
    print('Estes lados podem formar um triângulo')
else:
    print('Estes lados não podem formar um triangulo')
'''

'''
n1=float(input('Digite um número:\n'))
resultado=n1%2
if resultado==0:
    print('O número {} é PAR'.format(n1))
else:
    print('O número {} é IMPAR'.format(n1))
'''

'''
from datetime import date
ano=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:\n'))
if ano==0:
    ano=date.today().year
if ano%4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
'''

a=int(input('Digite o primeiro valor:\n'))
b=int(input('Digite o segundo valor:\n'))
c=int(input('Digite o terceiro valor:\n'))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
