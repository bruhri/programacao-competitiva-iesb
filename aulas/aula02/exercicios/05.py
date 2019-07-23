from collections import Counter

pessoas, pacotes = map(int,input().split())
comidas = map(int, input().split())
vetor = list(Counter(comidas).values())
dias = pacotes//pessoas
while dias > 0:
    if sum([comida//dias for comida in vetor]) >= pessoas:
        break
    dias-=1
print(dias)