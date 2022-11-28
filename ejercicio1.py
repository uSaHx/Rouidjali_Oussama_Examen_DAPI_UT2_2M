def convert_rgb2gray(lista_rgb):
    """""
    Esta funcion usa una lista de tuplas de RGB para darle a la funcion rgb2gray los datos de R, G Y B , luego usa el
    resultado de la otra funcion para crear una lista con los valores de luminancia
    Parametros:
        - lista_rgb = una lista de tuplas donde cada tupla tiene el valor de R, G y B
    Salidas:
        - lista_y = una lista de luminancias que se ha calcualdo con los valores RGB
    """
    lista_y = []
    for x in lista_rgb:
        z = list(x)
        R = z[0]
        G = z[1]
        B = z[2]
        y = rgb2gray(R, G, B)
        lista_y.append(y)
    return lista_y
def rgb2gray(R, G, B):
    """""
    Esta es una funcion que recoge los datos seccionadas de la funcion convert_rgb2gray y los usa para calcular la
    luminancia.
    Parametros:
        - R = es el primer valor de la tupla
        - G = es el segundo valor de la tupla
        - B = es el tercer valor de la tupla
    Salidas:
        - y = es el resultado del calculo y nos aseguramos de que sea un int
    """
    y = (R + G + B) / 3
    return int(y)


lista_rgb = []
while True:
    rgb = []
    r = int(input("Introduzca el valor de R, si quiere dejar de introducir numeros introduzca 00:\n"))
    if r == 00:
        break
    g = int(input("Introduzca el valor de G:\n"))
    b = int(input("Introduzca el valor de B:\n"))

    if r and g and b <= 255:
        rgb.append(r)
        rgb.append(g)
        rgb.append(b)
    else:
        print("Has introducido un numero mayor de 255")
    tupla_rgb = tuple(rgb)
    print(tupla_rgb)
    lista_rgb.append(tupla_rgb)

print(lista_rgb)
print(convert_rgb2gray(lista_rgb))
help(convert_rgb2gray)
help(rgb2gray)