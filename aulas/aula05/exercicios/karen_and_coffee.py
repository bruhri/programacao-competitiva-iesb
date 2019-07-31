recipes, min_recipes, questions = map(int, input().split())
recipes_temp = [0]*200002

for _ in range(recipes):
    l, r = map(int, input().split())
    recipes_temp[l] += 1
    recipes_temp[r+1] -= 1

for i in range(1, 200002):
    recipes_temp[i] = recipes_temp[i-1] + recipes_temp[i]

for i in range(1, 200002):
    recipes_temp[i] = 1 if recipes_temp[i] >= min_recipes else 0

for i in range(1, 200002):
    recipes_temp[i] = recipes_temp[i-1] + recipes_temp[i]

resp = list()
for _ in range(questions):
    l, r = map(int, input().split())
    resp.append(recipes_temp[r] - recipes_temp[l-1])
print(*resp, sep='\n')

