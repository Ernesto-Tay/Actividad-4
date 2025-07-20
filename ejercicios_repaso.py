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


print("\n\nEjercicio 3")
usuarios=[{"Usuario":"Ignacio", "Contraseña":"wasd"},{"Usuario":"Juanito","Contraseña":"tamalito123"},{"Usuario":"Polonio","Contraseña":"qwerty"}]
intentos = 3
while intentos>0:
    usuario = input("\nIngrese su usuario: ")
    contra = input("\nIngrese su contraseña: ")
    for i in usuarios:
        if i["Usuario"] == usuario and i["Contraseña"] == contra:
            print(f"\nBienvenido, {usuario}")
            print("\n" + "-"*5 + "MENÚ DE OPCIONES" + "-"*5)
            print("1. Ver perfil\n2. Cambiar Contraseña\n3. Cerrar sesión")

        else:
            intentos-=1
            print("Usuario o contraseña inválidos.")

if intentos==0:
    print("\nACCESO BLOQUEADO")


print("\n\nEjercicio 4")
cant = int(input("\n¿Cuántos productos va a ingresar?: "))
subtotal = 0
for i in range(cant):
    precio = int(input("\nIngrese el precio de su producto: "))
    subtotal+=precio

propina_confirm = input("¿Desea dejar propina?: ").lower()
if propina_confirm == "no":
    propina = 0
elif propina_confirm == "si":
    propina_percent = int(input("\nIngrese el porcentaje de su propina: "))
    propina =  subtotal*(propina_percent/100)
    propina = round(propina,2)

tarjeta_confirm = input("\n¿Tiene tarjeta de cliente frecuente?: ").lower()
if tarjeta_confirm == "no":
    tarjeta = 0
elif tarjeta_confirm == "si":
    tarjeta = subtotal/10

IVA = (subtotal/100)*12
IVA = round(IVA,2)
total=subtotal+propina+IVA-tarjeta

print(f"\nDatos de su compra:\nSubtotal: Q{subtotal}\nIVA: Q{IVA}\nPropina: Q{propina}\nDescuento: Q{tarjeta}\nTotal: Q{total}")
