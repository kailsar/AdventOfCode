
file = open("data8.txt", "r")
data = file.read().split(" ")
for x in range(len(data)):
    data[x] = int(data[x])

counter = 0

class node:

    def __init__(self):
        global counter
        self.number_of_children = data[counter]
        self.length_of_metadata = data[counter + 1]
        self.children = []
        self.metadata = []
        self.value = 0
        counter += 2
        for x in range(self.number_of_children):
            self.children.append(node())
        for x in range(self.length_of_metadata):
            self.metadata.append(data[counter])
            counter += 1
        self.calculate_value()
                
    def calculate_value(self):
        if self.children == []:
            self.value = sum(self.metadata)
        else:
            for x in self.metadata:
                if  x <= len(self.children):
                    self.value += self.children[x - 1].value

root_node = node()
print(root_node.value)
