n, m = map(int, input().split())
direita = True
for i in range(n):
    if i%2 == 0:
        print("#"*m)
    else:
        if direita:
            print("."*(m-1), "#", sep='')
            direita = False
        else:
            print("#", "."*(m-1), sep='')
            direita = True