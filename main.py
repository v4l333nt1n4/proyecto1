# import
from time import sleep
from random import randint

# constant
TICK_RATE = 0.4

FIGHTER = [12,3,5,14,20,0,0,0,2,8,0,0]
WIZARD  = [6,2,2,12,10,20,40,0,1,4,4,12]
CLERIC  = [8,2,4,12,12,0,20,40,1,6,0,0]

SELECTED_PLAYER = 0
EXIT_FLAG = False

# functions


# user input
print('Los nombres de los jugadoren son \na)Fighter \nb)Wizard \nc)Cleric')
selectedPlayer = input('Escoga el personaje que utilizara como jugador indicando a, b o c:')

if selectedPlayer == 'a' or selectedPlayer == 'A':
    SELECTED_PLAYER = FIGHTER
elif selectedPlayer == 'b' or selectedPlayer == 'B':
    SELECTED_PLAYER = WIZARD
elif selectedPlayer == 'c' or selectedPlayer == 'C':
    SELECTED_PLAYER = CLERIC
else:
    print("oe culiao selecciona una wea bien")
    SELECTED_PLAYER = None


if SELECTED_PLAYER is not None:
    print(SELECTED_PLAYER)
    # inicio del juego y wea
    ## logica para seleccionar el oponente random 
    PLAYER_HEALTH = SELECTED_PLAYER[0]
    PLAYER_GAUGE = 0
    PLAYER_ATTACK_VALUE = SELECTED_PLAYER[2]
    while not EXIT_FLAG:
    
        print("SELECTED PLAYER HEALTH: " + str(PLAYER_HEALTH))
        print("SELECTED PLAYER GAUGE: " + str(PLAYER_GAUGE))

        
        if(PLAYER_GAUGE >= 10):
            # utilizar randint para determinar el valor aleatorio del ataque
            # y según esto saber si es ataque o hechizo y si este logrará pegarle al 
            # oponente, fallar o hacer un golpe critico
            random = randint(1, 20)
            ataque = PLAYER_ATTACK_VALUE + random
            print ("random value obtained: " + str(random))
            attackModifier = 1;
        
            if random == 1:
                # fallo de ataque
                print ("random es: " + str(random) + "- ataque falla")
                attackModifier = 0;
            elif random == 20:
                # critico
                print ("random es: " + str(random) + "- ataque critico")
                attackModifier = 2;

            print ("ataque considerando critico/fallo: " + str(ataque * attackModifier))
                

            ## PLAYER_GAUGE = PLAYER_GAUGE - 10

        PLAYER_GAUGE = PLAYER_GAUGE + SELECTED_PLAYER[1]


        if PLAYER_HEALTH <= 0:
            EXIT_FLAG = True


        print ("--- FIN DE TURNO ---")
        sleep(TICK_RATE)

else:
    print("chupa la que cuelga")
