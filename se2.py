entrada = input('Voce quer[entrar ou sair]?')
entrada = entrada.lower()
print(entrada)

if entrada == 'entrar':
    print("Seja bem Vindo, Você entrou no sistema")
elif entrada == 'sair':
    print('Você saiu do sistema...')
else:
    print('Você não escolheu entre entrar nem sair, por favor recomece e escolha a opção desejada...')
