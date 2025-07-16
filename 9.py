"""
9.	Faça um Programa que peça a temperatura em graus Farenheit,
 transforme e mostre a temperatura em graus Celsius.
   C = (5 * (F-32) / 9).
"""

n1 = int(input('Digite a temperatura em Graus Farenheit =>'))
print('Você escoheu =>', n1, 'ºF')
temperatura = (n1 - 32) * 5 / 9
print('Portanto a temperatura escolhida convertida em Graus Celsius é =>', temperatura, 'ºC')