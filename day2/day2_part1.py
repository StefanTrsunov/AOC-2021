with open('day2_input') as f:
    data = f.readlines()
    forward = 0
    depth = 0
    for line in data:
        key, value = line.split()
        value = int(value)
        if key == "forward":
            forward += value
        elif key == "up":
            depth -= value
        elif key == "down":
            depth += value
    print(forward * depth)
