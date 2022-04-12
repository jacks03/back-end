#PROGRAMA PARA CONVERTIR MONEDAS
#VERSION 1.0 - CONVERTIR SOLES A DOLARES
#INPUTS - ENTRADAS
montoOrigen = input("ingrese el monto: ")
#proceso
opcion = ""
while(opcion == ""):
    print(" opcion 1 - soles a dolares")
    print(" opcion 2 - dolares a soles")
    print(" opcion 3 - euros a soles")
    print(" opcion 4 - soles a euros")
    print(" opcion 5 - dolares a euros")
    print(" opcion 6 - euros a dolares")
    print(" opcion 7 - soles a soles")
    print(" opcion 8 - dolares a dolares")
    print(" opcion 9 - euros a euros")
    opcion = input("elige una opcion")
    
    #OPCION 1  SOLES A DOLARES
    if(opcion == "1"):
        montoDolares =  float(montoOrigen) / 3.80
        montoDolaresFormato = "${:,.2f}".format(montoDolares)    
#OUTPUTS - SALIDAS
        print ("tu monto en dolares es :" + str(montoDolaresFormato))
        
    #OPCION 2  DOLARES A SOLES
    elif(opcion == "2"):
        montoSoles = float (montoOrigen)* 3.80
        montoSolesFormato = "S/.{:,.2f}".format(montoSoles)
    #output - salida
        print("El monto en soles es : ",montoSolesFormato)
        
    #OPCION 3  SOLES A EUROS   
    if(opcion == "3"):
        montoEuros =  float(montoOrigen) / 4.05
        montoEurosFormato = "€{:,.2f}".format(montoEuros)    
#OUTPUTS - SALIDAS
        print ("tu monto en euros es :" + str(montoEurosFormato))
        
    #OPCION 4  EUROS A SOLES
    elif(opcion == "4"):
        montoSoles = float (montoOrigen)* 4.05
        montoSolesFormato = "S/.{:,.2f}".format(montoSoles)
    #output - salida
        print("El monto en soles es : ",montoSolesFormato)
    
    #OPCION 5  DOLARES A EUROS
    if(opcion == "5"):
        montoDolares1 =  float(montoOrigen) / 0.92
        montoDolaresFormato1 = "${:,.2f}".format(montoDolares1)    
    #OUTPUTS - SALIDAS
        print ("tu monto en dolares es :" + str(montoDolaresFormato1))
        
    #OPCION 6  EUROS A DOLARES
    elif(opcion == "6"):
        montoEuros1 = float (montoOrigen)* 0.92
        montoEurosFormato1 = "€{:,.2f}".format(montoEuros1)
    #output - salida
        print("El monto en euros es : ",montoEurosFormato1)
        
    else:
        print("ALERTA !!! debes seleccionar una opcion ")
        opcion = ""