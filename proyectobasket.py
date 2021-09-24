# FUNCIONES

def field_goals(t, g):
    return (g / t) * 100


def prom_pg(a, b, c, d, e):
    return (a++b+c+d+e)/5


def match_points(pt):
    i = 1
    su = 0
    while i <= pt:
        print("Cuántos puntos metiste en el partido", i, "?")
        acum = int(input())
        su = su + acum
        i = i + 1
    return su/pt


# INTRODUCCION

print("Bienvenido a tu programa de Basketball favorito")
print("PRESIONA 1 - Estadísticas solo un partido\nPRESIONA 2 - Puntos por partido\nPRESIONA 3 - Field Goals  ")
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
