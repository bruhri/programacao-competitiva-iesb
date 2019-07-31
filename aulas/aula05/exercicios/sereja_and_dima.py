pointer_right = int(input())  - 1
sereja_points, dima_points = 0, 0
cards = list(map(int, input().split()))
pointer_left = 0

for iteretion in range(len(cards)):
    card_choiced = -1
    if cards[pointer_right] > cards[pointer_left]:
        card_choiced = cards[pointer_right]
        pointer_right -= 1
    else:
        card_choiced = cards[pointer_left]
        pointer_left += 1

    if iteretion % 2 == 0:
        sereja_points += card_choiced
    else:
        dima_points += card_choiced

print(sereja_points, dima_points)