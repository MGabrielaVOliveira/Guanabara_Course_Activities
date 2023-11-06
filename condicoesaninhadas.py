
#este programa seria para empréstimo bancário para a compra de uma casa, em que levamos em consideração:
#valor da casa, salário do comprador e em quantos anos ele vai pagar
#a prestação não pode exceder 30% do salário do comprador
'''
vc=float(input('Digite o valor da casa: \n'))
salario=float(input('Digite o valor do seu salário: \n'))
anos=float(input('Em quantos anos você quer pagar a casa? \n'))
idade=int(input('Qual a sua idade?\n'))
pm=vc/(anos*12)
if (idade+anos)<=60:
    print('Infelizmente não foi possível financiar sua casa por conta do tempo de financiamento')
elif pm<=(salario*(30/100)):
    print('Parabéns! Seu financiamento foi aprovado! Sua prestação será de {:.2f} reais por mês'.format(pm))
else:
    print('Sua prestação seria de {:.2f} reais, e infelizmente seu financiamento não foi aprovado.'.format(pm))
'''


#conversao de numero inteiro para binario, octal e hexadecimal
'''
num=int(input('Escreva um número:\n'))
opcao=int(input('Digite 1 para BINÁRIO, 2 para OCTAL e 3 para HEXADECIMAL\n'))
if opcao==1:
    print(bin(n)[2:])
elif opcao==2:
    print(oct(n)[2:])
elif opcao==3:
    print(hex(n)[2:])
else:
    print('Número incorreto, digite 1, 2 ou 3')
'''


#programa para ver qual número é maior
'''
n1=int(input('Digite um número:\n'))
n2=int(input('Digite outro número:\n'))
if n1>n2:
    print('O primeiro valor é o maior')
elif n2>n1:
    print('O segundo número é o maior')
else:
    print('Não existe valor maior, os dois são iguais')
'''

#programa para ver idade de acordo com o tempo de alistamento
'''
ano_nascimento=int(input('Qual é o seu ano de nascimento?'))
tempo=2023-ano_nascimento
if tempo<18:
    print('Você ainda vai se alistar ao serviço militar, falta {} anos'.format(18-tempo))
elif tempo>18:
    print('Já passou do tempo de alistamento, você passou {} anos do prazo'.format(tempo-18))
else:
    print('Agora é hora de se alistar!')
'''

#programa que calcula a media e diz se o aluno foi reprovado, aprovado ou esta de recuperação
'''
n1=int(input('Digite sua primeira nota:\n'))
n2=int(input('Digite sua segunda nota\n'))
media=(n1+n2)/2
if media<5:
    print('REPROVADO')
elif media>=7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
'''

#este programa reconhece idade e mostra categoria em algum esporte definitivo
'''
ano_nascimento=int(input('Qual é o seu ano de nascimento?\n'))
idade=2023-ano_nascimento
if idade<=9:
    print('Sua categoria é: MIRIM')
elif idade>9 and idade<=14:
    print('Sua categoria é: INFANTIL')
elif idade>14 and idade<=19:
    print('Sua categoria é: JUNIOR')
elif idade==20:
    print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER')
'''

#este programa realiza calculo de IMC
'''
peso=float(input('Digite o seu peso em kg:\n'))
altura=float(input('Digite sua altura em m:\n'))
IMC=peso/(altura**2)
if IMC<18.5:
    print('O resultado do seu IMC é {:.2f}, e você está abaixo do peso'.format(IMC))
elif IMC>=18.5 and IMC<25:
    print('O resultado do seu IMC é {:.2f}, e você está com o peso ideal'.format(IMC))
elif IMC>=25 and IMC<30:
    print('O resultado do seu IMC é {:.2f}, e você está sobrepeso'.format(IMC))
elif IMC>=30 and IMC<=40:
    print('O resultado do seu IMC é {:.2f}, e você está obeso'.format(IMC))
else:
    print('O resultado do seu IMC é {:.2f}, e você está com obesidade mórbida'.format(IMC))
'''

#programa que calcula o valor a ser pago considerando as condições
preco=float(input('Qual é o preço do produto?\n'))
condicao=int(input('Para a vista digite 1, a vista no cartão digite 2, em ate 2x no cartao digite 3 e 3x ou mais digite 4\n'))
if condicao==1:
    print('O preço do produto ficou de: {:.2f}'.format(preco-(preco*(10/100))))
elif condicao==2:
    print('O preço do produto ficou de: {:.2f}'.format(preco-(preco*(5/100))))
elif condicao==3:
    print('O preço do produto ficou de: 2x de {:.2f}'.format(preco))
elif condicao==4:
    print('O preço do procuto ficou de: {:.2f}'.format(preco+(preco*(20/100))))
else:
    print('Digite um número disponível!')