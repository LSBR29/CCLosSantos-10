class Dispositivo():
    #Eliminar pass y completar
    pass

class DispositivoInteligente():
    #Eliminar pass y completar
    pass

class Gestor():
    #Eliminar pass y completar
    pass

if __name__ == "__main__":
    gestor = Gestor()

    try:
        bombillo = DispositivoInteligente(nombre="Bombillo LED", consumo=25, horas_dia=6, modo=True)
        enchufe = DispositivoInteligente(nombre="Enchufe WiFi", consumo=20, horas_dia=12)
    except:
        print("Hubo un error al crear los objetos")
        exit()

    gestor.agregar_dispositivo(bombillo)
    gestor.agregar_dispositivo(enchufe)

    gestor.mostrar_todos()
    print(f"El {gestor.mayor_consumo().nombre} es el que consume más energía")

    #Puntos Extra
    #print(f"El {gestor.menor_consumo().nombre} es el que consume menos energía")