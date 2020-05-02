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

def binary_search(lo, hi, scenario):
    if hi - lo == 1:
        if greedy_decision(launcher_distances, scenario, hi):
            return hi
        else:
            return lo
    
    mid = int((hi + lo) / 2)
    
    if greedy_decision(launcher_distances, scenario, mid):
        return binary_search(mid, hi, scenario)
    else:
        return binary_search(lo, mid, scenario)

output = ''
for scenario in scenarios:
    output += str(binary_search(1, max_dist, scenario)) + '\n'

print(output[:-1])

exit()
