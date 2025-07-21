print("Ejercicio 1")
deptos = ["Alta Verapaz","Baja Verapaz","Chimaltenango","Chiquimula","Guatemala","El Progreso","Escuintla","Huehuetenango","Izabal","Jalapa","Jutiapa","Peten","Quetzaltenango","Quiché","Retalhuleu","Sacatepequez","San Marcos","Santa Rosa","Sololá","Suchitepequez","Totonicapán","Zacapa"]

nombre=input("\nIngrese su nombre: ")
if len(nombre)<5:
    print("El nombre debe ser mayor a 5 caracteres")
    name=False
else:
    name=True

DPI = int(input("\nIngrese su DPI: "))
if len(str(DPI))<13:
    print("DPI inválido")
    dpi=False
else:
    dpi=True

depto = input("\nIngrese su departamento: ").lower()
for depto_ in deptos:
    if depto_.lower() != depto:
        Depto = False
    else:
        Depto = True
        break
if not Depto:
    print("Departamento inválido")

edad = int(input("\nIngrese su edad: "))
if edad>=18:
    voto=True
elif edad>=17 and depto in ["petén", "alta verapaz"]:
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
if ingreso_anual<40000 and dependientes>2:
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
    correcto = False
    for i in usuarios:
        if i["Usuario"] == usuario and i["Contraseña"] == contra:
            correcto = True
            print(f"\nBienvenido, {usuario}")
            print("\n" + "-"*5 + "MENÚ DE OPCIONES" + "-"*5)
            print("1. Ver perfil\n2. Cambiar Contraseña\n3. Cerrar sesión")

        if correcto:
            break
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
            else:
                nota = 100

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
    print(f"{pelicula}. " + pelicula["Nombre"].ljust(25) + str(pelicula["Edad"]).ljust(10))

while True:
    peli_select = int(input("\nIngrese el número de la opción que desea ver: "))
    if peli_select <=0 or peli_select > len(peliculas):
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

if edad_est <= 13:
    if peliculas[peli_select]["edad"] >= 15:
        permiso = False

if permiso:
    if dos_por_uno:
        print(f"Precio final: {precio_base/2} (Oferta 2x1)")
    else:
        print(f"Precio final: {precio_base}")
else:
    print("No tienes permiso para ver esa película.")


import re
print("\n\nEjercicio 10")
meses_2 = [{"mes":1,"dias":30},{"mes":2,"dias":28},{"mes":3,"dias":31},{"mes":4,"dias":30} ,{"mes":5,"dias":31} ,{"mes":6,"dias":30},{"mes":7,"dias":31},{"mes":8,"dias":31},{"mes":9,"dias":30},{"mes":10,"dias":31},{"mes":11,"dias":30},{"mes":12,"dias":31}]

while True:
    fecha_1 = input("\nIngrese la fecha 1 (dd mm aaaa):")
    fecha_2 = input("\nIngrese la fecha 2 (dd mm aaaa):")
    letras_1 = re.search('[A-Za-z]',fecha_1)
    letras_2 = re.search('[A-Za-z]',fecha_2)
    if fecha_1 == fecha_2:
        print("Las fechas deben ser distintas")

    if letras_1 or letras_2:
        print("Escribir las fechas solamente con números separados por espacios.")
    else:
        numeros_1 = fecha_1.split()
        numeros_1 = [int(i) for i in numeros_1]
        numeros_2 = fecha_2.split()
        numeros_2 = [int(i) for i in numeros_2]

        if numeros_1[1]>12 or numeros_1[1]<1 or numeros_2[1]>12 or numeros_2[1]<1:
            print("El mes no puede ser 0 o mayor a 12")
        else:
            mes1_select = numeros_1[1]
            mes2_select = numeros_2[1]
            for i in meses_2:
                if mes1_select == i["mes"]:
                    max_dias1 = i["dias"]
                elif mes2_select == i["mes"]:
                    max_dias2 = i["dias"]

            if numeros_1[0]>max_dias1 or numeros_1[0]<1 or numeros_2[0]>max_dias2 or numeros_2[0]<1:
                print("Cantidad de días incorrecta en alguna de las 2 fechas")
            elif numeros_1[2] > numeros_2[2]:
                print("La fecha 1 es mayor a la fecha 2")
                mismo_ano = False
            elif numeros_2[2] > numeros_1[2]:
                print("La fecha 2 es mayor a la fecha 1")
                mismo_ano = False
            else:
                mismo_ano = True
                if numeros_1[1] > numeros_2[1]:
                    print("La fecha 1 es mayor a la fecha 2")
                    mismo_mes = False
                elif numeros_2[1] > numeros_1[1]:
                    print("La fecha 2 es mayor a la fecha 1")
                    mismo_mes = False
                else:
                    mismo_mes = True
                    if numeros_1[0] > numeros_2[0]:
                        print ("La fecha 1 es mayor a la fecha 2")
                    elif numeros_2[0] > numeros_1[0]:
                        print("La fecha 2 es mayor a la fecha 1")

                if mismo_ano:
                    print("Ambas fechas son del mismo año")
                    break
                if mismo_mes:
                    print("Ambas fechas son del mismo mes")
                    break
                else:
                    break

dias_f1 = 0
for año in range(0,numeros_1[2]):
    dias_f1 += 365
    if año%4==0 and año%100!=0 or año%400==0:
        dias_f1 += 1

for i in range(0, numeros_1[1]-1):
    if i==1 and (numeros_1[2]%4==0 and numeros_1[1]%100!=0 or numeros_1[1]%400==0):
        dias_f1 += 29
    else:
        dias_f1 += meses_2[i]["dias"]

dias_f1 += numeros_1[0]

dias_f2 = 0
for año in range(0, numeros_2[2]):
    dias_f2 += 365
    if año%4==0 and año%100!=0 or año%400==0:
        dias_f2 += 1

for i in range(0, numeros_2[1]-1):
    if i==1 and (numeros_2[2]%4==0 and numeros_2[1]%100!=0 or numeros_2[1]%400==0):
        dias_f2 += 29
    else:
        dias_f2 += meses_2[i]["dias"]

dias_f2 += numeros_2[0]

dif_total = abs(dias_f1-dias_f2)
print(f"La diferencia entre ambas fechas es de {dif_total} días")



