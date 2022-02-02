import csv
dados = ['patrick']
with open('C:/Users/Patrick/Desktop/mm.csv', 'w', newline='') as arquivo:
    add = csv.writer(arquivo)
    add.writerow(['User', 'Links', 'Músicas'])
    add.writerow(dados)
with open('C:/Users/Patrick/Desktop/mm.csv', 'r') as arquivo:
    leitor = arquivo.read()
    print(leitor)
