from tarea import tarea
from datetime import datetime

taskList = []

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
    for i in taskList:
        print(i.nombre, i.detalles, i.fechaC, i.fechaL, i.estado, "\n")

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
    writeFile(taskList)
    readFile()
    while True:
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Modificar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = int(input("Opción: "))
        if opcion == 1:
            taskList.append(add_tarea())
        elif opcion == 2:
            show_tareas(taskList)
        elif opcion == 3:
            mod_tarea(taskList)
        elif opcion == 4:
            del_tarea(taskList)
        else:
            writeFile(taskList)
            break

main()