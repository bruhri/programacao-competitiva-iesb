size = int(input())
students = list(sorted(map(int, input().split())))
left, right, ans = 0, 0, 0
while left < size and right < size:
    if students[right] - students[left] <= 5:
        ans = max(ans, right-left+1)
        right += 1
    elif left == right:
        right += 1
    else:
        left += 1
print(ans)

