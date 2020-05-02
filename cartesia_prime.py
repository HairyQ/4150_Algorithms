import sys

drone_coords = set()

line = sys.stdin.readline().split()
kirk_coords = (int(line[0]), int(line[1]))

line = sys.stdin.readline().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

minutes = int(sys.stdin.readline())
num_cubes = int(sys.stdin.readline())

for i in range(num_cubes):
    line = sys.stdin.readline().split()
    drone_coords.add((int(line[0]), int(line[1])))

print(str(drone_coords))
