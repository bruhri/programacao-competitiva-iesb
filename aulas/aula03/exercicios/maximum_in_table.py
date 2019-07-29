n = int(input())
linha = [1]*n
for _ in range(n-1):
    nova_linha = list()
    for i in range(1, n+1):
        nova_linha.append(sum(linha[:i]))
    linha = nova_linha
print(linha[-1])