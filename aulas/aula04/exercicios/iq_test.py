matriz = [input() for _ in range(4)]
for i in range(3):
    for j in range(3):
        count = 0
        if matriz[i][j] == '#':
            count += 1
        if matriz[i][j+1] == '#':
            count += 1
        if matriz[i+1][j] == '#':
            count += 1
        if matriz[i+1][j+1] == '#':
            count += 1
        if count != 2:
            print('YES')
            exit()
print('NO')
