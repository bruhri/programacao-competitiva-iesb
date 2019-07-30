a, b = map(int, input().split())
wa, wb, ww = 0, 0, 0
for vd in [1, 2, 3, 4, 5, 6]:
    if abs(a - vd) < abs(b - vd):
        wa += 1
    elif abs(a - vd) > abs(b - vd):
        wb += 1
    else:
        ww += 1
print(wa, ww, wb)