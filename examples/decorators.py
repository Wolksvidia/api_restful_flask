"""Los decoradores son funciones que embuelven a una funcion principal para agregar una
cierta funcionalidad adicional"""

import functools

def my_decorator(function):
    @functools.wraps(function)
    def function_that_runs_function():
        print("In the Decorator!!!")
        function()
        print("After the Decorator!!!")
    return function_that_runs_function


@my_decorator
def my_function():
    print("I am the Function!!!")

my_function()

##
"""Por ejemplo los decoradores con parametros se pueden utilizar para pasar los permisos de 
un usuario al momento de ejecutar una funcionalidad de un website"""

def decorator_with_args(number):
    def my_decorator(function):
        @functools.wraps(function)
        def function_that_runs_function(*args, **kwargs):
            """si la funcion decorada tiene parametros lleva args y kwargs.Esta es la funcion 
            que reemplaza y ejecuta a la funcion decorada"""
            print("In the Decorator!!!")
            if number == 56:
                print("Not running the function!!")
            else:
                function(*args, **kwargs)
            print("After the Decorator!!!")
        return function_that_runs_function
    return my_decorator

@decorator_with_args(57)
def my_function_too(x,y):
    print('Hello!!!')
    print(x + y)

my_function_too(10,100)