"""
Dante David Pérez Pérez
A01709226
Proyecto TC1028
El programa realiza una serie de estadística básica
que es utilizada en partidos de basketball además
muestra los mejores jugadores en la historia
"""
# BILIOTECAS
"""
"Esta librería la saque del siguiente de la 
API https://docs.python.org/3/library/datetime.html
y la utilizo para mostrar al final del programa la fecha 
y hora en la que el usuario ejecutó el programa
"""

from datetime import datetime

now = datetime.now()


# FUNCIONES
def field_goals(t, g):
    """
    Recibe: t valor númerico, g valor númerico.
    Divide g entre t y lo multiplica por 100 para tener un porcentaje.
    Devuelve: Resultado de operación númerico.
    """
    return (g / t) * 100


def match_points(pt):
    """
    La funcion es reutilizada para calcular promedio de puntos y
    promedio de asistencias.
    Recibe: pt como valor númerico.
    Acumula los puntos realizados por el usuario para después dividirlo
    entre los partidos que tuvo.
    Devuelve: Resultado de operación númerico (promedio).
    """
    cont = 1
    su = 0
    while cont <= pt:
        print("Cuántos puntos metiste en el partido", cont, "?")
        acum = int(input())
        su = su + acum
        cont = cont + 1
    return su / pt


def match_assist(pt):
    """
    La funcion es reutilizada para calcular promedio de puntos y
    promedio de asistencias.
    Recibe: pt como valor númerico.
    Acumula los puntos realizados por el usuario para después dividirlo
    entre los partidos que tuvo.
    Devuelve: Resultado de operación númerico (promedio).
    """
    cont = 1
    su = 0
    while cont <= pt:
        print("Cuántas asistencias tuviste en el partido", cont, "?")
        acum = int(input())
        su = su + acum
        cont = cont + 1
    return su / pt


def estatura_pies(length):
    """
    Recibe: lenght como valor númerico.
    Realiza una multiplicación para calcular la estura en pies.
    Devuelve: resultado de operación númerico.
    """
    return length * 3.281


option = 0


def menu():
    """
    Recibe: No recibe nada la función.
    Muestra en el promt el menú y recibe un valor del
    usuario.
    Devuelve: el valor númerico de opc.
    """
    opc = int(input("PRESIONA 1 - Estadísticas solo un partido\nPRESIONA 2 "
                    "- Puntos por partido\nPRESIONA 3 - Asitencias por partido\n"
                    "PRESIONA 4 - Field Goals\nPRESIONA 5 - Top 5 Leader Points\n"
                    "PRESIONA 6 - Termina el Programa "))
    return opc


# SOLITAR DATOS DEL USUARIO
name = str(input('Ingrese su nombre '))
surname = str(input('Ingrese su apellido '))
ege = int(input('Ingrese su edad '))
weight = int(input('Ingrese su peso en Kg '))
lenght = float(input('Ingrese su estatura en m '))
print("Tu estatura en pies es ", estatura_pies(lenght))
datos_persona = [name, surname, ege, weight, lenght]
print(datos_persona)

"""
========  PARTE PRINCIPAL DEL PROGRAMA =======================
"""

print("Bienvenido a tu programa de Basketball favorito")
while option != 6:
    option = menu()
    if option == 1:
        points = int(input("Cuántos puntos metiste hoy?  "))
        assist = int(input("Cuántas asistencias hiciste hoy?  "))
        shots = int(input("Cuántos tiros hiciste?  "))
        goals = int(input("Cuántos anotaste?  "))
        fg = (goals/shots)*100
        match1 = [points, assist, shots, goals, fg]
        print("Tu porcentaje de tiros es de", format(fg, ".2f"), "%")
        print("Hoy metiste", points, "pts", "y", assist, "ast")
    elif option == 2:
        num3 = int(input("Cuántos partidos jugaste?  "))
        print("Tu PPG es de ", match_points(num3))
    elif option == 3:
        num4 = int(input("Cuántos partidos jugaste?  "))
        print("Tu APG es de ", match_assist(num4))
    elif option == 4:
        num1 = int(input("Cuántos tiros realizaste?  "))
        num2 = int(input("Cuántos tiros metiste?  "))
        print("Tu FG% es de", "%.2f" % field_goals(num1, num2), "%")
    elif option == 5:
        best_players = ['Kareem Abdul-Jabbar', 'Karl Malone', 'Lebron James', 'Kobe Bryant', 'Michael Jordan']
        players_points = [38387, 36928, 35367, 33643, 32292]
        stats = [best_players, players_points]
        for i in range(len(best_players)):
            print('Jugador', best_players[i], '-', 'Puntos:', players_points[i])
    elif option == 6:
        print('Programa terminado')
    else:
        print('No tenemos esa opcion')

print('CREADO EL', now)
