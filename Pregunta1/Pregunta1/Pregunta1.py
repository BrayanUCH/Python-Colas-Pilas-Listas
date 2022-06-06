class arbol(object):
    def __init__(self):
        self.derecha = None
        self.izquierda = None
        self.dato = None

class Cola:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def vacia(self):
        return self.items == []
    def len(self):
        return len(self.items)
    def imprimirCola(self):
        print(self.items)
    def devolverDato(self,i):
        return self.items[i]

def preorden(nodo):
     if nodo!= None:
          print (nodo.dato)#esta es la raiz 
          preorden(nodo.izquierda)
          preorden(nodo.derecha)


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

def buscar(nodo,valor,cola,posicion):
     if nodo is not None:
         if valor == nodo.dato and posicion == "IZQUIERDA" and nodo.izquierda is not None:
            cola.push(nodo.izquierda.dato)
            return True

         if valor == nodo.dato and posicion == "DERECHA" and nodo.derecha is not None:
            cola.push(nodo.derecha.dato)
            return True

         buscar(nodo.izquierda,valor,cola,posicion)
         buscar(nodo.derecha,valor,cola,posicion)
     else: 
         return False



def pisos(nodo,cola,j):
    print("NIVEL #"+str(j))
    cola.imprimirCola()
    aux=Cola()
    print()
    for i in range(cola.len()):
        
        valor=cola.devolverDato(i)

        buscar(nodo,valor,aux,"IZQUIERDA")
        buscar(nodo,valor,aux,"DERECHA")       

    if(aux.vacia()==False):
        return pisos(nodo,aux,j+1)
    else:
        return "END"
    

raiz=arbol()
cola=Cola()

insertar(raiz, 8)
insertar(raiz, 2)
insertar(raiz, 1)
insertar(raiz, 11)
insertar(raiz, 15)
insertar(raiz, 4)
insertar(raiz, 5)


print("RAIZ")
print("["+str(raiz.dato)+"]")
print()
aux=buscar(raiz,raiz.dato,cola,"IZQUIERDA")
aux=buscar(raiz,raiz.dato,cola,"DERECHA")
if(raiz.derecha is not None or raiz.izquierda is not None):
    print(pisos(raiz,cola,1))

print()
print()
print()
print("Que pasaría si en lugar de colas en la función anterior se tienen pilas, suponiendo que la función esta correcta.")
print()
print("    Cumpliría con el propósito del código (pregunta #1), sin embrago sería necesario reestructurar partes del código,")
print("ya que en el manejo varia un poco de uno al otro, porque en la pila respeta el orden es el último que entra ")
print("es el primero en salir pero en la cola el orden es el primero en entrar es el primero en salir. ")
print()



















#class Cola:
#    def __init__(self):
#        self.dato = None
#        self.next = None
#
#def push(cola, valor):
#    aux=Cola()
#
#    aux.dato=valor
#
#    """ Agrega el elemento x como último de la cola. """
#    cola.append(valor)
#
#def pop(cola):
#    """ Elimina el primer elemento de la cola y devuelve su
#        valor. Si la cola está vacía, levanta ValueError. """
#    try:
#        return cola.pop(0)
#    except:
#        print("La cola está vacía")







