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

edad = int(input("\nIngrese su edad: "))
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


print("\n\nEjercicio 5")
meses = [{"mes":"marzo","dias":31},{"mes":"abril","dias":30} ,{"mes":"mayo","dias":31} ,{"mes":"junio","dias":30},{"mes":"julio","dias":31},{"mes":"agosto","dias":31},{"mes":"septiembre","dias":30},{"mes":"octubre","dias":31},{"mes":"noviembre","dias":30},{"mes":"diciembre","dias":31},{"mes":"enero","dias":30},{"mes":"febrero","dias":28}]
dias = ["Sábado","Domingo","Lunes","Martes","Miércoles","Jueves","Viernes"]
while True:
    ano = int(input("\nIngrese el año: "))
    if ano<1:
        print("Año inválido, intente nuevamente")
    else:
        break

while True:
    mes = input("\nIngrese el nombre del mes: ").lower()
    meses_name = [m["mes"] for m in meses]
    if mes not in meses_name:
        print("Mes inválido, intente nuevamente")
    else:
        break

for mess in meses:
    if mess["mes"]==mes:
        max_dias = mess["dias"]
        mes_num=meses.index(mess)+3
        if mes_num==13 or mes_num==14:
            ano-=1

while True:
    dia = int(input("\nIngrese el dia: "))
    if dia<=0 or dia >max_dias:
        print("Ingrese un número de día válido")
    else:
        break

siglo = ano//100
decada = ano%100

formula = (dia + (13*(mes_num+1))//5 + decada + (decada//4) + (siglo//4) + siglo*5)%7
diasem = dias[formula]

print(f"\nEl {dia} de {mes} del {ano} fue un: {diasem}")


print("\n\nEjercicio 6")
peso = float(input("\nIngrese el peso del paquete: "))
distancia = int(input("\nIngrese la distancia del viaje (en km): "))
urgencia = input("\n¿Es urgente el envío?: ").lower()
tamano = input("\n ¿su paquete es pequeño, mediano o grande?: ").lower()

costo_peso = peso*1.5
costo_distancia = distancia/2
if urgencia == "si":
    costo_urgencia = 50
else:
    costo_urgencia = 0

if tamano == "grande":
    costo_tamano = 30
else:
    costo_tamano = 0

total = costo_peso+costo_distancia+costo_urgencia+costo_tamano

print(f"\nDesglose de costo: \nPeso: +Q{costo_peso}\nDistancia: +Q{costo_distancia}\nUrgencia: +Q{costo_urgencia}\nTamaño: +Q{costo_tamano}\nTOTAL: Q{total}")


print("\n\nEjercicio 7")
estudiantes = []
promedios = []
for i in range(5):
    nombre = input(f"\nIngrese el nombre del estudiante {i}: ")
    while True:
        nota1 = int(input("\nIngrese su primer nota: "))
        if nota1<0 or nota1>100:
            print("Ingrese una nota válida (del 0 al 100")
        else:
            break
    while True:
        nota2 = int(input("\nIngrese su segunda nota: "))
        if nota2<0 or nota2>100:
            print("Ingrese una nota válida (del 0 al 100")
        else:
            break
    while True:
        nota3 = int(input("\nIngrese su tercera nota: "))
        if nota3<0 or nota3>100:
            print("Ingrese una nota válida (del 0 al 100")
        else:
            break
    promedio = (nota1+nota2+nota3)/3
    promedios.append(promedio)

    notas = {"nota 1": nota1, "nota 2": nota2, "nota 3": nota3,}
    estudiante = {"nombre": nombre,"notas": notas}
    estudiantes.append(estudiante)

curva = True
for i in promedios:
    if i > 70:
        curva = False

if curva:
    for i in estudiantes:
        for nota in i["notas"]:
            if nota<=95:
                nota += 5

print("--"*5 + "LISTA DE ESTUDIANTES" + "--"*5)
for i in estudiantes:
    print(".."*5 + f"ESTUDIANTE {i}" + ".."*5)
    print(f"Nombre: {i['nombre']}")
    print(f"Nota 1: {i['notas']['nota 1']}")
    print(f"Nota 2: {i['notas']['nota 2']}")
    print(f"Nota 3: {i['notas']['nota 3']}")
    print("..."*10 + "\n")


print("\n\nEjercicio 8")
coordenadas = [{"Coordenada":"norte", "Eje":1, "Signo":"+"}, {"Coordenada":"sur", "Eje":1, "Signo":"-"}, {"Coordenada":"este", "Eje":2, "Signo":"+"}, {"Coordenada":"oeste", "Eje":2,"Signo":"-"}]
while True:
    coord_1 = input("\nIngrese la coordenada inicial: ").lower()
    coord_2 = input("\nIngrese la coordenada final: ").lower()
    coord_names = [i["Coordenada"] for i in coordenadas]

    if coord_1 == coord_2:
        print("Las coordenadas deben ser distintas")
    elif coord_1 not in coord_names:
        print("Coordenada inicial inválida")
    elif coord_2 not in coord_names:
        print("Coordenada final inválida")
    else:
        break

for i in coordenadas:
    if i["Coordenada"] == coord_1:
        eje_1 = i["Eje"]
        signo_1 = i["Signo"]

    if i["Coordenada"] == coord_2:
        eje_2 = i["Eje"]
        signo_2 = i["Signo"]

if eje_1 == eje_2:
    print(f"Debe ir recto hacia el {coord_2}")
if signo_1 == signo_2:
    if signo_1 == "+":
        if eje_1 == 1:
            print("Debe ir hacia el sureste")
        elif eje_1 == 2:
            print("Debe ir hacia el noroeste")

    if signo_1 == "-":
        if eje_1 == 1:
            print("Debe ir hacia el noroeste")
        elif eje_1 == 2:
            print("Debe ir hacia el sureste")

if signo_1 != signo_2:
    if signo_1 == "+":
        if eje_1 == 1:
            print("Debe ir hacia el suroeste")
        elif eje_1 == 2:
            print("Debe ir hacia el noreste")

    if signo_1 == "-":
        if eje_1 == 1:
            print("Debe ir hacia el noreste")
        elif eje_1 == 2:
            print("Debe ir hacia el suroeste")


print("\n\nEjercicio 9")
peliculas = [{"Nombre":"el deslenguado", "Edad":17},{"Nombre": "Tras la muerte", "Edad": 14},{"Nombre": "David de la granja", "Edad":9},{"Nombre":"El rey carmesí", "Edad":16},{"Nombre":"Alba futura", "Edad":12}]
edad_est = int(input("\nIngrese su edad: "))
dia_sem = input("\nIngrese el día de la semana actual: ").lower()
est = input("\n¿Es estudiante? (si/no): ").lower()

print("\n"+"--"*5 + "CARTELERA" + "--"*5)
print("Nombre".ljust(25) + "Edad".ljust(10))
for pelicula in peliculas:
    print(f"{pelicula}. " + pelicula["Nombre"].ljust(25) + pelicula["Edad"].ljust(10))

while True:
    peli_select = input("\nIngrese la opción que desea ver: ")
    if peli_select <=0 or peli_select > peliculas.len():
        print("Opción inexistente")
    else:
        selected_peli = peliculas[peli_select]["Nombre"]
        break

permiso = True
dos_por_uno = False
precio_base = 50
if est == "si":
    precio_base=35

if dia_sem == "miercoles" or dia_sem == "miércoles":
     dos_por_uno = True

if edad <= 13:
    if peliculas[peli_select]["edad"] >= 15:
        permiso = False

if permiso:
    if dos_por_uno:
        print(f"Precio final: {precio_base/2} (Oferta 2x1)")
    else:
        print(f"Precio final: {precio_base}")
else:
    print("No tienes permiso para ver esa película.")




