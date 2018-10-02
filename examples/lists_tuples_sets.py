list_grade = [77, 80, 90, 95, 100]
tuple_grade = (77, 89, 75, 62, 88) #INMUTABLES
set_grade = {10, 12, 9, 44, 99, 32, 10} # unicos, no ordenables
#set quieta automaticamente los repetidos

print(sum(list_grade) / len(list_grade))

list_grade.append(99)

print(list_grade[4])
list_grade[4] = 50
print(list_grade[4])


print(sum(list_grade) / len(list_grade))

tuple_grade = tuple_grade + (100,)
print(tuple_grade)

set_grade.add(11)
print(set_grade)
set_grade.add(11)
print(set_grade)


## set operations 'Conjuntos'

set_names = {'Emiliano', 'Emiliano', 'manuel', 'Manuel'}
print(set_names)

your_lottery_num = {1, 2, 3, 4, 5}
winning_num = {1, 3, 5, 7, 8, 11}

#numeros que pertenecen a ambos conjuntos
print(your_lottery_num.intersection(winning_num))
#union
print(your_lottery_num.union(winning_num))
#dirrerence, los que no pertenecen al segundo conjunto
print(your_lottery_num.difference(winning_num))


