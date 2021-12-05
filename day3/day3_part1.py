with open('day3_input') as f:
    data = [x for x in f.read().split()]

gamma_rate = ''
epsilon_rate = ''
for i in range(0, len(data[0])):
    zero = 0
    one = 0
    for c in range(0, len(data)):
        if data[c][i] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))