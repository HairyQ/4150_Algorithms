import sys

drone_coords = set()

line = sys.stdin.readline().split()
kirk_coords = (int(line[0]), int(line[1]))

line = sys.stdin.readline().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

def generate_new_coords(coords, time):
    new_coords = set()
    x, y = coords
    new_coords.add((x + ((a * time) % b), y + ((c * time) % d)))
    new_coords.add((x + ((a * time) % b), y - ((c * time) % d)))
    new_coords.add((x - ((a * time) % b), y + ((c * time) % d)))
    new_coords.add((x - ((a * time) % b), y - ((c * time) % d)))
    return new_coords

minutes = int(sys.stdin.readline())
num_cubes = int(sys.stdin.readline())

for i in range(num_cubes):
    line = sys.stdin.readline().split()
    drone_coords.add((int(line[0]), int(line[1])))

initial_check = set()
initial_check.add((0, 0))
initial_check.add(kirk_coords)
if initial_check & drone_coords != set():
    print('You will be assimilated! Resistance is futile!')
    exit()

min_path_len = -1
i = 0
working_coords = set()
working_coords.add(kirk_coords)

while i <= minutes:
    if (0, 0) in working_coords:
        min_path_len = minutes - i
        break

    new_coords = set()
    for (x, y) in working_coords:
        new_coords = new_coords | generate_new_coords((x, y), i + 1)

    new_coords = new_coords - drone_coords
    working_coords = new_coords
        
    i += 1

if min_path_len == -1:
    print('You will be assimilated! Resistance is futile!')
else:
    print('I had ' + str(min_path_len) + ' to spare! Beam me up Scotty!')

exit()
