#Programa para crear LISTAS DE TAREAS en PYTHON

#Requsitos:
#1. Debo permitir que el usuario interactue con la app
# hasta que no elija SALIR

#2. Debo permitir: 
# crear una tarea
# consultar todas las tareas o pendientes
# modificar una tarea especifica
# eliminar una tarea especifica

#3. Una tarea debe recoger la siguiente información:
#id
#descripcion
#dia de la semana
#hora
#fecha

#4. Modifcar y eliminar se deben hacer por el ID

#5. El proyecto debe estar desplegado en GITHUB


#------------------------------------------------
opcion=None

print("TAREAS APP")
print("1. Crear una tarea")
print("2. Consultar una tarea")
print("3. Modificar una tarea")
print("4. Eliminar una tarea")
print("5. SALIR")

listaTareas=[]
while opcion != 5:
    tarea={}
    opcion=int(input("Digita una opcion por favor: "))
    if opcion == 1:
        print("Creando tarea....")
        tarea['id']=input("Digita el id de la tarea:")
        tarea['descripcion']=input("Digita una descripcion:")
        tarea['diaSemana']=input("¿Que dia es esta tarea?: ")
        tarea['hora']=input("¿A que hora es esta tarea?:")
        tarea['fecha']=input("Digita la fecha del evento (AAA-MM-DD)")
        listaTareas.append(tarea)
    elif opcion == 2:
        print("Consultando las taras....")
        print(listaTareas)
    elif opcion == 3:
        print("Modificando una  taras....")
        pass 
    elif opcion == 4:
        print("Eliminando una  taras....")
        pass
    elif opcion == 5:
        print("saliendo")
        break
    else:
        print("Opcion invalida")