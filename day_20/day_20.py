import time
import copy
from numpy import sum
input_file = open('test.txt', 'r')
data = input_file.read()
rows = data.split('\n')
print(data)

class Conway:

    def __init__(self):
        self.cells = {}
        self.temp = copy.copy(self.cells)
        rows = 3
        cols = 3
        layers = 3
        zmin = -1
        zmax = 1
        rmin = 0
        rmax = 2
        cmin = 0
        cmax = 2

    def exists(self, key):
        if key in self.cells.keys():
            return True


    def add_cell(self, r, c, z, occ):
        key = self.create_key(r, c, z)
        if self.exists(key):
            print(self.cells[key])
        else:
            self.cells[key] = 0

    def create_key(self, r, c, z):
        return str(r) + ',' + str(c) + ',' + str(z)

    def print_world(self):
        for 

game = Conway()
for i in range(len(rows)):
    for j in range(len(rows[i])):
        game.add_cell(i, j, 0, 0)