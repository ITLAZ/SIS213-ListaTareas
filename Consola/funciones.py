from tarea import tarea
from datetime import datetime
from tabulate import tabulate
from colorama import *
import time
import os

def valDate(date):
    try:
        datetime.strptime(date, '%d-%m-%y')
        return True
    except ValueError:
        return False
    
def valInt(num):
    try:
        int(num)
        IaN = True
    except ValueError:
        IaN = False
    if IaN == True:
        return num
    else:
        print("Valor no valido, intente de nuevo... \n Valor esperado: Número entero")
        return valInt(int(input()))

taskList = []
estado=""

def detectFile():
    if os.path.isfile("tareas.txt"):
        print("Archivo detectado")
    else:
        print("Archivo no detectado, creando archivo...")
        file = open("tareas.txt", "w")
        file.close()

def writeFile(taskList):
    file = open("tareas.txt", "w", encoding='utf-8')
    for i in taskList:
        file.write(i.nombre + "," + i.detalles + "," + str(i.fechaC) + "," + i.fechaL + "," + i.estado + "\n")
    file.close()

def readFile():
    if os.path.isfile("tareas.txt"):
        with open("tareas.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 5:  # Check if line has enough parts
                    task = tarea(parts[0], parts[1], parts[2], parts[3], parts[4])
                    taskList.append(task)

def add_tarea():
    nombre = input("Nombre de la tarea: ")
    detalles = input("Detalles de la tarea: ")
    fechaC = datetime.now().strftime("%d-%m-%Y")
    fechaL = input("Fecha límite de la tarea (Formato: dd-mm-yyyy) \n Para no ingresar fecha límite presione enter:")
    if fechaL == "":
        fechaL = "Sin fecha límite"
    elif fechaL != valDate(fechaL):
        print("Fecha no válida")
        fechaL = input("Fecha límite de la tarea (dd-mm-yyyy): ")
    estado = "pendiente"
    task = tarea(nombre, detalles, fechaC, fechaL, estado)
    return task

def show_tareas(taskList):
    data = []
    for i in range(len(taskList)):
        data.append([taskList[i].nombre, taskList[i].detalles, taskList[i].fechaC, taskList[i].fechaL, taskList[i].estado])
    print(tabulate(data, headers=["Nombre", "Detalles", "Fecha Creación", "Fecha Límite", "Estado"],showindex="always",
                       tablefmt="fancy_grid", stralign="center", numalign="center"))

def filtrar_por_estado(taskList):
    data = []
    print("1. Pendiente")
    print("2. En proceso")
    print("3. Terminado")
    print("Presione cualquier tecla para cancelar")
    print("Opción:", end=" ")
    opcion = valInt(int(input()))
    if opcion == 1:
        estado = "pendiente"
    elif opcion == 2:
        estado = "en proceso"
    elif opcion == 3:
        estado = "terminado"
    else:
        print("Cancelando...")
        return
    for i in taskList:
        if i.estado.lower() == estado.lower():
            data.append([i.nombre, i.detalles, i.fechaC, i.fechaL, i.estado])
    print(tabulate(data, headers=["Nombre", "Detalles", "Fecha Creación", "Fecha Límite", "Estado"],showindex="always",
                   tablefmt="fancy_grid", stralign="center", numalign="center"))

def changeState(estado):
    if(estado == "pendiente"):
        print("Estado Actual: ", estado)
        print("1. En proceso")
        print("2. Terminado")
        print("Presione cualquier tecla para cancelar")
        print("Opción:", end=" ")
        opcion = valInt(int(input()))
        if(opcion == 1):
            return "en proceso"
        elif(opcion == 2):
            return "terminado"
        else:
            return estado
    elif(estado == "en proceso"):
        print("Estado Actual: ", estado)
        print("1. Pendiente")
        print("2. Terminado")
        print("Presione cualquier tecla para cancelar")
        opcion = int(input("Opción: "))
        if(opcion == 1):
            return "pendiente"
        elif(opcion == 2):
            return "terminado"
        else:
            return estado
    elif(estado == "terminado"):
        print("Las tareas terminadas ya no pueden editarse")
        return estado        

def mod_tarea(taskList):
    nombre = input("Nombre de la tarea a modificar: ")
    for i in taskList:
        if i.nombre == nombre:
            print("1. Nombre")
            print("2. Detalles")
            print("3. Fecha límite")
            print("4. Estado")
            print("5. Cancelar")
            opcion = int(input("Opción a modificar: "))
            if opcion == 1:
                i.nombre = input("Nuevo nombre: ")
            elif opcion == 2:
                i.detalles = input("Nuevos detalles: ")
            elif opcion == 3:
                i.fechaL = input("Nueva fecha límite: ")
            elif opcion == 4:
                i.estado = changeState(i.estado)
            else:
                print("Cancelar modificación")
                break
        else:
            print("Tarea no encontrada")

def del_tarea(taskList):
    nombre = input("Nombre de la tarea a eliminar: ")
    for i in taskList:
        if i.nombre == nombre:
            taskList.remove(i)
            print("Tarea eliminada")
        else:
            print("Tarea no encontrada")

def menu():
    readFile()
    while True:
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Modificar tarea")
        print("4. Eliminar tarea")
        print("5. Filtrado")
        print("6. Salir")
        print("Opción:", end=" ")
        opcion = valInt(int(input()))
        if opcion == 1:
            os.system("cls")
            taskList.append(add_tarea())
            input("Tarea agregada, presione enter para continuar")
            os.system("cls")
        elif opcion == 2:
            os.system("cls")
            show_tareas(taskList)
            input("Presione enter para continuar...")
            os.system("cls")
        elif opcion == 3:
            os.system("cls")
            mod_tarea(taskList)
            input("Presione enter para continuar...")
            os.system("cls")
        elif opcion == 4:
            os.system("cls")
            del_tarea(taskList)
            input("Presione enter para continuar...")
            os.system("cls")
        elif opcion == 5:
            os.system("cls")
            filtrar_por_estado(taskList)
            input("Presione enter para continuar...")
            os.system("cls")
        elif opcion == 6:
            exitApp(taskList)
        else:
            print("Opción no válida, intente de nuevo...")
            input("Presione enter para continuar...")

def exitApp(taskList):
    if(int(input("¿Desea salir de la aplicacion? \n 1. Salir \n 2. Cancelar \n ")) == 1):
        print("Saliendo...")
        writeFile(taskList)
        time.sleep(2)
        print("Archivo guardado, gracias por usar el programa...")
        time.sleep(2)
        os.system("cls")
        quit()
    else:
        print("Cancelando...")
        time.sleep(2)
        os.system("cls")
        input("Presione enter para continuar...")

def pantallaInicio():
    init()
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(124) * 2 + chr(175) * 68 + chr(124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(124) * 2 + " " * 27 + "LISTA DE TAREAS" + " " * 26 + chr(124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(124) * 2 + chr(95) * 68 + chr(124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(124) * 2 + " " * 68 + chr(124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(124) * 2 + " " * 68 + chr(124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(124) * 2 + " " * 28 + "INTEGRANTES:" + " " * 28 + chr(124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(
        124) * 2 + " " * 26 + Back.GREEN + Fore.CYAN + Style.BRIGHT + "ROSARIO CALISAYA" + " " * 26 + Back.GREEN + Fore.RESET + Style.BRIGHT + chr(
        124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(
        124) * 2 + " " * 27 + Back.GREEN + Fore.CYAN + Style.BRIGHT + "IGNACIO TAPIA" + " " * 28 + Back.GREEN + Fore.RESET + Style.BRIGHT + chr(
        124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(
        124) * 2 + " " * 28 + Back.GREEN + Fore.CYAN + Style.BRIGHT + "WILLY VARGAS" + " " * 28 + Back.GREEN + Fore.RESET + Style.BRIGHT + chr(
        124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(124) * 2 + " " * 68 + chr(124) * 2 + Back.RESET)
    print(Back.GREEN + Fore.RESET + Style.BRIGHT + chr(124) * 2 + chr(95) * 68 + chr(124) * 2 + Back.RESET)
    time.sleep(4)
    os.system("cls")


pantallaInicio()
detectFile()
menu()