#Solución con lambda. Utilizando Map.

#Inicio.
print("Bienvenido/a.\n")


cadena = input(" Ingrese una frase a codificar: ")
 
 
print() 
 

#Conversion de caracteres. 
cadena = map(lambda x: chr(ord(x) +1), cadena)         


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

