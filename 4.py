#4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = int(input('Digite a primeira nota'))
n2 = int(input('Digite a segunda nota'))
n3 = int(input('Digite a terceira nota'))
n4 = int(input('Digite a quarta nota'))

entrada = input('Voce quer calcular a media destas notas?')
entrada = entrada.lower()
print(entrada)

if entrada == 'sim':
media = n1+n2+n3+n4
    print('A média calculada é =>', media)
elif entrada == 'não':
    print('Ok, até mais...')
else:
    print('Você não escolheu uma opção válida, por favor recomece e escolha entre sim ou não...')