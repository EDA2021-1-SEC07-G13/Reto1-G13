"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo ")
    print("2- Consultar los Top X videos por views, pais y categoria ")
    print("3- Consultar video que más días ha sido trending para un país específico ")
    print("4- Consultar video que más días ha sido trending para una categoría específica ")
    print("5- Consultar el ranking X de vides con mas likes y tag especifico en un pais ")
    print("0- Salir")

def initCatalog(Tipo):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(Tipo)

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printcategoriesList(categoryID):
    size = lt.size(categoryID)
    listaC=[]
    if size:
        print('Esta es la lista de categorias: ')
        for i in categoryID['elements']:       
            listaC.append(i['id\tname'])
    for j in listaC:
        print(j)

def print1stelement(videos,tipo):
    primero=lt.firstElement(videos)
    print("Title: {} Channel: {} Trending Date: {} Country: {} Views: {} Likes: {} Dislikes: {}  ".format(primero['title'],primero["channel_title"],primero["trending_date"],primero["country"],primero["views"],primero["likes"],primero["dislikes"]))
def sortVideos(catalog, size,typesort):
    return controller.sortVideos(catalog, size,typesort)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        Tipo=None
        input2=input('Ponga 1 si quiere la representacion en tipo arreglo o 2 si la quiere con lista encadenada\n')
        print("Cargando información de los archivos ....")
        if int(input2)==1:
            Tipo='ARRAY_LIST'
        elif int(input2)==2:
            Tipo='LINKED_LIST'
        else:
            pass
        catalog = initCatalog(Tipo)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        
        videos=(catalog['videos'])
        print1stelement(videos,int(input2))
        categoryID = catalog['category-id']
        printcategoriesList(categoryID)
        

    elif int(inputs[0]) == 2:
        det=True
        while det==True:
            muestra=int(input("Por favor digite el numero de la muestra que desea organizar\n"))
            if muestra >lt.size(videos):
                det=True                
                print("Su muestra es muy grande digite otra cantidad")
            else:
                det=False
        eleccion=int(input("Por favor digite 1 si quiere un algrotivo iterativo\nPor favor digite 2 si quiere un algoritmo recursivo\n"))
        if eleccion==1:
            type_sort=int(input("Por favor digite 1 si quiere que su tipo de ordenamiento sea INSERTION\nPor favor digite 2 si quiere que su tipo de ordenamiento sea SELECTION\nPor favor digite 3 si quiere que su tipo de ordenamiento sea SHELLSORT\n"))
        elif eleccion==2:
            type_sort=int(input("Por favor digite 4 si quiere que su tipo de ordenamiento sea QUICK\nPor favor digite 5 si quiere que su tipo de ordenamiento sea MERGE\n"))
        print("Ordenando los videos... Por favor espere en linea")
        videos_ordenados=sortVideos(catalog,muestra,type_sort)
        tiempo=videos_ordenados[0]
        print("Para la muestra de ",muestra," elementos y con la estructura de datos tipo: ",Tipo," el tiempo que tardo el programa es: ",tiempo,"milisegundos.")
      
    
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    else:
        sys.exit(0)
sys.exit(0)
