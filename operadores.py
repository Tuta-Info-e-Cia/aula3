""" # adição
"""
adicao = 2+2
print('Adição =>', adicao)

subtracao = 2-2
print('Subtração =>', subtracao)

multiplicacao = 2*2
print('Multiplicação =>', multiplicacao)

divisao = 2/2
print('Divisão =>', divisao)

divisao_inteira = 10//3 #retona apenas a parte inteira da conta ignorando as casas decimais virgulas dizimas e etc....
print ('Divisão Inteira ==>', divisao_inteira)

exponenciacao =2**10
print('Exponenciação ==>>>', exponenciacao)

modulo = 55 % 2 #resto da divisão - pra saber se o numero é par ou se é impar observase o resto da conta pela operação do modulo
print('Módulo x=>', modulo)

concatenacao = 'Senac' + 'Curso Python'
print(concatenacao)

teste = adicao + subtracao
print(teste)

cinco_vezes_a = 5 * 'a'
print(cinco_vezes_a)

#precedencia
#180 +20 /2 => 190
#(180+20)/2=> 100
"""
1 - (primeiro a resolver são os parenteses pela ordem de precedencia)
2 - **
3 - /  //  *  %

Quando nao coloca parenteses ele prioriza as multiplicaçoes divisoes e potencias ao inves das outras operacoes de contas
quando há o parenteses ele prioriza pela ordem de precedencia da matematica(escolinha da tia cotinha, vulgo primario kkkk) realizando primeiro as contas dentro do parenteses
depois de resolver o que esta entre parenteses que ele faz as demais contas necessarias
"""

