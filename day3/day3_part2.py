with open('day3_input') as f:
    data = [x for x in f.read().split()]

gamma_rate = ''
eplision_rate = ''
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    one_array = []
    zero_array = []
    for i in range(0, len(data)):
        if data[i][index] == '0':
            zero += 1
            zero_array.append(data[i])
        else:
            one += 1
            one_array.append(data[i])
    if zero > one:
        data = zero_array
    else:
        data = one_array
    index += 1

oxygen = int(data[0], 2)

while len(data) > 1:
    one = 0
    zero = 0
    one_array = []
    zero_array = []
    for i in range(0, len(data)):
        if data[i][index] == '0':
            one += 1
            one_array.append(data[i])
        else:
            zero += 1
            zero_array.append(data[i])
    if one < zero:
        data = one_array
    else:
        data = zero_array
    index += 1
co2 = int(data[0], 2)
print(co2 * oxygen)