'''
Este programa manipula los ingresos de los vehiculos
'''
import os
ingresos={'1': ['Marcos', 'Kia - Rio 4'],
            '2': ['Maria', 'Mercedez - Mercedito'],
            '3': ['Juanin', 'Susuki - Spresso']}
menup=['Ver Ingreso',"Añadir Ingreso","Eliminar Ingreso","Salir"]
#Menu Principal
while True:
    for ind, opt in enumerate(menup):
        print(f"{ind+1}. {opt}")
    ans=input("Que desea hacer?\n")
    if ans=="1":
        os.system("cls")
        for llave,valor in ingresos.items():
            print(f"Dueño: {llave}  \n Vehiculo: {valor[0]}  \n {valor[1]}")
    elif ans=="2":
        os.system("cls")
        temp=[int(llave) for llave in ingresos]
        newind=max(temp) + 1
        while True:
            nombre=input("Ingrese el nombre del usuario\n")
            if not nombre.replace(" "," ").isalpha():
                print("Error: solo se pueden usar caracteres alfabeticos")
                continue
            marca=input("Ingerese la marca del vehiculo\n")
            if not marca.replace(" "," ").isalpha():
                os.system("cls")
                print("Error: solo se pueden usar caracteres alfabeticos")
                continue
            modelo=input("Ingrese el modelo\n")
            temp=["s","si","n","no"]
            while True:
                os.system("cls")
                print(f"Dueño: {nombre}\n Marca: {marca}\n Modelo: {modelo}\n")
                ans=input("Son correctos los datos? (s/n)")
                if ans.lower()in temp:
                    break
            if ans.lower() in ["s","si"]:
                    break
            print("Agregado exitosamente")
        ingresos[str(ans)]= [nombre.capitalize(),
                             (f"{marca.capitalize}() - {modelo.capitalize()}")]
        os.system("cls")
        print("Datos ingresado correctamente")
    elif ans=="3":
        os.system("cls")
        while True:
            try:
                ans=int(input("Ingrese el registro a eliminar\n"))
                break
            except:
                os.system("cls")
                print("Error el ingreso es invalido")
                if str(ans) in ingresos:
                    del ingresos[str(ans)]
                    os.system("cls")
                    print("Registro borrado exitosamente")
                else:
                    os.system("cls")
                    print("Ingreso no valido, favor selecione in ingresado valido")
    elif ans=="4":
        os.system("cls")
        exit("Gracias por usar nuestro programa, Hasta Pronto")
    else:
        os.system("cls")
        print("Error: Eliga una opcion valida")
