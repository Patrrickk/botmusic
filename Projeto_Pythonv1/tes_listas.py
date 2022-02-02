import requests
header = ['user', 'musica']
verificacao = []
dados = []

stop = input('Sair = 1 | Cadastrar = 2: ')
while stop != '1':
    nome = str(input('Seu nome: '))
    music = str(input('Nome da música: '))
    if nome not in dados:
        print('ok')
        verificacao.append(nome)
        if music not in dados:
            verificacao.append(music)
    else:
        print('usuario já cadastrado')
    dados.append(verificacao[:])
    verificacao.clear()
    print(dados)
    stop = input('Sair = 1 | Cadastrar = 2: ')
