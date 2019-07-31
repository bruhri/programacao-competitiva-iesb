def dividir(palavra):
    tamanho = len(palavra)
    if tamanho%2 == 1:
        return palavra
    tamanho = tamanho // 2
    lado_esquerdo = dividir(palavra[:tamanho])
    lado_direito = dividir(palavra[tamanho:])
    if lado_esquerdo < lado_direito:
        return lado_esquerdo + lado_direito 
    else:
        return lado_direito + lado_esquerdo

palavra1, palavra2 = input(), input()
print('YES' if dividir(palavra1) == dividir(palavra2) else "NO")