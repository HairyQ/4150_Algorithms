import sys

launcher_distances = []
scenarios = []
max_dist = 0

line = sys.stdin.readline().split()
n = int(line[0])
k = int(line[1])

i = 1
while i < n:
    distance = int(sys.stdin.readline())
    launcher_distances.append(distance)
    max_dist += distance
    i += 1

i = 0
while i < k:
    scenarios.append(int(sys.stdin.readline()))
    i += 1

def greedy_decision(dist_list, num_shells, d):
    running_sum = 0
    num_lengths = 0

    for dist in dist_list:
        running_sum += dist

        if running_sum >= d:
            running_sum = 0
            num_lengths += 1

    if num_lengths + 1 >= num_shells:
        return True
    return False

output_list = []
for scenario in scenarios:
    

print(greedy_decision(launcher_distances, scenarios[0], 2))
