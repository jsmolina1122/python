# ejercicio 1

# A=input("Ingrese El Valor De 'A': \n")

# B=input("Ingrese El Valor De 'B': \n")

# print(f"El Nuevo Valor De 'A' Es:{B}\n")

# print(f"El Nuevo Valor De 'B' Es:{A}")
#-------------------------------------------------------------------------------------------------

#ejercicio 2

# numberOne=int(input("Ingrese El Primer Numero: \n"))

# numberTwo=int(input("Ingrese El Segundo Numero: \n"))

# print(f"La Suma De Los Dos Numeros Es: {(numberOne) + (numberTwo)}\n")

# print(f"La Resta De Los Dos Numeros Es: {numberOne - numberTwo}\n")

# print(f"La Multiplicacion De Los Dos Numeros Es: {numberOne * numberTwo}\n")

# print(f"La Division De Los Dos Numeros Es: {numberOne / numberTwo}\n")

#---------------------------------------------------------------------------------------------------

#ejercicio 3

# numberOne=int(input("Ingrese El Primer Numero: \n"))

# numberTwo=int(input("Ingrese El Segundo Numero: \n"))

# if numberOne == numberTwo:
#     print("Los Numeros Son Iguales: ")
# else:
#     if numberOne > numberTwo:
#         print(f"El Numero {numberOne} Es El Mayor: ")
#     else:
#         print(f"El Numero {numberTwo} Es El Mayor: ")

#-----------------------------------------------------------------------------------------------------

# #ejercicio 4

# numberOne=int(input("Ingrese El Primer Numero: \n"))

# numberTwo=int(input("Ingrese El Segundo Numero: \n"))

# numberThree=int(input("Ingrese El Tercer Numero: \n"))

# if numberOne > numberTwo  and numberOne > numberThree:
#     print(f"El Numero {numberOne} Es El Mayor: ")
# else:
#     if numberTwo > numberOne  and numberTwo > numberThree:
#         print(f"El Numero {numberTwo} Es El Mayor: ")
#     else:
#          print(f"El Numero {numberThree} Es El Mayor: ")

#----------------------------------------------------------------------------------------------------

#ejercicio 5

# numberOne=int(input("Ingrese El Primer Numero: \n"))

# numberTwo=int(input("Ingrese El Segundo Numero: \n"))

# numberThree=int(input("Ingrese El Tercer Numero: \n"))

# if  numberOne < 0 :
    
#     print(f"El Producto De Los Numeros Es: {numberOne*numberTwo*numberThree} ")

# else:
    
#     print(f"la Suma De Los Numeros Es: {numberOne+numberTwo+numberThree} ")

#--------------------------------------------------------------------------------------------

#ejercicio 6

# import math

# number=int(input("Ingrese Un Numero: "))

# if number <= 0 :

#     print(f"Error Verifique El Numero ingresado")
        
#     exit()
# else :
        
#     cuadrado=number*number
#     raiz=math.sqrt(number)
    
#     print(f"El Cuadrado Del Numero {number} Es: {number*number} Y Su Raiz Cuadrada Es: {math.sqrt(number)} ")
    
#-----------------------------------------------------------------------------------------------------------------------------------

#ejercicio 7    

# cantBoy=int(input("Ingrese la Cantidad De Niños Del Curso: \n"))

# cantGirl=int(input("Ingrese La Cantidad De Niñas Del Curso: \n"))

# print(f"El porcentaje De Niños En El Curso Es El: {(cantBoy * 100)/ (cantBoy + cantGirl) } % \n")

# print(f"El porcentaje De Niñas En El Curso Es El: {(cantGirl * 100)/ (cantBoy + cantGirl)} % \n")

#---------------------------------------------------------------------------------------------------------------------

#ejercicio 8

# totalCli=float(input("Ingrese El Total De La Compra: \n"))

# Month=input("Ingrese El Mes De Compra: \n")

# if Month == "octubre" :

#     print(f"El Total A Pagar Es: {totalCli - totalCli * 0.15}\n")
# else :
#      print(f"El Total A Pagar Es: {totalCli}\n")
    
#----------------------------------------------------------------------------------------------------------------------

#ejercicio 9

# namber=int(input("Ingrese Un Numero Entero: \n"))

# if namber == 0 :

#      print(f"El Numero {namber} No Es Ni Par Ni Inpar\n")

# else :

#     if namber % 2 == 0 :

#         print(f"El Numero {namber} Es Par\n")

#     else :

#         print(f"El Numero {namber} Es Impar\n")

#----------------------------------------------------------------------------------------------------------------

#ejercicio 10

# number=int(input("Ingrese Un Numero Entero : \n"))

# while True:
#     if number == 0 :

#         number=int(input("Ingrese Un Numero Entero: \n"))

#     else :
#             if number % 2 == 0 :

#                 print(f"El Numero {number} Es Par\n")
               
#             else :

#                 print(f"El Numero {number} Es Impar\n")
#             break
#-------------------------------------------------------------------------------------------------------

#ejercicio 12

# for i in range(10) :
#     print(f"El Cuadrado De {i} Es: {i * i} \n")

#------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------

#ejercicio 11

print("Ingrese Si/No Segun Sea La Respuesa : \n\n")

Title=input("El Aspirante Posee Titulo Universitario : \n")

if Title == "si" :
    print("El Aspirante Es Apto Para Realizar Un Ciclo Formativo De Educacion Superior \n")

else :

    print("Realise la Siguinete Prueba Para Acceder \n")
    print("cuanto Es 12X2-4/2+12? \n")
    result=int(input("Ingrese El Resultado De La Operacion Anterior : \n"))

    if result == 34 :
       print("El Aspirante Es Apto Para Realizar Un Ciclo Formativo De Educacion Superior \n") 
    else :
        print("El Aspirante No Es Apto Para Realizar Un Ciclo Formativo De Educacion Superior \n") 











 
    




                
                
            
    
        
    

