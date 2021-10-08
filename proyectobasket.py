# FUNCIONES
def field_goals(t, g):
    return (g / t) * 100


def match_points(pt,):
    i = 1
    su = 0
    while i <= pt:
        print("Cuántos puntos metiste en el partido", i, "?")
        acum = int(input())
        su = su + acum
        i = i + 1
    return su/pt


def estatura_pies(length):
    return length*3.281


def puntos2(i):
    total = 0
    for i in range(101):
        total = total + i
    return 'sumatoria ', total


#SOLITAR DATOS DEL USUARIO
name = str(input('Ingrese su nombre '))
surname = str(input('Ingrese su apellido '))
ege = int(input('Ingrese su edad '))
weight = int(input('Ingrese su peso en Kg '))
lenght = float(input('Ingrese su estatura en m '))
print("Tu estatura en pies es ", estatura_pies(lenght))
datos_persona = [name, surname, ege, weight, lenght]
print(datos_persona)

#INTRODUCCION
print("Bienvenido a tu programa de Basketball favorito")
print("PRESIONA 1 - Estadísticas solo un partido\nPRESIONA 2 - Puntos por partido\nPRESIONA 3 - Field Goals\nPRESIONA 4 - Top 5 Leader Points")
option = int(input("Elige la opción  "))

# CONDICIONAL PARA SABER QUE SE  VA A OPERAR ES INDISPENSABLE
if option == 1:
    points = int(input("Cuántos puntos metiste hoy?  "))
    assist = int(input("Cuántas asistencias hiciste hoy?  "))
    shots = int(input("Cuántos tiros hiciste?  "))
    goals = int(input("Cuántos anotaste?  "))
    fg = (goals * 100) / shots
    match1 = [points, assist, shots, goals, fg]
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
    best_players = ['Kareem Abdul-Jabbar', 'Karl Malone', 'Lebron James', 'Kobe Bryant', 'Michael Jordan']
    players_points = [38387,36928,35367,33643,32292]
    stats = [best_players, players_points]
    print(stats)
    for i in range(len(best_players)):
        print('Jugador', best_players[i], '-', 'Puntos:', players_points[i])
else:
    print('No tenemos esa opcion')