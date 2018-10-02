should_continue = True
if should_continue:
    print('Hello!')

known_people = ['Mario', 'Jose', 'Pepito']

person = input('Ingrese a la persona que conoce: ')

if person in known_people:
    print('Conoces a {}!'.format(person))
else:
    print('No conoces a {}!'.format(person))
# if person not in known_people:
#     print('Tu no conoces a esta persona!')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(even_numbers())