import medidas

if __name__ == "__main__":
    try:
        metros = float(input("Ingresa una distancia en metros: "))
        centimetros = medidas.metros_a_centimetros(metros)
        kilometros = medidas.metros_a_kilometros(metros)

        print(f"{metros} metros son {centimetros} centímetros.")
        print(f"{metros} metros son {kilometros} kilómetros.")
        
    except:
        print("Por favor, ingresa un número válido.")