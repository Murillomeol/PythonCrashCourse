magicos = ['Phil', 'máscara', 'DAVID']
for magico in magicos: 
#"magico" trata-se do nome da variável. 
#Recomendado escolher uma que represente os itens da lista.
    print(magico)

for magico in magicos:
    print(f'{magico.title()} esta foi uma excelente truque!')
    print(f'Mal posso esperar para ver seu próximo truque, {magico.title()}!\n')
print('Obrigado a todos. Este foi um show muito bom!\n')

print('\n#FUNÇÃO RANGE')
for value in range(-2,5):
    print(value)

print('\n#USANDO FUNÇÃO RANGE PARA CRIAR UMA LISTA:')
numeros = (list(range(-7,8,2)))
print(numeros)

quadrados = []
for valor in range(0,11):
    quadrados.append(valor ** 2)
print(quadrados)

print(f'\n#FUNÇÕES DO PYTHON:')
digitos = [0,1,2,5,-7]
print(f'sum:{sum(digitos)}')
print(f'min:{min(digitos)}')
print(f'max:{max(digitos)}')

print('\n#COMPREENSÕES DE LISTAS:')
quadrados = [valor ** 2 for valor in range(0,11)]
print(quadrados)

print(f'\n#PARTES DE UMA LISTA:')
jogadores = ['José', 'Cristiano', 'Neymar', 'Messi', 'Aldo']
print(jogadores[1:4])
print(jogadores[:4])
print(jogadores[1:])
print(jogadores[-3:])

print(f'\n#LOOPING:')
jogadores = ['José', 'Cristiano', 'Neymar', 'Messi', 'Aldo']
for jogador in jogadores[:3]:
    print(f'{jogador} é um ótimo jogador.') 

print(f'\n#COPIANDO LISTAS.')
comidas_preferidas = ['Batata doce', 'Frango', 'Camarão', 'Leite', 'Ovo']
preferidas_familia = comidas_preferidas[:]
print(preferidas_familia)

print(f'\n#TUPLAS.')
dimensões = (100, 50, 60,)
print(dimensões[0])
print(dimensões[-1])
for medida in dimensões:
    print(medida)
#Não é possível alterar um item da tupla, 
#Mas é possível modificar ela inteira.
print(f'\nAlterando os valores de uma tupla:')
dimensões = (1, 2, 3,) #Nova tupla para a variável "dimensões"
print(dimensões[0])
print(dimensões[-1])
for medida in dimensões:
    print(medida)