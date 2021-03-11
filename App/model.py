"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as she
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import insertionsort as inse
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(X):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'category-id': None,}
               

    catalog['videos'] = lt.newList(X)
    catalog['category-id'] = lt.newList('ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategoryID(catalog, category):
    lt.addLast(catalog['category-id'], category)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def cmpVideosByViews(video1,video2):
    comparison=float(video2['views'])<float(video1['views'])
    return comparison

def getBestVideos(catalog, number):

    videos = catalog['videos']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos

def cmpVideosByDays(video1,video2):
    comparison=float(video2['dias'])<float(video1['dias'])
    return comparison
    '''
def conteoDays(catalog):
    videos=catalog['videos']['elements']
    lista=lt.newList('ARRAY_LIST')
    for i in videos:   
        if not i['video_id'] in lista:
            listaaa= [i['video_id'] , 1]
            lt.addLast(lista,listaaa)
        elif:
               lt.changeInfo((lista, , [i['video_id'] , 1])
'''
            

def filtrarvideos(catalog,pais,categoria):
    videos=catalog['videos']
    videos2=lt.newList('ARRAY_LIST')
    categorias=catalog['category-id']['elements']
    if categoria=='Film & Animation':
        id1="1"
    else:    
        for t in categorias:
            l=t['id\tname']
            pos=l.find(" ")
            category=l[pos+1:]
            if category==categoria:
                pos2=l.find('\t')
                id1=l[:pos2]
    m=1
    while m<=lt.size(videos):
        i=lt.getElement(videos,m)
        if i["country"]== pais and i["category_id"]==id1:
            lt.addLast(videos2,i)
            
        m+=1
    return videos2


def filtrarvideos_categorias(catalog, categoria):
    videos=catalog['videos']
    videos2=lt.newList('ARRAY_LIST')
    categorias=catalog['category-id']['elements']
    if categoria=='Film & Animation':
        id1="1"
    else:    
        for t in categorias:
            l=t['id\tname']
            pos=l.find(" ")
            category=l[pos+1:]
            if category==categoria:
                pos2=l.find('\t')
                id1=l[:pos2]
    m=1
    while m<=lt.size(videos):
        i=lt.getElement(videos,m)
        if i["category_id"]==id1:
            lt.addLast(videos2,i)
            
        m+=1
    return videos2

def sortVideos(catalog):
           
    sorted_list=merge.sort(catalog,cmpVideosByViews)

    return sorted_list