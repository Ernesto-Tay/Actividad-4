print("Ejercicio 1")
deptos = ["Alta Verapaz","Baja Verapaz","Chimaltenango","Chiquimula","Guatemala","El Progreso","Escuintla","Huehuetenango","Izabal","Jalapa","Jutiapa","Peten","Quetzaltenango","Quiché","Retalhuleu","Sacatepequez","San Marcos","Santa Rosa","Sololá","Suchitepequez","Totonicapán","Zacapa"]

nombre=input("\nIngrese su nombre: ")
if nombre.len()<5:
    print("El nombre debe ser mayor a 5 caracteres")
    name=False
else:
    name=True

DPI = int(input("\nIngrese su DPI: "))
if DPI<13:
    print("DPI inválido")
    dpi=False
else:
    dpi=True

depto = input("\nIngrese su departamento: ").lower()
for depto_ in deptos:
    if depto_.lower==depto:
        Depto=True
    else:
        print("El departamento ingresado es inválido")
        Depto=False

edad = input("\nIngrese su año de nacimiento: ")
if edad>=18:
    voto=True
elif edad>=17 and depto == "petén" or edad>=17 and depto == "alta verapaz":
    voto=True
else:
    voto=False

if name==True and dpi==True and Depto==True and voto==True:
    print(f"\nBienvenido {nombre}, su centro de votación está en {depto.capitalize()}")


print("\n\nEjercicio 2")
ingreso_anual=int(input("\nEscriba su ingreso anual (en quetzales): "))
dependientes=int(input("\nEscriba su número de dependientes: "))

if 0<=ingreso_anual<=30000:
    impuesto=(ingreso_anual/100)*5
elif 3000<ingreso_anual<=60000:
    impuesto=(ingreso_anual/100)*10
elif 60000<ingreso_anual<=100000:
    impuesto=(ingreso_anual/100)*15
elif ingreso_anual>100000:
    impuesto=(ingreso_anual/100)*20
elif ingreso_anual<40000 and dependientes>2:
    impuesto=0

if impuesto>0:
    impuesto_total=impuesto-dependientes*1000
else:
    impuesto_total=0

print(f"\nImpuesto total: {impuesto_total}")




