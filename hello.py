#Funcion Recursiva que suma elementos de una lista
def sumaRecursiva(lista):
    if(not lista):
        return 0
    else:
        return lista[-1] + sumaRecursiva(lista[0:-1])
    
#sumaRecursiva = lambda lista: lista and (lista[-1] + sumaRecursiva(lista[0:-1])) or 0

def sumaFor(lista):
    respuesta = 0
    for elemento in lista:
        respuesta+=elemento
    return respuesta

def sumaWhile(lista):
    respuesta = 0
    i=0
    while i < len(lista):
        respuesta+=lista[i]
        i+=1
    return respuesta

def problema1(lista):
    print """  Problema 1
    Escriba tres funciones que sumen todos los numeros de una lista dada
        * Usando ciclo For
        * Usando Ciclo While
        * Usando Recursividad"""
    print "\n  Lista: "+str(lista)
    print "  Suma For: "+str(sumaFor(lista))
    print "  Suma While: "+str(sumaWhile(lista))
    print "  Suma Recursiva: "+str(sumaRecursiva(lista))

def problema2(lista1,lista2):
    print """  Problema 2
    Escriba una funcion que combine dos listas, alternando cada elemento.
        1. [ A , B , C ]
        2. [ 1 , 2 , 3 ]
    Dando como resultado [ A , 1 , B , 2 , C , 3 ]"""
    print "Lista1: "+str(lista1) +" \nLista2: "+str(lista2)
    print "Resultado: "+str(mezclarListas(lista1,lista2))

def mezclarListas(lista1,lista2):
    i=0
    resultado=[]
    largo=largoLista(lista1,lista2)
    while i < largo:
        if i < len(lista1):
            resultado.append(lista1[i])
        if i < len(lista2):
            resultado.append(lista2[i])
        i+=1
    return resultado

def largoLista(lista1,lista2):
    if len(lista1) > len(lista2):
        return len(lista1)
    else:
        return len(lista2)

lista= [1,2,3,5,6]
problema1(lista)
lista1= ["A","B","C"]
lista2= [1,2,3]
problema2(lista1,lista2)
