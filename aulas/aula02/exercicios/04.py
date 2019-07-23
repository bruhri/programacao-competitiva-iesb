movimentos, doces_final = map(int, input().split())
left, right = 0, movimentos + 1

while left < right -1 :
    media = (left + right)//2
    cedidos = (media * (media + 1)) // 2
    comidos = movimentos - media
    if cedidos - comidos > doces_final:
        right = media
    else:
        left = media
print(movimentos - left)