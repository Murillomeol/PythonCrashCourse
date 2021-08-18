convite_jantar = ['Tonioli', 'Conrado', 'Bumstead', 'Muzy']
print(f'Olá, {convite_jantar[0]}! Você está convidado para um jantar.')
print(f'Olá, {convite_jantar[1]}! Você está convidado para um jantar.')
print(f'Hello, {convite_jantar[-2]}! You are invited for a dinner.')
print(f'Olá, {convite_jantar[-1]}! Você está convidado para um jantar.\n')

popped_convidados = convite_jantar.pop(2)
print(f'Uma pena que nosso convidado {popped_convidados} não poderá comparecer.\n')
convite_jantar.insert(2, 'Breon')

print(f'Olá, {convite_jantar[0]}! Você está convidado para um jantar.')
print(f'Olá, {convite_jantar[1]}! Você está convidado para um jantar.')
print(f'Hello, {convite_jantar[-2]}! You are invited for a dinner.')
print(f'Olá, {convite_jantar[-1]}! Você está convidado para um jantar.\n')
