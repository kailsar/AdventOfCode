import time

input = open("data5-2.txt", "r")
polymer = input.read()
length = len(polymer)
repeat = 1
reactions = 0
results = {}

def check_reaction(a,b):
    if (a != b and a.lower() == b.lower()):
        # print (a + "---" + b)
        return True
    else:
        return False

def iterate_polymer(data):
    x = 0
    reactions = 0
    while x < len(data) - 1:
        reacts = check_reaction(data[x], data[x+1])
        if reacts:
            data = data[:x] + data[(x+2):]
            reactions += 1
        
        else:
            x += 1
    if reactions == 0:
        global repeat
        repeat = 0
    return data

def remove_unit(data, unit):
    x = 0
    while x < len(data):
        if data[x].lower() == unit:
            data = data[:x] + data[(x+1):]
        else:
            x += 1
    return data

for letter in range(97,123):
    unit = chr(letter)
    repeat = 1
    test_data = remove_unit(polymer, unit)
    while repeat == 1:
        test_data = iterate_polymer(test_data)
    results[unit] = len(test_data.strip())

print(results)

