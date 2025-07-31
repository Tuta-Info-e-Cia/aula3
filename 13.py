"""13.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
•	Para homens: (72.7*h) - 58
•	Para mulheres: (62.1*h) - 44.7"""

altura = float(input("Digite sua altura em metros (ex: 1.75): "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal para homem: {peso_ideal:.2f} kg")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal para mulher: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
    