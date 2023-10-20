class HashTable:

  def __init__(self, size=7):
    self.size = size
    self.table = [[] for _ in range(self.size)]

  def _hash(self, key):
    hash_value = 5381
    for char in key:
      hash_value = (hash_value * 33) ^ ord(char)
    return hash_value

  def set_item(self, key, value):
    index = self._hash(key) % self.size
    bucket = self.table[index]
    for i in bucket:
      if i[0] == key:
        i[1] = value
        return
    bucket.append([key, value])

  def get_item(self, key):
    index = self._hash(key) % self.size
    if self.table[index] != []:
      bucket = self.table[index]
      for i in bucket:
        if i[0] == key:
          return i[1]
    return None

  def remove_item(self, key):
    index = self._hash(key) % self.size
    if self.table[index][0]:
      bucket = self.table[index]
      for i in range(len(bucket)):
        if bucket[i][0] == key:
          return bucket.pop(i)
    return None

  def keys(self):
    all_keys = []
    for i in range(self.size):
      if self.table[i]:
        for j in self.table[i]:
          all_keys.append(j[0])
    return all_keys

  def print_table(self):
    for i, val in enumerate(self.table):
      print(i, ": ", val)


hash_table = HashTable(size=7)

with open('C:\\Users\\Usuario\\Desktop\\TallerEDD\\datos.txt') as file:
  lines = file.readlines()


def agregarEstudiante(id, nombre, materia, notas):
  suma = sum(notas)
  cantidad = len(notas)
  average = suma / cantidad
  student_info = {
    'nombre': nombre,
    'materias': materia,
    'notas': notas,
    'promedio': average,
  }
  hash_table.set_item(id, student_info)


def actualizarPromedio(id):
  estudiante = hash_table.get_item(id)
  nota = estudiante['notas']
  suma = sum(nota)
  cantidad = len(nota)
  if estudiante:
    average = round(suma / cantidad, 2)
    estudiante['promedio'] = average
    hash_table.set_item(id, estudiante)


agregarEstudiante("123", "Laura", ["Estructura", "estadistica"], [5, 2.6])
agregarEstudiante("122", "Santiago", ["Estructura", "estadistica"], [5, 2.6])
agregarEstudiante("125", "Andres", ["Estructura", "estadistica"], [3, 3.5])
agregarEstudiante("128", "Melissa", ["Estructura", "estadistica"], [4, 2.6])


def eliminarEstudiante(id):
  hash_table.remove_item(str(id))
  hash_table.print_table()


def nuevaAsignatura(id, materia, nota):
  estudiante = hash_table.get_item(id)
  materias = estudiante['materias']
  if materia in materias:
    modificarNota(id, materia, nota)
    actualizarPromedio(id, nota)
  else:
    materias.append(materia)
    estudiante['notas'].append(nota)
    actualizarPromedio(id)


def modificarNota(id, materia, nota):
  estudiante = hash_table.get_item(id)

  if materia in estudiante['materias']:
    print(estudiante['materias'])
    index = estudiante['materias'].index(materia)
    estudiante['notas'][index] = float(nota)
    print(estudiante['notas'][index])
    actualizarPromedio(id)

  else:
    print("No existe esa materia en el registro del estudiante.")


for line in lines:
  values = line.strip().split('-')
  student_name = values[0]
  student_id = values[1]
  subjects = values[2::2]
  grades = values[3::2]

  # Calcula el promedio de las notas
  grades_float = [float(grade) for grade in grades]
  average = sum(grades_float) / len(grades_float)

  # Crea un diccionario con la información del estudiante


def alumnoMejorPromedio():
  mejor_promedio = 0
  mejor_estudiante = None
  for student_id in hash_table.keys():
    estudiante = hash_table.get_item(student_id)
    promedio = estudiante['promedio']
    if promedio > mejor_promedio:
      mejor_promedio = promedio
      mejor_estudiante = estudiante

  if mejor_estudiante is not None:
    print("\033[42m\n\n")

    print("ALUMNO CON MEJOR PROMEDIO:", mejor_estudiante['nombre'],
          "CON PROMEDIO DE:", mejor_promedio)
    print("--------------------------------------")
    print("\n\n")
    print("\033[0m")
  else:
    print("\033[41m\n\nERROR!!!!")
    print("NO SE ENCONTRARON ESTUDIANTES EN EL LISTADO")
    print("--------------------------------------")
    print("\n\n")
    print("\033[0m")


def asignaturaMejorPromedio():

  materia = {}
  for student_id in hash_table.keys():
    estudiante = hash_table.get_item(student_id)
    materias = estudiante['materias']
    for k in range(len(materias)):
      if materias[k] in materia:
        materia[materias[k]] = (materia[materias[k]]+estudiante['notas'][k])
        print(estudiante['notas'][k])
    
      else:
        materia[materias[k]] = estudiante['notas'][k]
    
  valores= min(materia,key=materia.get)
  nota=materia[valores]
  print("\033[42m----------------------------------")
  print("ASIGNATURA CON MEJOR PROMEDIO")
  print("MATERIA", valores)
  print("PROMEDIO", nota)


def planMejoramiento(materia):
  estudiantes_plan_mejoramiento = []
  for student_id in hash_table.keys():
    estudiante = hash_table.get_item(student_id)
    materias = estudiante['materias']
    notas = estudiante['notas']
    for i in range(len(materias)):
      if materias[i] == materia and notas[i] < 3.0:
        estudiantes_plan_mejoramiento.append(estudiante)
  if len(estudiantes_plan_mejoramiento) > 0:
    print("Estudiantes que necesitan plan de mejoramiento en la asignatura",
          materia)
    for estudiante in estudiantes_plan_mejoramiento:
      print("Nombre:", estudiante['nombre'])
      print("Promedio:", estudiante['promedio'])
  else:
    print(
      "No se encontraron estudiantes que necesiten plan de mejoramiento en la asignatura",
      materia)


def alumnoMejorAsignatura(id):
  estudiante = hash_table.get_item(id)
  if estudiante is not None:
    mejor_promedio = 0
    mejor_materia = None
    for materia_info in estudiante['materias']:
      promedio = materia_info['nota']
      if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_materia = materia_info['materia']

    if mejor_materia is not None:
      print("Mejor asignatura para el alumno", estudiante['nombre'])
      print("Asignatura:", mejor_materia)
      print("Promedio:", mejor_promedio)
    else:
      print("No se encontraron asignaturas para el alumno",
            estudiante['nombre'])
  else:
    print("No se encontró ningún estudiante con el ID proporcionado.")

def pasandoLaMateria(materia):
  estudiantes_aprobados = []
  for student_id in hash_table.keys():
    estudiante = hash_table.get_item(student_id)
    materias = estudiante['materias']
    for materia_info in materias:
      if materia_info['materia'] == materia and materia_info['nota'] > 3.0:
        estudiantes_aprobados.append(estudiante)

  if len(estudiantes_aprobados) > 0:
    print("Estudiantes que pasaron la materia", materia)
    for estudiante in estudiantes_aprobados:
      print("Nombre:", estudiante['nombre'])
      print("Promedio:", estudiante['promedio'])
  else:
    print("No se encontraron estudiantes que hayan pasado la materia", materia)

def recomendar_mejor_materia():
    materia_promedios = {}

    for student_id in hash_table.keys():
        estudiante = hash_table.get_item(student_id)
        notas = estudiante['notas']
        materias = estudiante['materias']

        for i in range(len(materias)):
            materia = materias[i]
            nota = notas[i]

            if materia in materia_promedios:
                materia_promedios[materia].append(nota)
            else:
                materia_promedios[materia] = [nota]

    mejor_promedio = 0
    mejor_materia = None

    for materia, promedios in materia_promedios.items():
        promedio = sum(promedios) / len(promedios)

        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_materia = materia

    if mejor_materia is not None:
        print("Materia más recomendada:", mejor_materia)
        print("Promedio más alto:", mejor_promedio)
    else:
        print("No se encontraron materias.")


def obtener_materia_menos_recomendada():
    materia_promedios = {}

    for student_id in hash_table.keys():
        estudiante = hash_table.get_item(student_id)
        notas = estudiante['notas']
        materias = estudiante['materias']

        for i in range(len(materias)):
            materia = materias[i]
            nota = notas[i]

            if materia in materia_promedios:
                materia_promedios[materia].append(nota)
            else:
                materia_promedios[materia] = [nota]

    peor_promedio = float('inf')
    peor_materia = None

    for materia, promedios in materia_promedios.items():
        promedio = sum(promedios) / len(promedios)

        if promedio < peor_promedio:
            peor_promedio = promedio
            peor_materia = materia

    if peor_materia is not None:
        print("Materia menos recomendada:", peor_materia)
        print("Promedio más bajo:", peor_promedio)
    else:
        print("No se encontraron materias.")



def resumen_estudiante(id_estudiante):
    
    student = hash_table.get_item(id_estudiante)
    
    if student is None:
        print("ERROR: El estudiante con ID", id_estudiante, "no existe.")
    else:
        
        nombre = student['nombre']
        materias = student['materias']
        notas = student['notas']
        
        
        print("--------------------------------------")
        print("RESUMEN DEL ESTUDIANTE")
        print("Nombre del estudiante:", nombre)
        print("ID del estudiante:", id_estudiante)
        print("Materias matriculadas:")
        for i in range(len(materias)):
          print("  -", materias[i], "- Nota:", "{:.2f}".format(notas[i]))




    
    
    
    
  
hash_table.print_table()
