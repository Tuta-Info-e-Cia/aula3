nome = 'André'
peso = 78
altura = 1.89
imc = peso / altura **2
print(nome, 'tem', altura, 'de altura', ',pesa,', peso,'Kg'  '-'  'portanto seu IMC atual é =>>', imc)

#processamento
#imprimir na tela usando o fstring ao inves do print



#f-strings
print(f'{nome} tem, {altura}, de altura, pesa: {peso} Kg - portanto seu IMC atual é =>>{imc:.2f}')