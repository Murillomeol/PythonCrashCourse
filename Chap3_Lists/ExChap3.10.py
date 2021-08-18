muscles = ['Bíceps', 'Tríceps', 'Deltóides', 'Trapézio', 'Quadríceps']
print(muscles)
print(f'{muscles[2]} são o ponto forte do meu corpo.')
print(f'{muscles[-4]} são o ponto fraco do meu corpo.')

muscles[-2] = 'Peitoral'
print(muscles)

muscles.append('Isquiotibiais')
print(muscles)

muscles.insert(3, 'Trapézio')
print(muscles)

del muscles[-1]
print(muscles)

popped_muscles = muscles.pop()
print(muscles)
print(popped_muscles)

muscles.remove('Bíceps')
print(muscles)

muscles.sort()
print(muscles)
muscles.sort(reverse=True)
print(muscles)

print(sorted(muscles))
print(sorted(muscles, reverse=True))

muscles.reverse()
print(muscles)
muscles.reverse()
print(muscles)

print(len(muscles))