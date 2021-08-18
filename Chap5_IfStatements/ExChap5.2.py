#Teste para igualdade e desigualdade com strings:
print(f'Teste com igualdade:') #True e false respectivamente
nome = 'Maria'
print(nome == 'Maria')
print(nome == 'Mara')

print(f'\nTeste com desigualdade:') #True e false respectivamente
cor = 'Azul'
print(cor != 'Roxo')
print(cor != 'Azul')

print(f'\nTeste com lower():')
cor = 'Azul'
print(cor.lower() == 'azul')
print(cor.lower() == 'preto')

print(f'\nTeste numéricos:')
print('Igualdade:')
n = 1
print(n == 1)
print(n == 5)

print(f'\nDesigualdade:')
n = 100
print(n != 10)
print(n != 100)

print(f'\nMaior que:')
n = 150_000
print(n > 149999)
print(n > 150001)

print(f'\nMenor que:')
n = -500
print(n < -499)
print(n < -501)

print(f'\nMaior ou igual que:')
n = 0
print(n >= 0)
print(n >= 1)

print(f'\nMenor ou igual que:')
print(n <= 10)
print(n <= -1)

print(f'\nTestes usando and:')
n0 = 0
n1 = 1
print(n0 == 0 and n1 == 1)
print(n0 <= 0 and n1 <= 0)

print(f'\nTeste usando or:')
print(n0 >= 0 or n1 <= 0)
print(n0 >= 1 or n1 <= 0)

print(f'\nTeste usando is in:')
cores = ['Azul', 'Vermelho', 'Amarelo']
print('Azul' in cores)
print('azul' in cores)

print(f'\nTeste usando not:')
print('azul' not in cores)
print('Azul' not in cores)