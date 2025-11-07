"""Juego de Piedra, Papel o Tijera con comentarios detallados."""

import random

# Diccionario que relaciona cada opción con un emoji para hacerlo más vistoso en pantalla.
OPCIONES = {
    "piedra": "🪨 Piedra",
    "papel": "📄 Papel",
    "tijera": "✂️ Tijera",
}

# Lista con las claves válidas para facilitar validaciones y elecciones aleatorias.
OPCIONES_VALIDAS = list(OPCIONES.keys())


def mostrar_menu():
    """Muestra en pantalla el menú de bienvenida y las instrucciones básicas."""
    print("=" * 50)
    print("🎮  ¡Bienvenido al clásico juego de Piedra, Papel o Tijera!  🎮")
    print("=" * 50)
    print("Instrucciones:")
    print("1. Escribe 'piedra', 'papel' o 'tijera' para elegir tu jugada.")
    print("2. El ordenador elegirá al azar su jugada.")
    print("3. Gana la opción que venza según las reglas tradicionales:")
    print("   - Piedra aplasta Tijera")
    print("   - Tijera corta Papel")
    print("   - Papel envuelve Piedra")
    print("4. Puedes escribir 'salir' en cualquier momento para terminar el juego.")
    print("¡Buena suerte! ✨\n")


def obtener_eleccion_jugador():
    """Pide al usuario que introduzca su elección y la valida."""
    while True:
        print("Opciones disponibles: 🪨 piedra | 📄 papel | ✂️ tijera | 🚪 salir")
        eleccion = input("¿Cuál es tu jugada? -> ").strip().lower()

        # Se permite al jugador abandonar el juego en cualquier momento.
        if eleccion == "salir":
            return eleccion

        # Validamos que la elección esté dentro del conjunto permitido.
        if eleccion in OPCIONES_VALIDAS:
            return eleccion

        # Si llega aquí, la palabra escrita no es válida.
        print("❗ Entrada no reconocida. Intenta de nuevo con 'piedra', 'papel', 'tijera' o 'salir'.\n")


def obtener_eleccion_computadora():
    """Devuelve una elección aleatoria para la computadora."""
    # random.choice selecciona un elemento al azar de la lista proporcionada.
    return random.choice(OPCIONES_VALIDAS)


def determinar_ganador(eleccion_jugador, eleccion_computadora):
    """Compara ambas elecciones y devuelve el resultado de la ronda."""
    if eleccion_jugador == eleccion_computadora:
        # Empate si ambas elecciones son idénticas.
        return "empate"

    # Reglas básicas del juego expresadas como pares ganadores.
    combinaciones_ganadoras = {
        ("piedra", "tijera"),
        ("tijera", "papel"),
        ("papel", "piedra"),
    }

    # Si la tupla (jugador, computadora) está en el conjunto, gana el jugador.
    if (eleccion_jugador, eleccion_computadora) in combinaciones_ganadoras:
        return "jugador"

    # En caso contrario, gana la computadora.
    return "computadora"


def mostrar_resultado(eleccion_jugador, eleccion_computadora, resultado, puntos_jugador, puntos_computadora):
    """Imprime el resultado de la ronda junto con la puntuación acumulada."""
    print("\n" + "-" * 50)
    print("Tu elección:        ", OPCIONES[eleccion_jugador])
    print("Elección computadora:", OPCIONES[eleccion_computadora])

    if resultado == "empate":
        print("Resultado: 🤝 ¡Empate!")
    elif resultado == "jugador":
        print("Resultado: 🏆 ¡Ganaste esta ronda!")
    else:
        print("Resultado: 💻 La computadora ganó la ronda.")

    print("Marcador -> Tú: {0} | Computadora: {1}".format(puntos_jugador, puntos_computadora))
    print("-" * 50 + "\n")


def jugar_ronda():
    """Gestiona el flujo de una ronda: obtener elecciones y determinar ganador."""
    eleccion_jugador = obtener_eleccion_jugador()

    # Si el jugador desea salir, indicamos esta intención al código que llama.
    if eleccion_jugador == "salir":
        return None, None, "salir"

    eleccion_computadora = obtener_eleccion_computadora()
    resultado = determinar_ganador(eleccion_jugador, eleccion_computadora)
    return eleccion_jugador, eleccion_computadora, resultado


def main():
    """Función principal que mantiene el bucle de juego en marcha."""
    mostrar_menu()

    # Variables que almacenan los puntos acumulados de cada participante.
    puntos_jugador = 0
    puntos_computadora = 0

    while True:
        eleccion_jugador, eleccion_computadora, resultado = jugar_ronda()

        # Si el resultado indica que el jugador escribió 'salir', cerramos el bucle.
        if resultado == "salir":
            print("Gracias por jugar. ¡Hasta la próxima! 👋")
            break

        # Actualizamos marcadores según el resultado obtenido.
        if resultado == "jugador":
            puntos_jugador += 1
        elif resultado == "computadora":
            puntos_computadora += 1

        mostrar_resultado(
            eleccion_jugador,
            eleccion_computadora,
            resultado,
            puntos_jugador,
            puntos_computadora,
        )


# Punto de entrada convencional de un programa en Python.
if __name__ == "__main__":
    main()
