# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and
# ⋁ - or
# ¬ - not

# print('Проверка истинности выражения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')    

x = bool(int(input('Введите X: ')))
y = bool(int(input('Введите Y: ')))
z = bool(int(input('Введите Z: ')))

print(f'x,y,z : {x}, {y}, {z}') 

exp1 = not(x or y or z)
exp2 = (not x) and (not y) and (not z)

print(f'exp1 = {exp1}')
print(f'exp2 = {exp2}')

if(exp1 == exp2):
    print('Утверждение истинно!!!')
else:
    print('Утверждение НЕ истинно')
