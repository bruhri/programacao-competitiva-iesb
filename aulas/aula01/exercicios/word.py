lower, upper = 0, 0
texto = input()
for letra in texto:
    if 65 <= ord(letra) <= 90:
        upper += 1
    else:
        lower += 1
print(texto.upper() if upper > lower else texto.lower())

