data = []
with open("day1.in") as f:
    for line in f:
        line.split('\n')
        data.append(int(line))


n = len(data)
ans = 0

for i in range(1, n):
    if data[i] > data[i - 1]:
        ans += 1

print(ans)

