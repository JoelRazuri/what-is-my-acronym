"""
    Vamos a pedir al usuario que ingrese el significado completo de una organización o concepto y con ello como resultado obtendremos el acrónimo. 
    Por ejemplo:
        Entrada -> As Soon As Possible. Salida -> ASAP.
        Entrada -> World Health Organization. Salida -> WHO.
        Entrada -> Absent Without Leave. Salida -> AWOL.
"""

import os 



def validar_frase(frase):

    continuar = True
    i = 0

    while i<len(frase) and continuar:

        if not ((frase[i]>='A'and frase[i]<='Z') or (frase[i]>='a' and frase[i]<='z') or frase[i]=="*" or frase[i]==" "):
            continuar = False
        i+=1

    return continuar



def ingreso_frase():

    continuar = False
    
    while not continuar:
        os.system("cls")
        frase = input("Ingrese nombre de una organización o concepto (para salir *): ")
        continuar = validar_frase(frase)
        if not continuar:
            print("Error, ingrese solo letras.")
            input("...")
            os.system("cls")

    return frase


def buscar_acronimo(frase,acronimo_lista):

    frase = frase.title()

    for i in range(len(frase)):

        if (frase[i]>='A' and frase[i]<='Z'):
            acronimo_lista.append(frase[i])


def mostrar_acronimo(acronimo_lista):

    print("Acronimo:",end=" ")
    for i in range(len(acronimo_lista)):

        print(acronimo_lista[i],end="")
    print()
    input("Toque cualquier tecla para seguir...")

def menu():

    continuar = True
    
    while continuar:
        frase = ingreso_frase()
        
        if frase=="*":
            continuar = False
        else:
            acronimo_lista=[]
            buscar_acronimo(frase,acronimo_lista)
            mostrar_acronimo(acronimo_lista)




if __name__=="__main__":
    menu()