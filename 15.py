"""
15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
   8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
•	salário bruto.
•	quanto pagou ao INSS.
•	quanto pagou ao sindicato.
•	o salário líquido.
•	calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$ IR (11%) : R$ INSS (8%) : R$ Sindicato ( 5%) : R$ Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
print("\n------ RESUMO SALARIAL ------")
print(f"Salário Bruto     : R$ {salario_bruto:.2f}")
print(f"Desconto IR (11%) : R$ {ir:.2f}")
print(f"Desconto INSS (8%): R$ {inss:.2f}")
print(f"Sindicato (5%)    : R$ {sindicato:.2f}")
print(f"Salário Líquido   : R$ {salario_liquido:.2f}")
