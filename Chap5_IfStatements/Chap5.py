carros = ['audi', 'mitsubish', 'bmw', 'toyota']
for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())

name = 'Audi'
if name in carros:
    print(True)
else:
    print(False)

print(f'\n#IF:')
idade = int(input('Digite a idade: '))
if idade >= 16:
    print('Você está apto para votar')
    print('Você já fez seu titulo de eleitor?')
else:
    print('Você é muito novo para votar.')
    print('Por favor, registre-se quando completar 16!')

print(f'\n#IF-ELIF-ELSE:')
if idade < 4:
    print('Sua entrada custa 0$')
elif idade < 18:
    print('Sua entrada custa 25$')
elif idade < 65:
    print('Sua entrada custa 40$')
else:
    print('Sua entrada custa 20$')

#Outra forma de escrever:
if idade < 4:
    preço = 0
elif idade < 18:
    preço = 25
elif idade < 65:
    preço = 40
else:
    preço = 20
print(f'A sua entrada custa {preço}$')