qtd = int(input())
for _ in range(qtd):
    tam = int(input())
    number = input()
    pos = number.find('8')
    if pos != -1 and tam - pos >= 11:
        print('YES')
    else:
        print('NO')