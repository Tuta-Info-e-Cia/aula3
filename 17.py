"""
17.	Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
•	comprar apenas latas de 18 litros;
•	comprar apenas galões de 3,6 litros;
•	misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

import math
area = float(input("Informe o tamanho da área a ser pintada (em m²): "))
area_com_folga = area * 1.10
litros_necessarios = area_com_folga / 6
preco_lata = 80.00
preco_galao = 25.00
litros_por_lata = 18
litros_por_galao = 3.6
qtde_latas = math.ceil(litros_necessarios / litros_por_lata)
preco_total_latas = qtde_latas * preco_lata
qtde_galoes = math.ceil(litros_necessarios / litros_por_galao)
preco_total_galoes = qtde_galoes * preco_galao
qtde_latas_misto = math.floor(litros_necessarios / litros_por_lata)
litros_restantes = litros_necessarios - (qtde_latas_misto * litros_por_lata)
qtde_galoes_misto = math.ceil(litros_restantes / litros_por_galao)
preco_total_misto = (qtde_latas_misto * preco_lata) + (qtde_galoes_misto * preco_galao)
print("\n------ ORÇAMENTO DE TINTA ------")
print(f"Área com folga (10%): {area_com_folga:.2f} m²")
print(f"Litros necessários  : {litros_necessarios:.2f} L\n")

print("1) Apenas latas de 18L:")
print(f"   Quantidade: {qtde_latas} lata(s)")
print(f"   Preço total: R$ {preco_total_latas:.2f}")

print("\n2) Apenas galões de 3.6L:")
print(f"   Quantidade: {qtde_galoes} galão(ões)")
print(f"   Preço total: R$ {preco_total_galoes:.2f}")

print("\n3) Mistura de latas e galões (menor preço):")
print(f"   {qtde_latas_misto} lata(s) e {qtde_galoes_misto} galão(ões)")
print(f"   Preço total: R$ {preco_total_misto:.2f}")
