data = []
with open("day1.txt", "r") as f:
    for line in f:
        line.split('\n')
        data.append(int(line))

n = len(data)
ans = 0

current_sum = sum(data[:3])
prev_sum = 1
for i in range(n - 3):
    if current_sum > prev_sum:
        ans += 1

    prev_sum = current_sum
    current_sum -= data[i]
    current_sum += data[i + 3]
