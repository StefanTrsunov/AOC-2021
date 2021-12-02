with open('day2_input') as f:
    data = f.readlines()
    forward = 0
    depth = 0
    aim = 0
    for line in data:
        key, value = line.split()
        value = int(value)
        if key == "forward":
            forward += value
            depth += aim * value
        elif key == "up":
            aim -= value
        elif key == "down":
            aim += value
    print(forward * depth)