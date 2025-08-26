def contar_vocales(frase):
    if frase == "": #Caso base -> Al recortar la frase nos quedamos con ""
        return 0
    else:
        if frase[0] in "aeiouAEIOU":
            return 1 + contar_vocales(frase[1:]) #Recursión -> Si es vocal, sumamos 1 y volvemos a llamar a la función
        else:
            return contar_vocales(frase[1:]) #Recusión -> Si no es vocal, solo llamamos a la función

if __name__ == "__main__":
    frase = input("Palabra: ")
    vocales = contar_vocales(frase)

    print(f"La palabra '{frase}' tiene {vocales} vocales")