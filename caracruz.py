import random
import time

def main():

    #Opciones
    opciones = ["cara", "cruz"]

    #ASCII ART
    ascii_art = {
        'cara': '''
     _______
    /       \\
   /  ____   \\
  |  |    |   |
  |  |____|   |
   \\         /
    \\_______/  
        ''',
        'cruz': '''
     _______
    /       \\
   /         \\
  (    € €    )
   \\         /
    \\_______/
        '''
    }

    #Juego
    while True:

        while True:

            turno_jugador = input("¿Cara o cruz?\n").lower().strip()
            if turno_jugador in ["cara", "cruz"]:
                break
            else:
                print("Opción incorrecta")


        print(f"Has escogido {turno_jugador}")

        eleccion_bot = random.choice(opciones)
        print(f"Tu contrincante ha escogido {eleccion_bot}")

        tirar_moneda = random.choice(opciones)
        print(f"Se lanza la moneda y care en {tirar_moneda}")
        print(ascii_art[tirar_moneda])

        time.sleep(1)

        if turno_jugador == tirar_moneda:
            print(f"¡Has ganado!")
        else:
            print(f"¡Has perdido!")

        time.sleep(1)

if __name__ == '__main__':
    main()

