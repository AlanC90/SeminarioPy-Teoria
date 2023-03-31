#Solución sin lambda. Utilizando Map.

#Inicio.
print("Bienvenido/a.\n")


def encripto(x):
    """
    Funcion encripto(x).
    Recibe caracter en parametro "x" y devuelve su siguiente en la tabla ascii.    
    """
    x = chr(ord(x) + 1)
    return x


cadena = input(" Ingrese una frase a codificar: ")
 
 
print() 
 

#Conversion de caracteres. 
cadena = map(encripto, cadena)         


#Informar resultados.
nuevaCadena = ""
print(" Resultado: ")       
for elem in cadena:						
   nuevaCadena = nuevaCadena + elem
   
print("  " + nuevaCadena)      
  
  

  
#Fin.
print()
print()
print("Fin del programa.\n")

