def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)

nombre = 5
print(f"La factorielle de {nombre} est {factoriel(nombre)}")