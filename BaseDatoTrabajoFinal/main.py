import gestorMain as gm


while True:
    opcion = input ("""
    --- MENU PRINCIPAL ---
    1. Crear usuario
    2. Mostrar datos del usuario
    3. Actualizar datos del usuario
    4. Borrar usuario
    5. Borrar mascota
    6. Salir
    Opcion: """)
    if opcion == "1":
        gm.crear_usuario()
    elif opcion == "2":
        gm.mostrar_informacion_de_usuario()
    elif opcion == "3":
        gm.actualizar_datos()
    elif opcion == "4":
        gm.eliminar_usuario()
    elif opcion == "5":
        gm.eliminar_mascota()
    elif opcion == "6":
        break
    else:
        print("Error, valor no valido.")

