import random

# Definimos los palos y los valores de las cartas
palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
valores = {
    'A': 11,  # El As vale 11, pero más adelante en el juego se puede ajustar a 1.
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
    'J': 10, 'Q': 10, 'K': 10
}

class Baraja:
    def __init__(self):
        self.cartas = []
        self.crear_baraja()

    def crear_baraja(self):
        """Crea una baraja de 52 cartas con sus palos y valores"""
        self.cartas = [(valor, palo) for palo in palos for valor in valores]
    
    def barajar(self):
        """Mezcla la baraja"""
        random.shuffle(self.cartas)

    def repartir_carta(self):
        """Devuelve una carta de la baraja (la última)"""
        return self.cartas.pop()

    def mostrar_carta(self, carta):
        """Devuelve una representación en cadena de una carta"""
        valor, palo = carta
        return f"{valor} de {palo}"

def valor_carta(carta):
    """Devuelve el valor numérico de una carta"""
    valor = carta[0]
    return valores[valor]

def calcular_valor_mano(mano):
    """Calcula la suma total del valor de la mano"""
    total = sum(valor_carta(carta) for carta in mano)
    # Ajustamos el valor de Ases si el total excede 21
    ases = sum(1 for carta in mano if carta[0] == 'A')
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1
    return total
