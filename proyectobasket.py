# FUNCIONES

def field_goals(t, g):
    return (g / t) * 100


def prom_pg(a, b, c, d, e):
    return (a++b+c+d+e)/5


def match_points(pt,):
    i = 1
    su = 0
    while i <= pt:
        print("Cuántos puntos metiste en el partido", i, "?")
        acum = int(input())
        su = su + acum
        i = i + 1
    return su/pt,

def estatura_pies(length):
    length*3.281
    return length

def puntos2(i):
    total = 0
    for i in range (101):
        total = total + i
    return 'sumatoria ', total



# INTRODUCCION
nombre = str(input('Ingrese su nombre '))
apellido = str(input('Ingrese su apellido '))
edad = int(input('Ingrese su edad '))
peso = int(input('Ingrese su peso en Kg '))
estatura = float(input('Ingrese su estatura en m '))

estatura_pies(estatura)
datos_persona = [nombre, apellido, edad, peso, estatura]
print(datos_persona)
print("Bienvenido a tu programa de Basketball favorito")
print("PRESIONA 1 - Estadísticas solo un partido\nPRESIONA 2 - Puntos por partido\nPRESIONA 3 - Field Goals\nPRESIONA 4 - Top 5 Mejores jugadores ")
option = int(input("Elige la opción  "))

# CONDICIONAL PARA SABER QUE SE  VA A OPERAR ES INDISPENSABLE
if option == 1:
    points = int(input("Cuántos puntos metiste hoy?  "))
    assist = int(input("Cuántas asistencias hiciste hoy?  "))
    shots = int(input("Cuántos tiros hiciste?  "))
    goals = int(input("Cuántos anotaste?  "))
    fg = (goals * 100) / shots
    print("Tu porcentaje de tiros es de", fg, "%")
    print("Hoy metiste", points, "pts", assist, "ast")
elif option == 2:
    num3 = int(input("Cuántos partidos jugaste?  "))
    print("Tu PPG es de ", match_points(num3))
elif option == 3:
    num1 = int(input("Cuántos tiros realizaste?  "))
    num2 = int(input("Cuántos tiros metiste?  "))
    print("Tu FG% es de", "%.2f" % field_goals(num1, num2), "%")
elif option == 4:
#USO DE FOR PARA RECORRER LA LISTA
    best_players = ['Michael Jordan', 'Lebron James', 'Stephen Curry', 'James Harden', 'Giannis Antetokounmpo']
    top=int(input('del 1 al 5 que jugador deseas ver'))
    for top in best_players:
        print(top)
else:
    print('No tenemos esa opcion')


