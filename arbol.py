class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def agregar(self, dato):
        nodo = self.raiz
        while True:
            if dato < nodo.dato:
                if nodo.izquierda is None:
                    nodo.izquierda = Nodo(dato)
                    break
                else:
                    nodo = nodo.izquierda
            else:
                if nodo.derecha is None:
                    nodo.derecha = Nodo(dato)
                    break
                else:
                    nodo = nodo.derecha

    def inorden(self):
        pila = []
        nodo = self.raiz
        print("Imprimiendo árbol inorden: ")
        while True:
            while nodo is not None:
                pila.append(nodo)
                nodo = nodo.izquierda
            if len(pila) == 0:
                break
            nodo = pila.pop()
            print(nodo.dato)
            nodo = nodo.derecha

    def preorden(self):
        pila = [self.raiz]
        print("Imprimiendo árbol preorden: ")
        while len(pila) > 0:
            nodo = pila.pop()
            print(nodo.dato)
            if nodo.derecha is not None:
                pila.append(nodo.derecha)
            if nodo.izquierda is not None:
                pila.append(nodo.izquierda)

    def postorden(self):
        pila = []
        visitados = set()
        nodo = self.raiz
        print("Imprimiendo árbol postorden: ")
        while True:
            while nodo is not None and nodo in visitados:
                nodo = pila.pop()
            if nodo is None:
                break
            visitados.add(nodo)
            pila.append(nodo)
            if nodo.izquierda is not None:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
        while len(pila) > 0:
            nodo = pila.pop()
            print(nodo.dato)

    def buscar(self, busqueda):
        nodo = self.raiz
        while nodo is not None:
            if nodo.dato == busqueda:
                return nodo
            if busqueda < nodo.dato:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
        return None
