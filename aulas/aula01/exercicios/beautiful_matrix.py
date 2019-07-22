x, y = 0, 0
for i in range(5):
    for j, number in enumerate(input().split()):
        if number == '1':
            x, y = i, j
tx, ty = abs(x - 2), abs(y - 2)
print(tx+ty)