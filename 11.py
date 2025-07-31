"""
11.	Faça um Programa que peça 2 números inteiros e um número real.
 Calcule e mostre:
•	o produto do dobro do primeiro com metade do segundo .
•	a soma do triplo do primeiro com o terceiro.
•	o terceiro elevado ao cubo.
"""

n1 = int(input('Digite um número inteiro'))
n2 = int(input('Digite um número inteiro'))
n3 = float(input('Digite um número real(numero quebrado / fracionado)'))
dobro = (n1 + n2) + (n2 / 2)
soma = (n1 * 3) + n3
triplo = (n3 * 3)
print ('O produto do dobro do primeiro com a metade do segundo numero é =>',dobro )
print ('O produto da elevaçao ao cubo do terceiro número é =>', triplo)
print ('O produto da soma do triplo do primeiro número com o terceiro número é =>', soma)


