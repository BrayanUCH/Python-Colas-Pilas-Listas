#• Un nodo X se almacena en la posición K, correspondiente del arreglo.
#• El hijo izquierdo del nodo K se almacena en la posición 2*K.
#• El hijo derecho del nodo K se almacena en la posición 2*k+1

class arbol(object):
  def __init__(self):
    self.dato  = None
    self.derecha = None
    self.izquierda  = None



#k=posicion
def insertar(nodo,k,vec1):
    if(nodo.dato==None):
        nodo.dato=vec1[0]

    k1 = 2*k
    if(k1-1<len(vec1) and vec1[k1-1] != None):
        nuevo = arbol()
        nodo.izquierda = nuevo
        nuevo.dato = vec1[k1-1]

    k2 = 2*k+1
    if(k2-1<len(vec1) and vec1[k2-1] != None):
        nuevo = arbol()
        nodo.derecha = nuevo
        nuevo.dato = vec1[k2-1]

    if nodo.izquierda != None:
        insertar(nodo.izquierda,k1,vec1)
    if nodo.derecha != None:
        insertar(nodo.derecha,k2,vec1)




def preorden(nodo):
     if nodo!= None:
          print (nodo.dato) 
          preorden(nodo.izquierda)
          preorden(nodo.derecha)

raiz=arbol()
vec=[70,67,75,66,69,73,86,None,None,68,None,None,None,None,93]
#raiz.dato = vec[0]

insertar(raiz,1,vec)
print("Preorden")
preorden(raiz)



