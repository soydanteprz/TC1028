"""
Sub-Competencia:
componente: usa la forma más a apropiada al problema para guardar los datos (listas, variable, tipo de dato, etc...)
(avance 5)
Error original: Uso mal de listas
Cambio realizado: creé un conjuntos de dos lista denominada stats y
le muestro al usuario los jugadores con sus respectivos puntos
Líneas de código donde se ve la corrección: 90 a 94


Proyecto TC1028
El programa realiza una seria de estadistica basica
que es utilizada en partidos de basketball
además muestra los mejores jugadores en la historia
"""
# BILIOTECAS
"Esta librería la saque del siguiente API https://docs.python.org/3/library/datetime.html"
from datetime import datetime

now = datetime.now()


# FUNCIONES
def field_goals(t, g):
    return (g / t) * 100


def match_points(pt):
    cont = 1
    su = 0
    while i <= pt:
        print("Cuántos puntos metiste en el partido", i, "?")
        acum = int(input())
        su = su + acum
        cont = cont + 1
    return su / pt


def estatura_pies(length):
    return length * 3.281


option = 0


def menu():
    opc = int(input("PRESIONA 1 - Estadísticas solo un partido\nPRESIONA 2 "
                    "- Puntos por partido\nPRESIONA 3 - Asitencias por partido\nPRESIONA 4 "
                    "- Field Goals\nPRESIONA 5 - Top 5 Leader Points\nPRESIONA 6 - Termina el Programa "))

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

# INTRODUCCION
print("Bienvenido a tu programa de Basketball favorito")
while option != 6:
    option = menu()
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
        num4 = int(input("Cuántos partidos jugaste?  "))
        print("Tu APG es de ", match_points(num4))
    elif option == 4:
        num1 = int(input("Cuántos tiros realizaste?  "))
        num2 = int(input("Cuántos tiros metiste?  "))
        print("Tu FG% es de", "%.2f" % field_goals(num1, num2), "%")
    elif option == 5:
        # USO DE FOR PARA RECORRER LA LISTA
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
