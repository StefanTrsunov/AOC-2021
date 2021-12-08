with open('day6_input') as f:
    data = [int(x) for x in f.readline().split(',')]
    new_fish = 8
    day = 1
    for day in range(1, 81):
        for i in range(len(data)):
            if data[i] == 0:
                data[i] = 6
                data.append(8)
            else:
                data[i] -= 1

    print('Size', len(data))