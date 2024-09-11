from baraja import Baraja, calcular_valor_mano

def jugar_blackjack():
    dinero = 500  # Dinero inicial

    print("¡Bienvenido al Black Jack!")
    print(f"Empiezas con {dinero} unidades de dinero.")
    
    # Bucle principal del juego
    while 0 < dinero < 1000:
        print(f"\nTienes {dinero} unidades de dinero.")
        
        # Apuesta
        while True:
            try:
                apuesta = int(input(f"¿Cuánto deseas apostar? (Tienes {dinero}): "))
                if 1 <= apuesta <= dinero:
                    break
                else:
                    print("Apuesta inválida. Debes apostar una cantidad positiva y que no exceda tu dinero.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
        # Inicializamos la baraja y la barajamos
        baraja = Baraja()
        baraja.barajar()
        
        # Inicializamos las manos del jugador y de la banca
        mano_jugador = []
        mano_banca = []

        # Repartimos dos cartas al jugador y a la banca
        mano_jugador.append(baraja.repartir_carta())
        mano_jugador.append(baraja.repartir_carta())
        mano_banca.append(baraja.repartir_carta())
        mano_banca.append(baraja.repartir_carta())
        
        jugando = True

        # Turno del jugador
        while jugando:
            print("\nTu mano:", ", ".join(baraja.mostrar_carta(carta) for carta in mano_jugador))
            print("Valor de tu mano:", calcular_valor_mano(mano_jugador))
            
            if calcular_valor_mano(mano_jugador) > 21:
                print("Te pasaste de 21. ¡Perdiste!")
                dinero -= apuesta  # El jugador pierde la apuesta
                break

            accion = input("¿Quieres pedir otra carta? (s/n): ").lower()

            if accion == 's':
                mano_jugador.append(baraja.repartir_carta())
            else:
                jugando = False

        if calcular_valor_mano(mano_jugador) <= 21:
            # Turno de la banca
            print("\nTurno de la banca...")
            while calcular_valor_mano(mano_banca) < 17:
                mano_banca.append(baraja.repartir_carta())
            
            print("Mano de la banca:", ", ".join(baraja.mostrar_carta(carta) for carta in mano_banca))
            print("Valor de la mano de la banca:", calcular_valor_mano(mano_banca))

            # Resultados
            valor_jugador = calcular_valor_mano(mano_jugador)
            valor_banca = calcular_valor_mano(mano_banca)
            
            if valor_banca > 21:
                print("La banca se pasó de 21. ¡Ganaste!")
                dinero += apuesta  # El jugador gana la apuesta
            elif valor_jugador > valor_banca:
                print("¡Ganaste! Tu mano es mejor que la de la banca.")
                dinero += apuesta  # El jugador gana la apuesta
            elif valor_jugador == valor_banca:
                print("Es un empate. No ganas ni pierdes dinero.")
            else:
                print("La banca gana. ¡Perdiste!")
                dinero -= apuesta  # El jugador pierde la apuesta
        
        if dinero <= 0:
            print("\nTe has quedado sin dinero. ¡Fin del juego!")
        elif dinero >= 1000:
            print("\n¡Felicidades! Has alcanzado 1000 unidades de dinero. ¡Has ganado el juego!")
    
if __name__ == '__main__':
    jugar_blackjack()
