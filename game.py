from random import choice, randrange
from datetime import datetime

#Inicio del programa.
print('--------------------')
print()
print("Bienvenido/a.")
print()

# Operadores posibles.
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver.
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

#Correctos, incorrectos y sin respuesta.
correctos = 0
incorrectos = 0
sinResp = 0     

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
print()

for i in range(0, times):
    divPorCero = False

    # Se eligen números y operador al azar.
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    
    #Calculo de resultado.
    match operator:
        case "+":
            res = number_1 + number_2     
        case "-":
            res = number_1 - number_2                      
        case "*":
            res = number_1 * number_2                 
        case "/":
            #Se procesa si divisor es distinto de 0.
            if number_2 != 0:
              res = round((number_1 / number_2),2) #Se redondea al 2do decimal.                                                                               
            else:
                print("No se puede dividir por cero.")
                divPorCero =True
      

    print()
    
    if divPorCero == False:
        # Le pedimos al usuario el resultado.
        resUser = input("resultado: ")
        
        #Se procesa si hay respuesta.
        if resUser != "":
            resUser = float(resUser)
            #Informamos en pantalla si fue correcto o no.
            if res == resUser:
                print("Correcto")
                correctos += 1
            else:
                print("Incorrecto")
                incorrectos += 1
        else:
            print("No se ingreso numero.")
            sinResp += 1;                       

    print()

    print()

      
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")

# Informamos cantidad de aciertos y desaciertos.
print(f" Acertaste {correctos} veces. Te equivocaste {incorrectos} veces. Sin responder {sinResp} veces.")


#Fin del programa.
print()
print()
print("Fin del programa.")
print()
print('--------------------')