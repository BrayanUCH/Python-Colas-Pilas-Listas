#Realice una funciona en pyhton, sin usar recursión que permita contar cuantos nodos tiene un árbol,
#y decirlo de la siguiente manera: 5 total, 3 izquierda y 2 derecha. (5 pts)
class arbol(object):
  def __init__(self):
    self.dato  = None
    self.derecha = None
    self.izquierda  = None

def insertar(nodo, dato):

    if nodo.dato == None:
        nodo.dato = dato
        print(dato)
    ##########################################################
    if nodo.izquierda is None and dato < nodo.dato:
        nuevo = arbol()
        nodo.izquierda = nuevo
        nuevo.dato = dato

    if nodo.izquierda != None and dato < nodo.dato:
        insertar(nodo.izquierda, dato)
    ##########################################################
    if nodo.derecha is None and dato > nodo.dato:
        nuevo = arbol()
        nodo.derecha = nuevo
        nuevo.dato = dato

    if nodo.derecha != None and dato > nodo.dato:
        insertar(nodo.derecha, dato)


def numeroNodo(nodo):
    j=0
    nodo1=arbol()
    nodo2=arbol()
    aux=arbol()

    nodo1=nodo.izquierda
    nodo2=nodo.derecha

    if(nodo!=None):
        print (nodo.dato)
        j+=1
        while(nodo1!= None):

            aux=nodo1
            if nodo1!= None:
                j+=1
                print (nodo1.dato)

            nodo1 = nodo1.derecha
            while(nodo1!= None):
                if nodo1!= None:
                    print (nodo1.dato)
                    j+=1
                nodo1 = nodo1.derecha

            nodo1 = aux.izquierda
        #############################################################
        while(nodo2!= None):
       
            aux=nodo2
            if nodo2!= None:
                print (nodo2.dato)
                j+=1

            nodo2 = nodo2.izquierda
            while(nodo2!= None):
                if nodo2!= None:
                    print (nodo2.dato)
                    j+=1
                nodo2 = nodo2.izquierda
       
            nodo2 = aux.derecha
        return j
raizP = arbol()


insertar(raizP, 8)
insertar(raizP, 4)
insertar(raizP, 5)
insertar(raizP, 9)
insertar(raizP, 12)
insertar(raizP, 6)
insertar(raizP, 7)
insertar(raizP, 2)
insertar(raizP, 11)
insertar(raizP, 10)

j=numeroNodo(raizP.derecha)
i=numeroNodo(raizP.izquierda)

print("El el arbol cuenta con:")
print("-"+str(i)+" nodos a la izquierda.")
print("-"+str(j)+" nodos a la derecha.")
print("-Con un total de "+str(j+i+1)+" nodos contando al principal(raiz).")

