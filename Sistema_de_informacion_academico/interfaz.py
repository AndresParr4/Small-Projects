import datos as abc


def mostrarInicio():
  print("------------------------------------------------------")
  print("\033[94m\033[1m\033[1mBIENVENIDO AL MENÚ PRINCIPAL\033[0m")
  print(
    "\033[1m\n1)Matricular Alumno\n2)Eliminar estudiante\n3)Editar o agregar información\n4)Resumenes\n5)Funciones adicionales\n6)Salir."
  )
  print("\033[0m")


while True:
  mostrarInicio()
  opcion = input("Selecciona una opción: ")
  if opcion == "1":
    print("--------------------------------------")
    print("\033[1m\033[44mMATRICULAR ALUMNO")
    print("\033[0m")
    nombre = input("ingrese el nombre:")
    id = input("ingrese el id:")
    materias = []
    notas = []
    n = int(input("Ingrese el numero de materias:"))
    for i in range(n):
      print("\n\n")
      m = input("Ingrese la materia {}: ".format(i + 1))
      n = float(input("Ingrese nota de la materia {}: ".format(m)))
      while n > 5:
        print("\n")
        print("ERROR!!!!!!!!!!!")
        print("\n")
        print("La nota debe ser un valor entre 0 y 5")

        n = float(
          input("Escriba nuevamente la nota de la materia {}: ".format(m)))
        print("\033[0m")
      materias.append(m)
      notas.append(int(n))
    abc.agregarEstudiante(id, nombre, materias, notas)
    print("\033[42m\n\n")
    print("--------------------------------------")
    print("LA NUEVA ALUMNA", nombre, "HA SIDO AGREGADA")
    print("--------------------------------------")
    print("\n\n")
    print("\033[0m")
    abc.hash_table.print_table()

  elif opcion == "2":
    print("--------------------------------------")
    print("\033[94m\033[1m\033[1ELIMINAR ESTUDIANTE\033[0m")
    estudiante = input("Ingrese ID del estudiante:")
    if abc.hash_table.get_item(estudiante) == None:
      print("\033[41m\n")
      print("ERROR!!!!!!!!!!!")
      print("El alumno con ID", estudiante, "no existe\n")
      print("\033[0m")

    else:
      e = abc.hash_table.get_item(estudiante)
      e = e['nombre']
      abc.eliminarEstudiante(estudiante)
      print("\033[42m\n\n")
      print("--------------------------------------")
      print("EL ALUMNO", e, "HA SIDO ELIMINADO")
      print("--------------------------------------")
      print("\n\n")
      print("\033[0m")

  elif opcion == "3":
    print("--------------------------------------")
    print("\033[94m\033[1m\033[1AAGREGAR ASIGNATURA Y NOTA\033[0m")
    print("\n1)Agregar nueva nota y asignatura\n2)Actualizar nota\n3)Salir.")
    opcion = input()

    if opcion == "1":
      print("--------------------------------------")
      id = input("Ingrese ID del estudiante:")
      if abc.hash_table.get_item(id) == None:
        print("\033[41m\n")
        print("ERROR!!!!!!!!!!!")
        print("El alumno con ID", id, "no existe\n")
        print("\033[0m")
        mostrarInicio()
      else:
        materia = input("Ingrese la nueva materia:")
        nota = float(input("Ingrese la nota:"))
        while nota > 5:
          print("\033[41m\nERROR!!!!!!!!!!!\n")
          print("La nota debe ser un valor entre 0 y 5")
          nota = float(input("Escriba nuevamente la nota de la materia"))
          print("\033[0m")
        abc.nuevaAsignatura(id, materia, nota)
        print("\033[42m\n\n")
        print("--------------------------------------")
        print("LA MATERIA", materia, "CON NOTA", nota, "HA SIDO AGREGADA")
        print("--------------------------------------")
        print("\n\n")
        print("\033[0m")

    elif opcion == "2":
      print("--------------------------------------")
      id = input("Ingrese el ID del estudiante:")
      if abc.hash_table.get_item(id) == None:
        print("\033[41m\n")
        print("ERROR!!!!!!!!!!!")
        print("El alumno con ID", id, "no existe\n")
        print("\033[0m")

      else:
        print("--------------------------------------")
        materias = input("Ingrese la materia:")
        notas = float(input("Ingrese la nota:"))

        abc.modificarNota(id, materias, notas)
        abc.hash_table.print_table()
        print("\033[42m\n\n")
        print("--------------------------------------")
        print("LA NOTA HA SIDO MODIFICADA CON EXITO")
        print("--------------------------------------")
        print("\n\n")
        print("\033[0m")

    elif opcion == "3":
      print("--------------------------------------")
      mostrarInicio()

  elif opcion == "4":
    print("--------------------------------------")
    print("\033[1m\033[44mRESUMEN DE ESTUDIANTES DE UNA ASIGNATURA")
    print("\033[0m")
    print(
      "\n1)Estudiante con mejor promedio\n2)Asignatura con mejor promedio\n3)Estudiantes que necesitan plan de mejoramiento\n4)Mejor asignatura por estudiante\n5)Asignatura y estudiantes que van aprobando\n6)salir"
    )
    opcion = input()
    if opcion == "1":
      print("--------------------------------------")

      abc.alumnoMejorPromedio()

    elif opcion == "2":
      print("--------------------------------------")
      print("ASIGNATURA CON MEJOR DESEMPEÑO")
      abc.asignaturaMejorPromedio()

    elif opcion == "3":
      print("--------------------------------------")
      print("ESTUDIANTES QUE NECESITAN PLAN DE MEJORAMIENTO")
      materia = input("Ingrese la materia:")
      abc.planMejoramiento(materia)

    elif opcion == "4":
      print("--------------------------------------")
      "MATERIA CON MEJOR NOTA"
      estudiante = input("Ingrese la cédula:")
      abc.alumnoMejorAsignatura(estudiante)

    elif opcion == "5":
      print("--------------------------------------")
      "LISTADO DE ESTUDIANTES QUE VAN PASANDO LA MATERIA"
      materia = input("Ingrese la materia de su interés:")
      abc.pasandoLaMateria(materia)
    else:
      break

  elif opcion == "5":
    print("--------------------------------------")
    print("\033[1m\033[44mFUNCIONES ADICIONALES")
    print("\033[0m")
    print(
      "\n1) Recomendacion de materias\n2) Asignatura con mejor promedio\n3) Resumen del estudiante\n4) Salir"
    )
    opcion = input()
    if opcion == "1":
      print("--------------------------------------")
      abc.obtener_materia_menos_recomendada()
    elif opcion == "2":
      print("--------------------------------------")
      abc.recomendar_mejor_materia()
    elif opcion == "3":
      print("--------------------------------------")
      print("\033[94m\033[1m\033[1RESUMEN DEL ESTUDIANTE\033[0m")
      id_estudiante = input("Ingrese el ID del estudiante: ")
      abc.resumen_estudiante(id_estudiante)


    else:
      break
  
  else:
    break

#python Taller_ED/interfaz.py
