"""
16.	Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math
area = float(input("Informe o tamanho da área a ser pintada (em m²): "))
litros_necessarios = area / 3
latas = math.ceil(litros_necessarios / 18)
preco_total = latas * 80.00
print("\n------ ORÇAMENTO ------")
print(f"Área a pintar          : {area:.2f} m²")
print(f"Litros necessários     : {litros_necessarios:.2f} litros")
print(f"Latas de tinta (18L)   : {latas}")
print(f"Preço total            : R$ {preco_total:.2f}")
