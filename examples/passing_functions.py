def methodeception(another):
    return another()

def add_method():
    return 77 + 33

print(methodeception(add_method))

print(methodeception(lambda: 77 + 33))


mi_lista = [13, 56, 77, 480]
#genera una lista donde se quita el numero 13
print(list(filter(lambda x: x != 13, mi_lista)))

"""Las siguientes dos funciones son identicas
es mas facil utilizar las funcion lambda en algunos 
casos de progamacion funcional"""

print((lambda x: x * 3)(5))

def f(x):
    return x * 3

print(f(5))
