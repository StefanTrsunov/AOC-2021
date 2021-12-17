with open('day7_input') as f:
    data = f.readline().split(',')

#print(data)
data = list(map(int, data))
min_fuel = 2 ** 31
for i in range(min(data), max(data) + 1):
    fuel = 0
    for number in data:
        fuel += abs(int(number) - int(i))
    min_fuel = min(min_fuel, fuel)

print(min_fuel)