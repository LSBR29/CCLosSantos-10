# Escriba aquí las clases Sensor, SensorTemperatura, SensorHumedad y Estacion.
# Si realiza el extra, escriba también ExportableMixin y SensorHumedadExportable.


if __name__ == "__main__":
    estacion = Estacion("Laboratorio de Los Santos")
    estacion.agregar_sensor(SensorTemperatura("T1", "Servidores", 35))
    estacion.agregar_sensor(SensorTemperatura("T2", "Oficina", 28))
    estacion.agregar_sensor(SensorHumedad("H1", "Servidores"))

    lecturas = [("T1", 31.5), ("T2", 24.0), ("H1", 45), ("T1", 36.2),
                ("H1", 120), ("T3", 20), ("T2", 25.5), ("H1", 28), ("T2", 26.0)]

    rechazadas = 0
    for codigo, valor in lecturas:
        if not estacion.registrar_lectura(codigo, valor):
            rechazadas += 1

    for sensor in estacion.sensores:
        print(sensor)
    print("Lecturas rechazadas:", rechazadas)

    print("Sensores en alerta:")
    for sensor in estacion.alertas():
        print(sensor.codigo)

    print("Total de lecturas:", estacion.total_lecturas())

    # Extra (quite el comentario si lo implementó)
    # h2 = SensorHumedadExportable("H2", "Bodega")
    # h2.registrar(50)
    # h2.registrar(60)
    # print(h2.a_csv())