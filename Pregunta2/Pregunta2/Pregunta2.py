#Realice una función o procedimiento para insertar ordenadamente en un árbol binario. 
#Asimismo, realice una función que determine cual es la ruta del árbol para llegar 
#desde la raíz hasta el último nodo en el nivel más bajo. (5 puntos)

class arbol(object):
  def __init__(self):
    self.dato  = None
    self.derecha = None
    self.izquierda  = None
    

def insertar(nodo, dato):

    if nodo.dato == None:
        nodo.dato = dato

    if nodo.izquierda is None and dato < nodo.dato:
        nuevo = arbol()
        nodo.izquierda = nuevo
        nuevo.dato = dato

    if nodo.izquierda != None and dato < nodo.dato:
        insertar(nodo.izquierda, dato)

    if nodo.derecha is None and dato > nodo.dato:
        nuevo = arbol()
        nodo.derecha = nuevo
        nuevo.dato = dato

    if nodo.derecha != None and dato > nodo.dato:
        insertar(nodo.derecha, dato)

def numeroNodos(nodo):
    if (nodo==None):
        return 0
    else:
        return 1 + numeroNodos(nodo.izquierda) + numeroNodos(nodo.derecha)


def nivelMasbajo(nodos):
    print(nodos.dato)

    if(nodos.izquierda!=None or nodos.derecha!=None):
        if(numeroNodos(nodos.derecha) < numeroNodos(nodos.izquierda)):
            nivelMasbajo(nodos.izquierda)
        else:
            nivelMasbajo(nodos.derecha)


raizP = arbol()

insertar(raizP, 8)
insertar(raizP, 2)
insertar(raizP, 1)
insertar(raizP, 11)
insertar(raizP, 15)
insertar(raizP, 4)
insertar(raizP, 5)



print("----------------")
print("----------------")
print("----------------")
print("La ruta del árbol para llegar desde la raíz (" + str(raizP.dato) + ") hasta el último nodo en el nivel más bajo es:")
nivelMasbajo(raizP)
print("----------------")
print("----------------")
print("----------------")
