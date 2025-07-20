print("Ejercicio 1")
deptos = ["Alta Verapaz","Baja Verapaz","Chimaltenango","Chiquimula","Guatemala","El Progreso","Escuintla","Huehuetenango","Izabal","Jalapa","Jutiapa","Peten","Quetzaltenango","Quiché","Retalhuleu","Sacatepequez","San Marcos","Santa Rosa","Sololá","Suchitepequez","Totonicapán","Zacapa"]

nombre=input("Ingrese su nombre: ")
if nombre.len()<5:
    print("El nombre debe ser mayor a 5 caracteres")
    name=False
else:
    name=True

DPI = int(input("Ingrese su DPI: "))
if DPI<13:
    print("DPI inválido")
    dpi=False
else:
    dpi=True

depto = input("Ingrese su departamento: ").lower()
for depto_ in deptos:
    if depto_.lower==depto:
        Depto=True
    else:
        print("El departamento ingresado es inválido")
        Depto=False

edad = input("Ingrese su año de nacimiento: ")
if edad>=18:
    voto=True
elif edad>=17 and depto == "petén" or edad>=17 and depto == "alta verapaz":
    voto=True
else:
    voto=False

if name==True and dpi==True and Depto==True and voto==True:
    print(f"Bienvenido {nombre}, su centro de votación está en {depto.capitalize()}")
