
#EJERCICIO:
"""  
* - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" 
 
 """

#Python url: https://docs.python.org/3/

# Comentario de una linea

""" 
Comentario
de multiples líneas
"""

language = 'Python'

myStr : str= 'este es un string, aunque el lenguaje es dinamico podemos dar un hint del tipo de dato con los :'

myInt : int = 22

myFloat : float = 2.2

myList : list = [1,2,3,4,5]

myDict : dict = {'name':'Milagros'}

myTuple : tuple = (1, 2, 3, 4, 6)

myBoolean : bool = True

mySet : set = {'Milagros', 22}

print(f'Hola {language}!')