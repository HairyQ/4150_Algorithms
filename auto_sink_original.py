import sys

class Node:
    def __init__(self, name, toll):
        self.name = name
        self.toll = int(toll)
        self.path = self.toll
        self.next = None
        self.visited = False
        self.parents = set()

topo_list = []
def explore(city_set, search_city):
    city = city_set[search_city.name]
    if city.visited == False:
        city.visited = True
        edge = city.next
            
        while edge != None:
            city_2 = city_set[edge.name]
            if city_2.visited == False:
                explore(city_set, city_2)

            edge = edge.next

        topo_list.append(city)

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

count = 0
num_trips = int(sys.stdin.readline())
list_of_trips = []

def find_total(trip_list):
    for trip_split in trip_list:
        if trip_split[0] == trip_split[1]: #source = dest
            print(0)
            continue

        topo_list.clear()
        for city in city_set.values():
            city.visited = False
        explore(city_set, city_set[trip_split[0]])
        
        allowed = set()
        allowed.add(trip_split[1])
        i = 0
        while i < len(topo_list):
            if topo_list[i].name == trip_split[1]:
                break
            i += 1

        if i == len(topo_list):
            print('NO')
            continue
        allowed = allowed | topo_list[i].parents
        curr_node = topo_list[i] # Currently dest
        i += 1
        while i < len(topo_list):
            curr_node = topo_list[i] #Next in list
            if curr_node.name not in allowed:
                i += 1
                continue

            allowed = allowed | curr_node.parents
        
            edge = topo_list[i].next
            while edge != None:
                if edge.name not in allowed:
                    edge = edge.next
                else:
                    break
            if edge is None:
                break
            min_path = city_set[edge.name].path
            while edge != None:
                if edge.name not in allowed:
                    edge = edge.next
                    continue

                actual_city_path = city_set[edge.name].path
                if actual_city_path < min_path:
                    min_path = actual_city_path
                edge = edge.next

            if curr_node.name == trip_split[0]:
                curr_node.path = min_path
                break
            
            curr_node.path = curr_node.path + min_path
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
