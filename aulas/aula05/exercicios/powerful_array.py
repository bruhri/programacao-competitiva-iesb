from collections import Counter

tamanho, consultas = map(int, input().split())
numeros = list(map(int, input().split()))
contagem = [0]*tamanho

for i in range(tamanho):
    contagem[i] = Counter(numeros[:i+1])

