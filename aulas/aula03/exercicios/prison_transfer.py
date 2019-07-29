presos, crime_maximo, tamanho_maximo = map(int, input().split())
crimes = map(int, input().split())
possiveis, fila_atual = 0, 0
for crime in crimes:
    if crime <= crime_maximo:
        fila_atual += 1
        if fila_atual >= tamanho_maximo:
            possiveis += 1
    else:
        fila_atual = 0
print(possiveis)
