def contador(ist):
   print(ist)


valores = {}
dados = []
for c in range(0, 2):
   valores['nome'] = str(input('NOme: '))
   dados.append(valores.copy())
   valores.clear()
   contador(dados)
print(dados[0]['nome'])
