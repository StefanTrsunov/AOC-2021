with open("day4_input") as f:
    chosen_ones = [int(x) for x in f.readline().strip('\n').split(',')]
    grids = []
    while f.readline():
        grid = []
        for i in range(5):
            grid.extend([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
        grids.append(grid)
def check_winner(grid):
    #horizontal
    start = 0
    for i in range(5):
        if grid[start] + grid[start+1] + grid[start+2] + grid[start+3] + grid[start+4] == -5:
            return True
        start += 5
    #vertical
    start = 0
    for i in range(5):
        if grid[start] + grid[start + 5] + grid[start + 10] + grid[start + 15] + grid[start + 20] == -5:
            return True
        start += 1

found = False
while found == False:
    number = chosen_ones[0]
    chosen_ones = chosen_ones[1:]
    for grid in grids:
        for i in range(len(grid)):
            if grid[i] == number:
                grid[i] = -1
    for grid in grids:
        if check_winner(grid):
            total = sum([x for x in grid if x != -1])
            print(total * number)
            found = True