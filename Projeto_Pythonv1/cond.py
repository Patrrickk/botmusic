import csv

header = ['user', 'musica']
dados = []
with open('dados//este.csv', 'r') as ds:
    reade = csv.reader(ds)
    opt = input('1: para sair | 2: para cadastrar')

    while opt != '1':
        nome = input('Qual é seu user: ')
        musica = input('Qual música: ')
        for row in reade:
            print(row)
            if nome not in row:
                dados.append([nome, musica])
        opt = input('1 > para sair | 2: para cadastrar')


with open('dados\este.csv', 'w', encoding='utf-8', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)
# with open('dados\este.csv', 'r') as ds:
#     csv_reader = csv.reader(ds, delimiter=',')
#     for row in csv_reader:
#         print(row)


