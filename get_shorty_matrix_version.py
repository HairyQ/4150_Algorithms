import sys, heapq

data = []

# Run modified version of Dijkstra's algorithm on test case,
# print final output
#
# corridors = list of corridors between intersections
def get_shorty(corridors, num_intersections):
    visited = dict()
    size = dict()
    graph = []

    # Initialize dictionaries
    i = 0
    while i < num_intersections:
        size[i] = -1.0
        visited[i] = False
        i += 1
    size[0] = 1.0

    # Set up graph representation
    i = 0
    while i < num_intersections * num_intersections:
        graph.append(-1.0)
        i += 1

    for corridor in corridors:
        corridor_split = corridor.split()
        u = int(corridor_split[0])
        v = int(corridor_split[1])
        w = float(corridor_split[2])

        '''
        changed = False
        i = 0
        while i < len(graph[u]):
            vertex, weight = graph[u][i]
            if vertex == v:
                if weight > w:
                    graph[u][i] = (vertex, weight)
                    changed = True
                    break
            i += 1

        if changed:
            i = 0
            while i < len(graph[v]):
                vertex, weight = graph[v][i]
                if vertex == u:
                    if weight > w:
                        graph[v][i] = (vertex, weight)
                        break
                i += 1

        if not changed:
            graph[u].append((v, w))
            graph[v].append((u, w))
        '''

        if w > graph[u * num_intersections + v]:
            graph[u * num_intersections + v] = w
            graph[v * num_intersections + u] = w
        
    # Run Dijkstra's algorithm
    PQ = []
    heapq.heappush(PQ, (0, 1.0))

    while len(PQ) is not 0:
        u, u_weight = heapq.heappop(PQ)
        
        if visited[u]:
            continue
        visited[u] = True

        i = u * num_intersections
        while i < (u + 1) * num_intersections:
            if graph[i] == -1.0:
                i += 1
                continue

            v = i - u * num_intersections
            w = graph[i]
            if size[v] < size[u] * w:
                size[v] = size[u] * w
                heapq.heappush(PQ, (v, size[v] * -1))
            i += 1

    print('%.4f'%size[num_intersections - 1])
    
# Make sure we capture all data before printing outputs
for line in sys.stdin:
    if line == '0 0\n':
        break

    data.append(line)

# Parse input into separate test cases, implementing
# algorithm per test case as we find them
i = 0
while i < len(data):
    test_case = data[i]
    num_intersections = int(test_case.split()[0])
    num_corridors = int(test_case.split()[1])
    count = 0
    corridors = []
    while count < num_corridors:
        count += 1
        i += 1
        corridors.append(data[i])

    get_shorty(corridors, num_intersections)
    i += 1

exit()
