sesccion_valida = "DRY7122-003V"
seccion_alumno = input("Ingrese el código de su sección: ")
if seccion_alumno == sesccion_valida:
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    sede = input("Ingrese su sede: ")
    print(f"Nombre: {nombre}\nApellido: {apellido}\nCódigo-sección: {seccion_alumno}\nSede: {sede}")
else:
    print("El código de sección ingresado no es válido")