#Pedimos las palabras
palabra1, palabra2 = input("Ingrese dos palabras separadas por un espacio: ").split()

#Verificar cuál palabra es más larga
if len(palabra1) > len(palabra2):
    print(f"La palabra '{palabra1}' es más larga que '{palabra2}'")

elif len(palabra1) < len(palabra2):
    print(f"La palabra '{palabra2}' es más larga que '{palabra1}'")
    
else:
    print(f"Las palabras '{palabra1}' y '{palabra2}' son del mismo largo")
