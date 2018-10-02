def how_do_you_know():
    #ask the user for a list of people they know
    #split the string into a list
    #return that list
    list_names = []
    siguiente = True
    while siguiente == True:
        name = input('Ingrese el nombre de un conocido: ')
        list_names.append(name)
        check = input('Desea ingresar otro nombre? S/N: ')
        if check == 'N':
            siguiente = False
    return list_names

def how_do_you_know_2():
    names = input('Ingrese los nombres de las personas, separados por comas: ')
    list_names = names.split(',') 
    #Aque tenemos el problema de si se ponen espacios
    #strip quita de los strings caracteres no visibles
    lista_names_sin_espacios = [name.strip() for name in list_names]
    # for gente in list_names: 
    #     lista_names_sin_espacios.append(gente.strip()) 
    return lista_names_sin_espacios

def ask_user(list_names):
    #Ask user for a name
    #see if their name is in the list of people they know
    #Print out that they know te person
    name = input('Ingrese un nombre: ')
    if name in list_names:
        print('Conoces a {}'.format(name))
    else:
        print('No conoces a {}'.format(name))

ask_user(how_do_you_know_2())