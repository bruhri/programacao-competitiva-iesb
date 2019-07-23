from queue import PriorityQueue


def get_na_fila(show_snack, maior):
    while True:
        if fila_preferencia.empty():
            break

        snack = -1*fila_preferencia.get()
        if snack == maior:
            show_snack.append(snack)
            maior -= 1
        else:
            fila_preferencia.put(-1*snack)
            break
    return maior

maior = int(input())
snacks = map(int, input().split())
fila_preferencia, show_snack = PriorityQueue(), list()


for snack in snacks:    
    if snack == maior:
        show_snack.append(snack)
        maior -= 1
        maior = get_na_fila(show_snack, maior)
        print(*show_snack)
        show_snack = list()
    else:
        fila_preferencia.put(-1*snack)
        print()
    
            
