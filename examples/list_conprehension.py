#forma de crear listas, de forma programatica
an_equal_list = [x for x in range(5)]
print(an_equal_list)

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

even_list = [n for n in range(10) if n % 2 == 0]
print(even_list)

people_you_know = ['Rolf ', ' John', 'anna', 'GREG']
normalised_people = [people.strip().lower() for people in people_you_know]
print(normalised_people)

