def circle(n):
    qtd = 0
    while True:
        qtd += 1
        if n == 1:
            break
        n = (3*n + 1) if n%2 != 0 else n//2
    return qtd

while True:
    try:
        x, y = map(int, input().split())
        ans, a, b = 0, min([x, y]), max([x, y])
        while a <= b:
            ans = max(ans, circle(a))
            a += 1
        print(x, y, ans)
    except EOFError:
        break
