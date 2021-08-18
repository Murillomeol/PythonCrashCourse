convite_jantar = ['Marcos', 'Tonioli', 'Conrado', 'Elizabete', 'Bumstead', 'Muzy', 'Jordana']
print(f'Olá, {convite_jantar[0]}! Você está convidado para um jantar.')
print(f'Olá, {convite_jantar[1]}! Você está convidado para um jantar.')
print(f'Olá, {convite_jantar[2]}! Você está convidado para um jantar.')
print(f'Olá, {convite_jantar[3]}! Você está convidado para um jantar.')
print(f'Hello, {convite_jantar[4]}! You are invited for a dinner.')
print(f'Olá, {convite_jantar[5]}! Você está convidado para um jantar.')
print(f'Olá, {convite_jantar[-1]}! Você está convidado para um jantar.\n')

print('Poderei convidar apenas duas pessoas.\n')

popped_convite = convite_jantar.pop()
print(f'Peço desculpas {popped_convite}, mas não poderei mais te convidar para o jantar.')
popped_convite = convite_jantar.pop()
print(f'Peço desculpas {popped_convite}, mas não poderei mais te convidar para o jantar.')
popped_convite = convite_jantar.pop()
print(f'Peço desculpas {popped_convite}, mas não poderei mais te convidar para o jantar.')
popped_convite = convite_jantar.pop()
print(f'Peço desculpas {popped_convite}, mas não poderei mais te convidar para o jantar.')
popped_convite = convite_jantar.pop()
print(f'Peço desculpas {popped_convite}, mas não poderei mais te convidar para o jantar.\n')

print(f'{convite_jantar[0]}, você continua convidado para o jantar.')
print(f'{convite_jantar[1]}, você continua convidado para o jantar.\n')

del convite_jantar[1]
del convite_jantar[0]

print(convite_jantar)