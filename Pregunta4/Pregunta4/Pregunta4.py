class arbol(object):
  def __init__(self):
    self.dato  = None
    self.derecha = None
    self.izquierda  = None

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
        try:
            return self.items[i]
        except:
            return None

def Probabilidad(matriz,letraM,letram):
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #print(str(matriz[i][j]) + "")
            if(letraM==matriz[i][j] or letram==matriz[i][j]):
                contador+=1
    return contador/100

def ordenar(lista):

    for i in range(1,len(lista)):
        actual = lista[i]
        posicion = i

        while posicion > 0 and lista[posicion-1] > actual:
            lista[posicion] = lista[posicion-1]
            posicion = posicion - 1

        lista[posicion] = actual

def preorden(nodo):
     if nodo!= None:
          print (nodo.dato)
          preorden(nodo.izquierda)
          preorden(nodo.derecha)

def huffman(lista,raiz):
    lisArbol=Cola()

    if(lista.len()%2==0):
        mitad=int(lista.len()/2)
    else:
        mitad=int(lista.len()/2)
    ########################################################
    if(lista.len() != 2):
        i=0
        while(i < mitad):
            newArbol=arbol()

            if(lista.devolverDato(i) is not None ):

                if((lista.devolverDato(i+1) is not None and i+1 < mitad) and lista.devolverDato(i) is not None):
                    newArbol.dato=lista.devolverDato(i).dato + lista.devolverDato(i+1).dato 
                    newArbol.izquierda=lista.devolverDato(i)
                    newArbol.derecha=lista.devolverDato(i+1)

                if((lista.devolverDato(i+1) == None or i+1 >= mitad) and lista.devolverDato(i) is not None):
                    newArbol.dato=lista.devolverDato(i).dato

                if((lista.devolverDato(i+1) is not None and i+1 < mitad) and lista.devolverDato(i) == None):
                    newArbol.dato=lista.devolverDato(i).dato                    

                lisArbol.push(newArbol)
            i=i+2
        ########################################################
        i=mitad
        while(i < lista.len()):
            newArbol=arbol()

            if(lista.devolverDato(i) is not None):
                if((lista.devolverDato(i+1) is not None and i+1 < lista.len()) and lista.devolverDato(i) is not None):
                    newArbol.dato=lista.devolverDato(i).dato + lista.devolverDato(i+1).dato
                    newArbol.izquierda=lista.devolverDato(i)
                    newArbol.derecha=lista.devolverDato(i+1)

                if((lista.devolverDato(i+1) == None or i+1 >= lista.len()) and lista.devolverDato(i) is not None):
                    newArbol.dato=lista.devolverDato(i).dato

                if((lista.devolverDato(i+1) is not None  and i+1 < lista.len()) and lista.devolverDato(i) == None):
                    newArbol.dato=lista.devolverDato(i+1).dato

                lisArbol.push(newArbol)
            i=i+2
        huffman(lisArbol,raiz)
    else:
        raiz.dato=lista.devolverDato(0).dato + lista.devolverDato(1).dato
        raiz.izquierda=lista.devolverDato(0)
        raiz.derecha=lista.devolverDato(1)
        return True
        



Matriz=[["a","c","e","e","e","e","D","d","d","d"],
        ["b","a","e","e","e","e","B","b","b","d"],
        ["f","b","a","c","c","c","A","d","b","d"],
        ["f","c","b","a","c","c","A","d","b","d"],
        ["f","c","b","b","a","c","B","a","d","d"],
        ["f","c","e","a","b","c","B","d","a","e"],
        ["f","a","a","f","b","b","B","d","d","a"],
        ["f","f","f","f","b","c","C","d","d","d"],
        ["a","f","f","a","d","a","A","f","f","f"],
        ["f","a","a","f","a","a","D","a","a","f"]]

raiz=arbol()
cola=Cola()
a=0
b=0
c=0
d=0
e=0
f=0

a = Probabilidad(Matriz,"a","A")
b = Probabilidad(Matriz,"b","B")
c = Probabilidad(Matriz,"c","C")
d = Probabilidad(Matriz,"d","D")
e = Probabilidad(Matriz,"e","E")
f = Probabilidad(Matriz,"f","F")

lista=[a,b,c,d,e,f]
listaLetras=["a","b","c","d","e","f"]
print ("LISTA DE PROBABILIDADES:") 

i=0
while(i<len(lista)):
    print(listaLetras[i]+"-"+str(lista[i]))
    i+=1

print("TOTAL")
print(a+b+c+d+e+f)


ordenar(lista)
print ("VECTOR ORDENADO:") 
print(lista)
print()
print()
print()
######################################################################################
i=0
while(i<len(lista)):
    a=arbol()
    a.dato=lista[i]
    cola.push(a)
    i+=1
i=0


huffman(cola,raiz)
print()
print("PREORDEN DEL ARBOL DE HUFFMAN")
print()
preorden(raiz)
print()



