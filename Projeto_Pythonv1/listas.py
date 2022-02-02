# lista = []
# temp = lista[:]
# user = dict()
# nome = 'pk'
# for c in range(0, 3):
#     lista.append(int(input('num: ')))
#     temp.append(lista[0])
#     user[nome] = temp
#     lista.clear()
# print(f'Temp = {temp}\nLista = {lista}\nUser = {user}')

# quardar todos os dados dos úsuarios
dados = list()

# salva temporariamente os dados de um úsuario
pessoas = dict()

# salva temporariamente os nomes das músicas de um úsuario
nome_music = list()

nome = str(input('Seu nome: '))
titulo = str(input('Titulo: '))
pessoas['nome'] = nome
nome_music.append(titulo)
pessoas['titulo'] = nome_music[:]
dados.append(pessoas.copy())
nome_music.clear()
pessoas.clear()
print(f'Pessoas = {pessoas}\nNome das músicas = {nome_music}\nDados = {dados}')
while True:
    pessoas['nome'] = str(input('your name: '))
    nome_music.append(str(input('Name music: ')))
    pessoas['titulo'] = nome_music[:]
    dados.append(pessoas.copy())
    nome_music.clear()
    pessoas.clear()
    stop = str(input('Quer add mais uma música?: '))
    if stop == 'n':
        break
    print(dados)
    op = str(input('escolha alguem: '))
    for limpa in dados:
        if op in limpa.values():
            print('SIIIIIIIIIIIIIIIIIIIIIIM')
            op = str(input('O que você quer alterar: '))
            if op in limpa.keys():
                print('yes')
                for user in dados:
                    for k, v in user.items():
                        if k == 'titulo':
                            v.append(str(input('Nome da música: ')))
    print(dados)
