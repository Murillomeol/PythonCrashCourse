pizzas = ['Strogonoff', 'Atum', 'Quatro Queijos', 'bacon']

friend_pizzas = pizzas[:]

pizzas.append('Portuguesa')
friend_pizzas.append('Vegetariana')
print(f'Minhas pizzas favoritas são:')
for pizza in pizzas:
    print(pizza.title())

print(f'\nAs pizzas favoritas dos meus amigos são:')
for pizzafriend in friend_pizzas:
    print(pizzafriend.title())