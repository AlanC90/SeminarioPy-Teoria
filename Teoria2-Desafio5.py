#-----Módulos-----#

#Funcion para primer proceso del desafio.
def ingreso_pelis():
    """ Esta función retorna un diccionario con los nombres y duración de películas."""
    
    peli = input(" Titulo (<FIN> si quiere finalizar): ")
   
    dicci = {}
    
    while peli != "FIN":
        cant_minutos = int(input(" Duración en minutos: "))
        
        dicci[peli] = cant_minutos

        print(' ----------')
        
        peli = input(" Titulo (<FIN> si quiere finalizar): ")
    
    return dicci


#Funcion para segundo proceso del Desafio.
def calcular_promedio(pelis):
    """ Esta función recibe el diccionario "pelis", lo procesa y retorna duracion promedio de peliculas."""
    
    valores = pelis.values()    
    
    suma = 0
    for elem in valores:
      suma = suma + elem

    cantPelis = len(pelis)
          
    return suma/cantPelis


#Funcion para tercer proceso del Desafio.
def informar_pelis_mayores(pelis, promedio):
    """ Esta función recibe el diccionario "pelis" y la duracion promedio, e informa películas que duran más que ese promedio."""        
    
    cantMayores = 0
    
    for elem in pelis:
      if pelis[elem] > promedio:
        print(f'  {elem}')
        cantMayores += 1
    
    if cantMayores == 0:    #Para el caso que se ingrese solo una pelicula.
      print("  Ninguna\n")
    

#-----Programa principal-----#

#Comienzo del programa.
print('--------------------\n')
print('Bienvenido/a.\n')

print('Solucion al Desafio 5 de la "Clase 2 Secuencias-Funciones".\n')

print('Comienza carga de datos de peliculas de Harry Potter.\n')

#Cargar datos.
pelis = ingreso_pelis()

print(' ----------\n')


#Procesar e informar resultados.
print("Resultados: \n")

if len(pelis) != 0:
    print(' Promedio de duracion de peliculas: ')
    promedio = calcular_promedio(pelis)
    print(f'  {promedio}\n')
    
    print(' Peliculas que duran mas que el promedio, en minutos: ')    
    informar_pelis_mayores(pelis, promedio) 
else:
    print(' No se ingresaron datos.\n')


#Fin del programa.
print()
print()
print('Fin del programa.\n')
