"""
14.	João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
 deve pagar uma multa de R$ 4,00 por quilo excedente.
   João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
     Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
       Imprima os dados do programa com as mensagens adequadas.
"""

limite = 50.0  # quilos
multa_por_quilo = 4.00

peso = float(input("Digite o peso dos peixes (em kg): "))

if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_por_quilo
else:
    excesso = 0
    multa = 0

print(f"\nPeso informado: {peso:.2f} kg")
print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")
