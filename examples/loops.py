my_string = 'Hola Mundo'

for character in my_string:
    print(character)

lista = [1, 3, 5, 6, 7, 8]

for num in lista:
    print(num ** 2)

for num in range(10):
    print(num)

user_nuember = True
while user_nuember == True:
    print(10)
    user_input = input('Desea continuar? (y/n) ')
    if user_input == 'n':
        user_nuember = False
        