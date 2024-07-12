import random

def main():

    #Lista de Palabras
    palabras = ["coche", "dinosaurio", "mono", "columna", "movil", "banana", "manzana", "ascensor", "austrolopitecus", "dinosaurio", "autobus", "casa", "causa", "pera", "hermoso"]

    letras_acertadas = []

    Fallos = 0

    ahorcado = '''


    +---+
        |
        |
        |
        |
    =======    

    '''

    nombre_jugador = input ("Introduce tu nombre:\n")

    palabra_escogida = random.choice(palabras)
    #print(palabra_escogida)
    numero_letras = len(palabra_escogida)

    tablero = "_" * numero_letras
    
    print(ahorcado)
    print(tablero)
    
    #Comienza el juego
    while True:

        introduce_letra = input ("Introduce una letra:\n").lower()
    
        if introduce_letra in palabra_escogida:
            posicion_letra = palabra_escogida.find(introduce_letra)
            #print(posicion_letra)
            #print("_"*numero_letras)

            letras_acertadas.append(introduce_letra)

            tablero = ''.join([letra if letra in letras_acertadas else '_' for letra in palabra_escogida])

        elif introduce_letra not in palabra_escogida:
            Fallos = Fallos + 1
            #print(Fallos)

        print(tablero)


        if "_" not in tablero:
            print("¡Has ganado!")
            break
            

        match Fallos:
            case 1:
                print(
                '''
                +---+
                |   |
                    |
                    |
                    |
                =======    

                ''')


            case 2:
                print(
                '''
                +---+
                |   |
                O   |
                    |
                    |
                =======    

                ''')

            case 3:
                print(
                '''
                +---+
                |   |
                O   |
                |   |
                    |
                =======    

                ''')

            case 4:
                print(
                '''
                +---+
                |   |
                O   |
               -|   |
                    |
                =======    

                ''')

            case 5:
                print(
                '''
                +---+
                |   |
                O   |
               -|-  |
                    |
                =======    

                ''')             
            case 6:
                print(
                '''
                +---+
                |   |
                O   |
               -|-  |
               /    |
                =======    

                ''')

            case 7:
                print(
                '''
                +---+
                |   |
                O   |
               -|-  |
               / \  |
                =======    

                ''')

        if Fallos == 7:
            print("¡Has perdido!")
            break

if __name__ == '__main__':
    while True:
        main()

