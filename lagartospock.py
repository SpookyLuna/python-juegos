import random
import time

def main():

    
    #Añadir imagen ascii por cada opción
    #ascii_art = {}

    #Posibilidades
    opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]


    #Inicio de bucle jugable

    while True:

        while True:

            #\n Introduce el input en la siguiente linea
            turno_jugador = input("¿Piedra, papel, tijera, lagarto o Spock?\n").lower().strip()
            if turno_jugador in ["piedra", "papel", "tijera", "lagarto", "spock"]:
                break
            else:
                print("Opción incorrecta")

        
        #print(ascii_art{turno_jugador})
        print(f"*Sacas {turno_jugador}*")

        turno_bot = random.choice(opciones)
        #print(ascii_art{turno_bot})
        print(f"*Tu contrincante saca {turno_bot}*")

        #Reglas
        if turno_jugador == "piedra" and turno_bot == "piedra":
            print("¡Empate!")
        elif turno_jugador == "tijera" and turno_bot == "tijera":
            print("¡Empate!")
        elif turno_jugador == "papel" and turno_bot == "papel":
            print("¡Empate!")
        elif turno_jugador == "spock" and turno_bot == "spock":
            print("¡Empate!")
        elif turno_jugador == "lagarto" and turno_bot == "lagarto":
            print("¡Empate!")
        elif turno_jugador == "tijeras" and turno_bot == "papel":
            print("¡Has ganado, tijeras cortan papel!")
        elif turno_jugador == "papel" and turno_bot == "piedra":
            print("¡Has ganado, papel envuelve a piedra!")
        elif turno_jugador == "piedra" and turno_bot == "lagarto":
            print("¡Has ganado, piedra aplasta lagarto!")                  
        elif turno_jugador == "lagarto" and turno_bot == "spock":
            print("¡Has ganado, lagarto envenena a Spock!")
        elif turno_jugador == "spock" and turno_bot == "tijeras":
            print("¡Has ganado, Spock aplasta dijeras!")                                                                                                                                                          
        elif turno_jugador == "tijeras" and turno_bot == "lagarto":
            print("¡Has ganado, tijeras decapitan lagarto!")
        elif turno_jugador == "lagarto" and turno_bot == "papel":
            print("¡Has ganado, lagarto se come papel!")
        elif turno_jugador == "papel" and turno_bot == "spock":
            print("¡Has ganado, papel desaprueba a Spock!")
        elif turno_jugador == "spock" and turno_bot == "piedra":
            print("¡Has ganado, Spock desintegra piedra!")
        elif turno_jugador == "piedra" and turno_bot == "tijera":
            print("¡Has ganado, piedra aplasta tijera!")
        else:
            print("¡Has perdido!")                                                                                       
        time.sleep(1)                                
    
if __name__ == '__main__':
    main()




