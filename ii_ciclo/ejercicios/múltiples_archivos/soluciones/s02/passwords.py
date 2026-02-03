import random

def generar_password(longitud):
    letras_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minus = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiales = "!@#$%^&*()-_=+[]{};:,.<>?/|\\"

    posibles = letras_mayus + letras_minus + numeros + especiales

    password = ""
    while len(password) != longitud:
        indice = random.randint(0, len(posibles) - 1)
        password += posibles[indice]

    return password