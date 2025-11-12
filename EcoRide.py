#Primer Punto
# Dar la bienvenida al usuario
print ("Bienvenido a Ecoride")

#Variables
tipo_metodo_de_pago = ["efectivo", "tarjeta", "puntos"]
estandar = 2.5
premium = 5.0
costo_total = 0
bicitype = ""
tiempo_de_uso = 0
cargo_extra = 0
descuento = 0
recargo = 0

#Va a iprimir el menu principal y ejecutar las opciones hasta que el usuario decida salir

while True:
    print ("\n---Menu princial---")
    print ("1. Consultar tarifas")
    print ("2. Alquilar bilcicleta")
    print ("3. Pagar")
    print ("4. Salir")

    #punto 2 (validacion de opcion)
    option = input("seleccione una opcion entre el 1 - 4: ")
    if option == "1": #consultar tarifas
            print("Menu EcoRide - Tarifas de Alquiler de bicicletas")
            tabla = f"{'Tipo de bicicleta'}   {'-'}  {'Precio x min'}\n"
            tabla += f"{'1. Estandar'}                 {'$2.5'}\n"
            tabla += f"{'2. Premium'}                  {'$5.0'}\n"
            print(tabla)

    elif option == "2": #alquilar bicicleta
        print("1. Estandar")
        print("2. Premium")
    
        bicitype = input("Que tipo de bicicleta deseas alquilar? (1 - 2): ") #validacion de tipo de bicicleta

        if bicitype == "1":# bicicleta estandar
            tarifa_por_minuto = 2.5
            print("$",tarifa_por_minuto, "Por minuto")

        elif bicitype == "2":# bicicleta premium
            tarifa_por_minuto = 5.0
            print("$",tarifa_por_minuto, "Por minuto")

        else:
            print("Opcion no valida. Intente de nuevo")
            continue

        #validacion de tiempo de uso
        try:# Validar que el usuario ingrese un numero entero
           tiempo_de_uso = int(input("Ingrese la cantidad de minutos de alquiler?: "))

        except ValueError:
           print("Entrada no valida. Por favor ingrese un numero entero.")
           continue
        
        if tiempo_de_uso <= 0:
            print("candidad de minutos no valido, confirma nuevamente.")

        elif bicitype == "1":# bicicleta estandar
            costo_total = tiempo_de_uso * estandar
            print(f"El costo total por alquilar una bicicleta estandar por {tiempo_de_uso} minutos es: ${costo_total}")

        elif bicitype == "2":# bicicleta premium
            costo_total = tiempo_de_uso * premium
            print(f"El costo total por alquilar una bicicleta premium por {tiempo_de_uso} minutos es: ${costo_total}")
            continue
        
    elif option == "3":# pagar

        if costo_total == 0:
            print("No hay ningun alquiler pendiente de pago.")
            continue

        print(f"El total a pagar es: ${round(costo_total, 2)}")

        #validacion de metodo de pago

        metodo_pago = input(f"""
        Que metodo de pago deseas usar?: 
        - {tipo_metodo_de_pago[0]} 
        - {tipo_metodo_de_pago[1]}
        - {tipo_metodo_de_pago[2]}                     
        ingrese metodo de pago: """).lower()
        
        print(f"Has seleccionado pagar con {metodo_pago}")

        #   validacion de descuentos y recargos
                            
        if tiempo_de_uso > 60 and metodo_pago == "tarjeta":# aplicacion de descuento
            descuento = costo_total * 0.10
            costo_total -= descuento
            print(f"Se ha aplicado un descuento del 10%. El nuevo costo total es: ${costo_total}")

        elif tiempo_de_uso < 10 and metodo_pago == "puntos":
            print(f"No aplica para descuentos, el costo total es: ${costo_total}")
            continue
        

        dia = input("Ingrese el día de la semana: ").lower()
        recargo = 0

        if dia == "sabado" or dia == "domingo": #   aplicacion de recargo
            print("Hoy es fin de semana. Se aplicará un recargo del 5%.")
            recargo = costo_total * 0.05
            costo_total += recargo
            print(f"El nuevo costo total con recargo es: ${round(costo_total, 2)}")

        elif dia in ["lunes", "martes", "miercoles", "jueves", "viernes"]: # dia laborable
            print(f"Hoy es día laborable. No se aplicará recargo, el costo total es: ${round(costo_total, 2)}")

        else:
            print("Día no válido. vuelva a intentarlo.")
            continue
     

        #validacion de tiempo extra

        tiempo_final = int(input("Ingrese el tiempo final de uso en minutos: "))
        
        if tiempo_final > tiempo_de_uso: # aplicacion de cargo extra por tiempo adicional
            tiempo_extra = tiempo_final - tiempo_de_uso
            cargo_extra = tiempo_extra * tarifa_por_minuto * 1.20
            costo_total += cargo_extra
            print(f"Se ha aplicado un cargo extra por tiempo adicional de {tiempo_extra} minutos. El nuevo costo total es: ${round(costo_total, 2)}")# Redondea a 2 decimales

        else:
            print("No se ha excedido el tiempo de uso, el costo total se mantiene.")
            

        #resumen del servicio

        resumen = f"""

        ---Resumen del Servicio EcoRide---
        Tipo de bicicleta: {'Estandar' if bicitype == '1' else 'Premium'}
        tiempo de uso: {tiempo_final} minutos
        Metodo de pago: {metodo_pago}
        descuento aplicado: ${round(descuento, 2)}
        recargo aplicado: ${round(recargo, 2)}
        Cargo extra por tiempo adicional: ${round(cargo_extra, 2)}
        ------------------------------------------------------------
        Costo total a pagar: ${round(costo_total, 2)}
        ------------------------------------------------------------
        """
        print(resumen)

        #reiniciar variables para nuevo alquiler
    
        costo_total = 0
        bicitype = ""
        tiempo_de_uso = 0
        cargo_extra = 0
        descuento = 0
        recargo = 0

        #preguntar si desea realizar otro alquiler

        respuesta = input("\n¿Desea realizar otro alquiler? (s/n): ").lower()

        if respuesta != "s":
            print("Gracias por usar EcoRide. ¡Hasta luego!")
            break

# salir del programa
    elif option == "4":
        print("Gracias por usar EcoRide. ¡Hasta luego!")
        break

    else:
        print("Opcion no valida. Intente de nuevo.")
        



    
    
    
    
        
      


            
        
       
        
        

    




  