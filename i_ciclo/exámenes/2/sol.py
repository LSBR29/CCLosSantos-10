# Función para pedir una respuesta al usuario
def pedir_respuesta(pregunta):
    # Recibe una pregunta (string) y retorna la respuesta ingresada por el usuario.
    respuesta = input(f"{pregunta}\n> ")
    return respuesta

# Función para verificar si la respuesta es correcta (sin distinguir mayúsculas)
def es_correcta(respuesta_usuario, respuesta_correcta):
    # Retorna True si coinciden (ignorando mayúsculas/minúsculas), False en caso contrario.
    return respuesta_usuario.lower() == respuesta_correcta.lower()

# Función para calcular el porcentaje de aciertos
def calcular_porcentaje(aciertos, total):
    # Calcula el porcentaje de respuestas correctas.
    if total == 0:
        porcentaje = 0
    else:
        porcentaje = (aciertos / total) * 100
    return porcentaje

# Bloque principal del programa
if __name__ == "__main__":
    # Diccionario con preguntas y respuestas correctas
    # Se incluyen 5 preguntas adicionales para obtener puntos extra
    preguntas = {
        "¿Capital de Costa Rica?": "San José",
        "¿Cuál es el número primo más pequeño?": "2",
        "¿Qué partícula tiene carga eléctrica negativa?": "Electrón",
        "¿Cómo se llama el área que estudia los hongos?": "Micología",
        "¿Qué fuerza se opone al movimiento de un cuerpo?": "Fricción",
        "¿Cuál es el valor de pH que se considera neutro?": "7",
        "¿Cuántos cromosomas tiene el ser humano?": "46"
    }

    # Inicializar contador de aciertos
    aciertos = 0
    total_preguntas = len(preguntas)

    # Recorrer todas las preguntas del diccionario
    for pregunta, respuesta_correcta in preguntas.items():
        # Pedir respuesta al usuario
        respuesta_usuario = pedir_respuesta(pregunta)

        # Verificar si la respuesta es correcta
        if es_correcta(respuesta_usuario, respuesta_correcta):
            print("Correcto\n")
            aciertos += 1
        else:
            print("Incorrecto\n")

    # Mostrar resultados finales
    print(f"Aciertos: {aciertos}")
    porcentaje = calcular_porcentaje(aciertos, total_preguntas)
    print(f"Porcentaje obtenido: {porcentaje}%")