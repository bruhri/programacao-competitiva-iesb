n, m = map(int, input().split())
pool, saida, qtd = [0]*n, list(), 0
for problem in map(int, input().split()):
    pool[problem-1] += 1
    if pool[problem-1] == 1:
        qtd += 1
        if qtd == n:
            saida.append('1')
            for i in range(n):
                pool[i] -= 1
            qtd = n - pool.count(0)
            continue
    saida.append('0')
print(''.join(saida))