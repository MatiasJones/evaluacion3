import	os
os.system("cls")

menu = """
\n1. REGISTRAR ESPECIE
\n2. INGRESAR NOMBRE DE LA MASCOTA
\n3. IMPRIMIR FICHA
\n4. SALIR
"""
mascota = []
especie = ["perro","gato","ave"]

registro  = """ 
------------------------------------------------------------------------------------
ESPECIE   NOMBRE     PESO   COSTO DE CONSULTA ADICIONAL   IMPU.SALUD  COSTO TOTAL
------------------------------------------------------------------------------------
"""
def registrar ():
    while True:
        try:
            especie = input(f"especie{especie}:").strip ().lower() 
            nombre = input ("NOMBRE:")
            peso = int (input("peso"))
            costo_inicial = int(input ("Costo_inicial"))
            mascota.append([especie,nombre,peso,costo_inicial])
            input("mascota registrada con exito")
            break
        except Exception as e:
            input (f"exepcion al registrar: {str (e)}")

def listadoMascota():
    salida = mascota
    salida += f"{t[0]: }" #  especie
    salida += f"{t[1]: }" #  nombre
    salida += f"{t[2]: }" #  peso
    salida += f"{t[3]: }" #  cpsto de consulta
    salida += f"{t[4]: }" #  impu.salud
    salida += f"{t[5]: }" #  costo total
    salida += "\n"

def imprimir():
    with open ("listado .txt,","w") as archivo:

        archivo.write(listarTodos)
#programa principal 
while  True:
    try:
        opc = input(menu)
        if opc == "4":
            break
        elif opc == "1":
            registrar()
        elif opc =="2":
            print(listadoMascota())
        elif opc == "3":
            imprimir()
        else:
            input("opcion incorrecta, reingrese")
    except Exception as e :
        input (f" Excepcion menu: {str(e)} ")
