import random

# Clase para los objetos pregunta
class Pregunta:
    """Clase que representa una pregunta del juego."""
    def __init__(self, dificultad: int, texto: str, opciones: list):
        """Inicializa una pregunta con dificultad, texto, opciones y respuesta correcta."""
        self.dificultad = dificultad
        self.texto = texto
        self.opciones = opciones
        self.__respuesta_correcta = ""

    # Getter y Setter para establecer la respuesta
    @property
    def respuesta(self):
        return self.__respuesta_correcta
    @respuesta.setter
    def respuesta(self, valor):
        if valor in ["A", "B", "C", "D"]:
            self.__respuesta_correcta = valor
        else:
            raise ValueError

    def mostrar_pregunta(self):
        """Devuelve un string con el número de nivel, el texto y las opciones etiquetadas."""
        texto = f"{self.dificultad}: {self.texto}\n"
        letras = ["A", "B", "C", "D"]

        # Recorre las opciones y las muestra junto con su letra
        for i in range(len(letras)):
            texto += f"{letras[i]}) {self.opciones[i]}\n"

        print(texto)

    def verificar_respuesta(self, respuesta_usuario: str):
        """Verifica si la respuesta del usuario coincide con la letra de la respuesta correcta."""
        return respuesta_usuario == self.respuesta


# Mixin: Comodín 50:50
class Comodin5050Mixin:
    """Permite eliminar dos opciones incorrectas y mostrar solo dos posibles respuestas."""
    def usar_5050(self, pregunta: Pregunta):
        """Ejecuta el comodín 50:50 sobre una pregunta dada."""
        opciones = pregunta.opciones.copy()
        letras = ["A", "B", "C", "D"]

        texto = ""
        # Recorre las 4 opciones buscando la correcta
        for i in range(4):
            if letras[i] == pregunta.respuesta:
                # Imprime la opción correcta
                texto += f"{letras[i]}) {opciones[i]}\n"

                # Elimina esa opción de las listas
                opciones.pop(i)
                letras.pop(i)

                # Selecciona aleatoriamente una incorrecta restante
                aleatoria = random.randint(0, 2)
                texto += f"{letras[aleatoria]}) {opciones[aleatoria]}\n"

                break

        # Muestra las dos opciones que quedan
        print(texto)


# Mixin: Comodín Cambio de Pregunta
class ComodinCambioMixin:
    """Permite cambiar la pregunta actual por otra del mismo nivel."""
    def usar_cambio(self, nivel: int, preguntaActual: Pregunta):
        """Selecciona una nueva pregunta del mismo nivel, diferente de la actual."""
        nueva = self.seleccionar_pregunta(nivel)
        
        # Evita que la nueva pregunta sea la misma
        while nueva == preguntaActual:
            nueva = self.seleccionar_pregunta(nivel)
        
        print("\n--- Pregunta cambiada ---")
        
        return nueva


# Clase principal del juego
class Juego(Comodin5050Mixin, ComodinCambioMixin):
    """Clase principal que gestiona el juego completo."""
    def __init__(self):
        """Inicializa el juego, niveles, premios y comodines."""
        self.preguntas = []                # Lista de objetos Pregunta
        self.nivel_actual = 1              # Nivel inicial
        self.jugando = True                # Control del estado del juego
        self.comodines_usados = {          # Estado de los comodines
            "50:50": False,
            "cambio": False,
        }

        # Diccionario con premios por nivel
        self.premios = {
            15: 30000000, 14: 15000000, 13: 10000000, 12: 7500000, 11: 5000000,
            10: 3000000, 9: 2000000, 8: 1500000, 7: 1000000, 6: 650000,
            5: 500000, 4: 400000, 3: 300000, 2: 200000, 1: 100000
        }

    def cargar_preguntas(self, ruta: str):
        """Carga las preguntas desde un archivo CSV separado por comas."""
        with open(ruta, "r", encoding='utf-8') as archivo:
            for l in archivo.readlines():
                linea = l.strip().split(",")

                # Extrae los datos de la línea
                dificultad = int(linea[0])
                texto = linea[1]
                opciones = [linea[2], linea[3], linea[4], linea[5]]
                respuesta = linea[6]
                
                # Crea y guarda el objeto Pregunta
                preg = Pregunta(dificultad, texto, opciones)
                
                try:
                    preg.respuesta = respuesta
                    self.preguntas.append(preg)
                except:
                    print("Error: Una de las preguntas tiene una respuesta inválida")  
                    raise ValueError

    def seleccionar_pregunta(self, nivel: int):
        """Devuelve una pregunta aleatoria del nivel solicitado."""
        disponibles = []
        # Recorre todas las preguntas y selecciona las del nivel actual
        for p in self.preguntas:
            if p.dificultad == nivel:
                disponibles.append(p)

        # Devuelve una pregunta aleatoria del conjunto
        return disponibles[random.randint(0, len(disponibles)-1)]

    def calcular_premio(self, correcto: bool):
        """Calcula el premio que corresponde según el avance o pérdida del jugador."""
        if correcto:
            # Si ganó el nivel o llegó al final
            if self.nivel_actual == 15:
                return self.premios[15]
            else:
                if self.nivel_actual == 1:
                    return 0
                # Devuelve el premio del nivel anterior
                return self.premios[self.nivel_actual - 1]
        else:
            # Si perdió, aplica las zonas seguras
            if self.nivel_actual > 10:
                return self.premios[10]
            elif self.nivel_actual > 5:
                return self.premios[5]
            else:
                return 0

    def mostrar_comodines(self):
        """Muestra en pantalla los comodines que aún no se han usado."""
        print("-----------------------------------------")
        print("Comodines disponibles:")

        # Imprime solo los que no se han usado
        for comodin, estado in self.comodines_usados.items():
            if not estado:
                print(f" - {comodin}")
        print("-----------------------------------------")

    def usar_comodin(self, tipo: str, preguntaActual: Pregunta):
        """Ejecuta el comodín seleccionado, si está disponible."""
        # Comodín 50:50
        if tipo == "50:50" and not self.comodines_usados["50:50"]:
            self.usar_5050(preguntaActual)
            self.comodines_usados["50:50"] = True

        # Comodín cambio de pregunta
        elif tipo == "CAMBIO" and not self.comodines_usados["cambio"]:
            preguntaNueva = self.usar_cambio(self.nivel_actual, preguntaActual)
            self.comodines_usados["cambio"] = True
            return preguntaNueva

        else:
            print("Comodín inválido o ya usado.")
