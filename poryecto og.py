#SECCIÓN DE LABORATORIO
#PROFESOR DE LABORATORIO: FELIPE MORENO
#PROFESOR DE TEORIA: ALFREDO GONZALEZ
#INTEGRANTES
#1.
#NOMBRE: Valentina Ignacia Astudillo Sepulveda
#RUT: 20.670.203-6
#CARRERA: Ingenieria en Biotecnologia
#2.
#NOMBRE: Constanza Anaís Lorca Alarcón
#RUT: 20.712.428-1
#CARRERA: Ingenieria Civil en Quimica

#DESCRIPCION DEL PROGRAMA

#IMPORTACION DE FUNCIONES
#funcion para elegir jugador aleatorio 
from random import randint
aleatorio=(randint(1,3))


Fighter=['Puntos de vida:12','Velocidad:3','Ataque:5','Defensa:14','Umbral de hechizo:20','Prob.de hechizo de ataque:0'
'Prob.de hechizo de defensa:0','Prob. de hechizo decuración:0','Daño mín:2','Daño máx:8','Daño de hechizo mínimo:0','Daño de hechizo máximo:0']

Wizard=['Puntos de vida:6','Velocidad:2','Ataque:2','Defensa:12','Umbral de hechizo:10','Prob.de hechizo de ataque:20'
'Prob.de hechizo de defensa:40','Prob. de hechizo decuración:0','Daño mín:1','Daño máx:4','Daño de hechizo mínimo:4','Daño de hechizo máximo:12']

Cleric=['Puntos de vida:8','Velocidad:2','Ataque:4','Defensa:12','Umbral de hechizo:12','Prob.de hechizo de ataque:0'
'Prob.de hechizo de defensa:20','Prob. de hechizo decuración:40','Daño mín:1','Daño máx:6','Daño de hechizo mínimo:0','Daño de hechizo máximo:0']


caracFighter=[12,3,5,14,20,0,0,0,2,8,0,0]
caracWizard=['6','2','2','12','10','20','40','0','1','4','4','12']
caracCleric=['8','2','4','12','12','0','20','40','1','6','0','0']

Kóbold=['Puntos de vida:4','Velocidad:2','Ataque:2','Defensa:12','Umbral de hechizo:20','Prob.de hechizo de ataque:0'
'Prob.de hechizo de defensa:0','Prob. de hechizo decuración:4','Daño mín:1','Daño máx:6','Daño de hechizo mínimo:0','Daño de hechizo máximo:0']
caracKóbold=['4','2','2','12','20','0','0','4','1','6','0','0']

Goblin=['Puntos de vida:6','Velocidad:4','Ataque:1','Defensa:12','Umbral de hechizo:0','Prob.de hechizo de ataque:0'
'Prob.de hechizo de defensa:0','Prob. de hechizo decuración:0','Daño mín:1','Daño máx:4','Daño de hechizo mínimo:0','Daño de hechizo máximo:0']
caraGoblin=['6','4','1','12','0','0','0','0','1','4','0','0']

GuerreroOrco=['Puntos de vida:12','Velocidad:2','Ataque:5','Defensa:14','Umbral de hechizo:0','Prob.de hechizo de ataque:0'
'Prob.de hechizo de defensa:0','Prob. de hechizo decuración:0','Daño mín:1','Daño máx:8','Daño de hechizo mínimo:0','Daño de hechizo máximo:0']
caracGuerreroOrco=['12','2','5','14','0','0','0','0','1','8','0','0']
           
#DEFINICION DE CONSTANTES

#DEFINICION DE FUNCIONES





#ENTRADA
print('Los nombres de los jugadoren son \na)Fighter \nb)Wizard \nc)Cleric')
Jugador = input('Escoga el personaje que utilizara como jugador indicando a, b o c:')

if aleatorio==1:
           print('su contrincate es kobold')
if aleatorio==2:
           print('su contrincate es goblin')
if aleatorio==3:
           print('su contrincate es guerreroOrco')


caracFighter=['12','3','5','14','20','0','0','0','2','8','0','0']
caracWizard=['6','2','2','12','10','20','40','0','1','4','4','12']
caracCleric=['8','2','4','12','12','0','20','40','1','6','0','0']
