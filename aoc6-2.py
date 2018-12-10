
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
total_under = 0
for x in range(500):
    x_list = []
    for y in range(500):
        total_dists = 0
        for coord in coords:
            x_dist = abs(x - int(coord[1]))
            y_dist = abs(y - int(coord[0]))
            dist = x_dist + y_dist
            total_dists += dist
        if total_dists < 10000:
            total_under += 1

print(total_under)
file.close()
