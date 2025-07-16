"""
8.	Faça um Programa que pergunte quanto você ganha por hora
 e o número de horas trabalhadas no mês. 
 Calcule e mostre o total do seu salário no referido mês.
"""

n1 = int(input('Insira o valor que recebe por cada hora de trabalho =>'))
print('Você recebe =>', n1, 'por cada hora de trabalho')
n2 = int(input('Insira a quantidade de horas trabalhadas no mês =>'))
print('Você trabalha =>', n2, 'horas por mês')
salario = n1 * n2
print('Portanto seu salario mensal será =>', salario, 'com base na jornada mensal calculada pelos dados fornecidos')
