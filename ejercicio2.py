def check_DDBB(ddbb):
    for x in ddbb:
        (name) = x.get(nombre)
        surname = x.get(apellidos)
        correcion_user = check_username(name, surname)
        x[nombre] = correcion_user[0]
        x[nombre] = correcion_user[1]
    for y in ddbb:
        dni = y.get(nif)
        correccion_nif = check_nif(dni)
    return ddbb

def check_username(name, surname):
    nombre = name.capitalize()
    apellidos = surname.capitalize()
    return nombre, apellidos

def check_nif(dni):

    return

ddbb = []
while True:
    datos = {}
    nombre = input("Introduza el nombre del usuario o escriba TERMINAR para dejar de introducir datos:\n")
    if nombre == "TERMINAR":
        break
    apellidos = input("Introduza los apellidos del usuario:\n")
    nif = input("Introduza el NIF del usuario:\n")
    datos["nombre"] = nombre
    datos["apellidos"] = apellidos
    datos["nif"] = nif
    ddbb.append(datos)
    print(datos)
print(ddbb)
print(check_DDBB(ddbb))