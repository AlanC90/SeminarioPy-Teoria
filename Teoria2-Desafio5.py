
#Comienzo del programa.
print('--------------------\n')
print('Bienvenido/a.\n')

print('Solucion al Desafio 5 de la "Clase 2 Secuencias-Funciones".\n')

print('Comienza carga de datos de peliculas de Harry Potter.\n')



#Funcion para primer proceso del desafio.
def ingreso_pelis():
    """ Esta función retorna un diccionario con los nombres y duración de películas """
    
    peli = input(" Titulo (<FIN> si quiere finalizar): ")
   
    dicci = {}
    
    while peli != "FIN":
        cant_minutos = int(input(" Duración en minutos: "))
        
        dicci[peli] = cant_minutos

        print(' ----------')
        
        peli = input(" Titulo (<FIN> si quiere finalizar): ")
    
    return dicci
    
pelis = ingreso_pelis()

print(' ----------\n')



#Funcion para segundo proceso del Desafio.
#Calcular duracion promedio de peliculas.

def calcular_promedio(pelis):
    valores = pelis.values()
    
    suma = 0
    for elem in valores:
      suma = suma + elem

    cantPelis = len(pelis)
          
    return suma/cantPelis


print('Promedio de duracion de peliculas: ')
promedio = calcular_promedio(pelis)
print(f' {promedio}\n')



#Funcion para tercer proceso del Desafio.
#Informar películas que duran más que el promedio, en minutos.    
def informar_pelis_mayores(pelis, promedio):
    for elem in pelis:
      if pelis[elem] > promedio:
        print(f' {elem}')
    
print('Peliculas que duran mas que el promedio, en minutos: ')    
informar_pelis_mayores(pelis, promedio) 



#Fin del programa.
print()
print()
print('Fin del programa.\n')