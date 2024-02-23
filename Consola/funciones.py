from tarea import tarea
from datetime import datetime
from tabulate import tabulate
from colorama import *
import time
import os

taskList = []
estado=""

def writeFile(taskList):
    file = open("tareas.txt", "w")
    file.close()

def readFile():
    file = open("tareas.txt", "r")
    data = file.readlines()
    for d in data:
        nombre, detalles, fechaC, fechaL, estado = d.rstrip.split(",")
        task = tarea(nombre, detalles, fechaC, fechaL, estado)
        taskList.append(task)
    file.close()

def add_tarea():
    nombre = input("Nombre de la tarea: ")
    detalles = input("Detalles de la tarea: ")
    fechaC = datetime.now()
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

def filtrar_por_estado(taskList, estado):
    for i in taskList:
        if i.estado.lower() == estado.lower():
            print(i.nombre, i.detalles, i.fechaC, i.fechaC, i.fechaL, i.estado, "\n")



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
                i.estado = input("Nuevo estado (En Progreso, Finalizada, Pendiente): ")
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

def main():
    readFile()
    while True:
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Modificar tarea")
        print("4. Eliminar tarea")
        print("5. Filtrado")
        print("6. Salir")
        opcion = int(input("Opción: "))
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
            estado=input("Ingrese el estado que desea ver ")
            filtrar_por_estado(taskList, estado)
            input("Presione enter para continuar...")
            os.system("cls")
        elif opcion == 6:
            
            writeFile(taskList)
            break
        else:
            print("Opción no válida, intente de nuevo...")
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
main()