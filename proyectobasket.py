#Aqui es la introduccion a mi programa

print("Bienvenido a tu programa de basketball favorito")
b = int(input("Esccribe 1 si deseas estadisticas personales   "))
#pongo un condicional para saber si el usuario desea estadisticas personales
if b == 1:
 punto = int(input("Cuántos puntos metiste hoy  "))
 asistencia = int(input("Cuantas asistencias hiciste hoy  "))
 tiros = int(input("cuantos tiros hiciste  "))
 goals = int(input("Cuantos anotaste  "))
 fg = (goals*100)/tiros
 print("tu porcentaje de tiros es de", fg,"%")
 print("Hoy metiste",punto, "pts",asistencia,"ast")

game1 = int(input("Cuántos puntos metiste en el juego 1?  "))
game2 = int(input("Cuántos puntos metiste en el juego 2?  "))
game3 = int(input("Cuántos puntos metiste en el juego 3?  "))
game4 = int(input("Cuántos puntos metiste en el juego 4?  "))
ppg = (game1+game2+game3+game4)/4
print("Tu PPG es de ", ppg)


def field_goals(f,g):
 return g*100/f

print("tu %FG es de",field_goals(40,20))


