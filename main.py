from si import Arbol

arbol = Arbol("Rosa")
arbol.agregar("Tulipán")
arbol.agregar("Gerbera")
arbol.agregar("Orquídea")
arbol.agregar("Margaritas")
flor = input("Ingresa una flor para agregar al árbol: ")
arbol.agregar(flor)
arbol.preorden()
arbol.inorden()
arbol.postorden()


#Aqui vamos a buscar algo en el árbol
busqueda = input("Busca una flor en el árbol: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")

gerbera = arbol.buscar("Gerbera")

if gerbera is not None:
    print("La gerbera existe")
else:
    print("La gerbera no existe")

arbol_num = Arbol(222222)
arbol_num.agregar(10)
arbol_num.preorden()
arbol_num.inorden()
arbol_num.postorden()
arbol.agregar(arbol_num)
num = input("Ingresa un numerito para agregar al árbol: ")

busqueda = int(input("Ingresa un número para buscar en el árbol: "))
n = arbol_num.buscar(busqueda)
if n is None:
    print(f"{busqueda} Este número no lo encontramos")
else:
    print(busqueda)