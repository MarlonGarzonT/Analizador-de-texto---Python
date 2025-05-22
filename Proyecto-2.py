texto = input("Ingrese el texto a su eleccion: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letras: ").lower())
letras.append(input("Ingresa la primera letras: ").lower())
letras.append(input("Ingresa la primera letras: ").lower())

##CANTIDAD DE LETRAS
print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])


print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

##CANTIDAD DE PALABRAS

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

##Letras de inicio a fin

print("\n")
print("LETRAS DE INICIO A FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra del final es '{letra_final}'")

##TEXTO INVERTIDO

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texo al revés va decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_pyton= 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'python' {dic[buscar_pyton]} se encuentra en el texto")