import sys

class Node:
    def __init__(self, name, toll):
        self.name = name
        self.toll = int(toll)
        self.path = self.toll
        self.next = None
        self.visited = False
        self.first = 0
        self.second = 0
        self.parents = set()

topo_list = []
def topo_sort(city_set):
    topo_count = 1

    for city in city_set.values():
        if city.visited == False:
            topo_count = explore(city_set, city, topo_count)

def explore(city_set, search_city, topo_count):
    city = city_set[search_city.name]
    if city.visited == False:
        city.visited = True
        city.first = topo_count
        topo_count += 1
        edge = city.next
            
        while edge != None:
            city_2 = city_set[edge.name]
            if city_2.visited == False:
                topo_count = explore(city_set, city_2, topo_count)

            edge = edge.next

        city.second = topo_count
        topo_list.append(city)
        topo_count += 1
        return topo_count

count = 0
city_set = dict()
num_cities = int(sys.stdin.readline())
for line in sys.stdin:
    count += 1
    split_line = line.split()
    city_node = Node(split_line[0], split_line[1])
    city_set[split_line[0]] = city_node
    if count >= num_cities:
        break

count = 0
num_highways = int(sys.stdin.readline())
if num_highways != 0:
    for line in sys.stdin:
        if num_highways == 0:
            break
        count += 1
        split_line = line.split()
        source = city_set[split_line[0]]
        dest = city_set[split_line[1]]
    
        while source.next != None:
            source = source.next

        source.next = Node(dest.name, dest.toll)
        city_set[split_line[1]].parents.add(split_line[0])
    
        if count >= num_highways:
            break

topo_sort(city_set)

count = 0
num_trips = int(sys.stdin.readline())
list_of_trips = []

def find_total(trip_list):
    for trip_split in trip_list:
        if trip_split[0] == trip_split[1]: #source = dest
            print(0)
            continue

        allowed = set()
        allowed.add(trip_split[1])
        i = 0
        while i < len(topo_list):
            if topo_list[i].name == trip_split[1]:
                break
            i += 1

        i += 1
        allowed = allowed | topo_list[i].parents
        while i < len(topo_list):
            curr_node = topo_list[i]
            if curr_node.name not in allowed:
                i += 1
                continue

            allowed = allowed | curr_node.parents
            edge = curr_node.next
            while edge != None:
                if edge not in allowed:
            
            i += 1
            
        if curr_node.name != trip_split[0]:
            print('NO')
        else:
            print(curr_node.path)
        for node_i in city_set.values():
            node_i.path = node_i.toll
    
for trip in sys.stdin:
    count += 1
    trip_split = trip.split()
    list_of_trips.append(trip_split)
    if count >= num_trips:
        break

find_total(list_of_trips)

exit()
