vetor = list(map(int, input().split()))
find = int(input())
inicio, fim = 0, len(vetor)
while inicio < fim:
    media = (inicio+fim)//2
    print(inicio, fim, vetor[inicio:fim], vetor[media])
    if find == vetor[media]:
        print('YES')
        exit()
    if vetor[media] < find:
        inicio = media+1
    else:
        fim = media
print('NO')
    
