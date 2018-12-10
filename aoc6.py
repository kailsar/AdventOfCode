
file = open("data6.txt", "r")
data = file.readlines()
coords = []
coord_number = 0
for line in data:
    line = line.strip("\n")
    line = line.split(", ")
    line.append(coord_number)
    coords.append(line)
    coord_number += 1

grid = []
for x in range(500):
    x_list = []
    for y in range(500):
        lowest_dist = 1000
        lowest_coord = "x"
        duplicate = False
        for coord in coords:
            x_dist = abs(x - int(coord[1]))
            y_dist = abs(y - int(coord[0]))
            dist = x_dist + y_dist
            if dist < lowest_dist:
                lowest_dist = dist
                lowest_coord = coord[2]
                duplicate = False
            elif dist == lowest_dist:
                duplicate = True
        if duplicate == True:
            x_list.append(".")
        else:
            x_list.append(lowest_coord)
    grid.append(x_list)

border_coords = []
for line in grid:
    if line[0] not in border_coords:
        border_coords.append(line[0])
    if line[len(line) - 1] not in border_coords:
        border_coords.append(line[len(line) - 1])

top_line = grid[0]
bottom_line = grid[len(grid) - 1]
for item in top_line:
    if item not in border_coords:
        border_coords.append(item)
for item in bottom_line:
    if item not in border_coords:
        border_coords.append(item)

print(border_coords)

totals = []
for coord in coords:
    totals.append(0)

for line in grid:
    for item in line:
        if item != ".":
            item = int(item)
            totals[item] += 1

for item in border_coords:
    if item != ".":
        totals[item] = 0

print(totals)

file.close()
