familia = ['Murillo', 'Jordana', 'Getulio', 'Marcos', 'Elizabete']
print (familia)
print(familia[4])
print(familia[-1])

mensagem = f'O {familia[2].title()} é o filho mais velho.'
print(mensagem)

print('\n#Alterando itens em uma lista')
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
carros[-1] = 'Civic'
print(carros)

print('\n#Adicionando itens no final de uma lista')
carros.append('Sandero')
print(carros)

print('\n#Preenchendo uma lista do zero.')
carro = []
carro.append('Corola')
carro.append('Monza')
carro.append('Cerato')
print(carro)

print('\nAdicionando itens no meio de uma lista.')
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
carros.insert(1,'Logan')
print(carros)

print('\n#Removendo itens de uma lista pelo index.')
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
print(carros)
del carros[1] #Utiliza-se 'del' quando se sabe a posição do item na lista.
print(f'{carros}\n\nMétodo pop:')

carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
popped_carros = carros.pop() #Remove o ultimo item da lista. Ou pop(x) para remover index x.
print(carros)
print(popped_carros) #Permite o armazenamento do item removido.
popped_carros = carros.pop()
print(carros)
print(popped_carros)

print('\n#Removendo itens de uma lista pelo seu valor.')
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
print(carros)
carros.remove('Celta')
print(carros)

print('\n#Sorting a list: ordem alfabética.') 
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
carros.sort() #Muda a lista permanentemente.
print(carros)
print('\n#Sorting a list: ordem reversa alfabética.')
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
carros.sort(reverse=True) #Muda a lista permanentemente.
print(carros)

print('\n#Sorting a list com "sorted":') 
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
print(f'Lista original: {carros}.')
print(f'Lista modificada com sorted: {sorted(carros)}.')
print(f'Lista original novamente: {carros}.')

print('\n#Invertendo a ordem de uma lista:')
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
print(carros)
carros.reverse()
print(carros)

print('\n#Encontrando o comprimento de uma lista:')
carros = ['Voyage', 'Celta', 'Cobalt', 'Sandero'] 
print(len(carros))

