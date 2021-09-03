# FUNCIONES

def field_goals(t, g):
    return (g / t) * 100


def promedio_pg(a, b, c, d, e):
    return (a++b+c+d+e)/5


# INTRODUCCION

print("Bienvenido a tu programa de basketball favorito")
print("PRESIONA 1 Estadisticas solo un partido\nPRESIONA 2 Puntos por partido\nPRESIONA 3 Field Goals  ")
opcion = int(input("Elige la opción  "))

# CONDICIONAL PARA SABER QUE SE  VA A OPERAR

if opcion == 1:
    punto = int(input("Cuántos puntos metiste hoy  "))
    asistencia = int(input("Cuantas asistencias hiciste hoy  "))
    tiros = int(input("cuantos tiros hiciste  "))
    goals = int(input("Cuantos anotaste  "))
    fg = (goals * 100) / tiros
    print("tu porcentaje de tiros es de", fg, "%")
    print("Hoy metiste", punto, "pts", asistencia, "ast")
elif opcion == 2:
    game1 = int(input("Cuántos puntos metiste en el juego 1?  "))
    game2 = int(input("Cuántos puntos metiste en el juego 2?  "))
    game3 = int(input("Cuántos puntos metiste en el juego 3?  "))
    game4 = int(input("Cuántos puntos metiste en el juego 4?  "))
    game5 = int(input("Cuántos puntos metiste en el juego 5?  "))
    print("Tu PPG es de", promedio_pg(game1, game2, game3, game4, game5))
elif opcion == 3:
    num1 = int(input("Cuántos tiros realizaste?  "))
    num2 = int(input("Cuántos tiros metiste?  "))
    print("Tu FG% es de", field_goals(num1, num2), "%")
