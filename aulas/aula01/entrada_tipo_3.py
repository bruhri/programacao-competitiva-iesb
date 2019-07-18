while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    print(x+y)