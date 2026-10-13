class libro: #crearemos la clase libro.
    def __init__(self, titulo, num_paginas): #definiremos el metodo constructor con los atributos de titulo y num_paginas.
        self.titulo = titulo #se guardara el titulo del libro.
        self.num_paginas = num_paginas #se guardara el numero de paginas del libro.

    def __str__(self): # Este es un metodo especial que representara el objeto como texto.
        return f"Libro: {self.titulo}, Páginas: {self.num_paginas}" #se regresara la informacion del libro en formato de texto.

    def __len__(self): # Este es un metodo especial que permitira obtener la longitud del objeto.
        return self.num_paginas #se regresara el numero de paginas del libro.

libro1 = libro("Cien años de soledad", 471) #crearemos un objeto con el titulo de cien años de soledad y un numero de paginas de 471 como ejemplo.
print(libro1) #se imprimira la informacion del libro utilizando el metodo str.
print("Número de páginas:", len(libro1)) #se imprimira el numero de paginas del libro utilizando el metodo len.

