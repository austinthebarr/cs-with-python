x = '11001'

ans = 0
count = 0
# right to left
# 1 0 position
# 0 1 position
# 1 2 position
# 1 3 postion

for i in x:
    ans += int(i) * (2**count)
    count += 1

print(ans)