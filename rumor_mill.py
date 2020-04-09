import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.friends = set()
        self.dist = -1


student_set = dict()
dist_dict = dict()

def bfs(student, dist_dict):
    student_set[student].dist = 0

    Q = []
    Q.append(student)
    dist_dict[0] = set([student])

    while len(Q) is not 0:
        curr_student = Q.pop(0)
        for friend in student_set[curr_student].friends:
            if student_set[friend].dist is -1:
                Q.append(friend)
                curr_dist = student_set[curr_student].dist + 1
                student_set[friend].dist = curr_dist
                if curr_dist not in dist_dict:
                    dist_dict[curr_dist] = set()
                dist_dict[curr_dist].add(friend)

def print_rumor_list(student, dist_dict):
    bfs(student, dist_dict)
    i = 0
    final_string = ''
    while True:
        if i not in dist_dict:
            break
        for student in sorted(dist_dict[i]):
            final_string = final_string + student + ' '
        i += 1

    not_connected = set()
    for student in student_set.keys():
        if student_set[student].dist is -1:
            not_connected.add(student)

    for student in sorted(not_connected):
        final_string = final_string + student + ' '

    print(final_string[:-1])
                
count = 0
num_students = int(sys.stdin.readline())
for line in sys.stdin:
    count += 1
    line = line.rstrip()
    student_set[line] = Node(line)
    if count >= num_students:
        break

count = 0
num_friend_pairs = int(sys.stdin.readline())
if num_friend_pairs is not 0:
    for line in sys.stdin:
        count += 1
        line_split = line.split()
        student_set[line_split[0]].friends.add(line_split[1])
        student_set[line_split[1]].friends.add(line_split[0])
        if count >= num_friend_pairs:
            break

count = 0
num_rumorers = int(sys.stdin.readline())
rumorer_list = []
for line in sys.stdin:
    count += 1
    rumorer_list.append(line.rstrip())
    if count >= num_rumorers:
        break

count = 0
for rumorer in rumorer_list:
    count += 1
    print_rumor_list(rumorer, dist_dict)
    if count >= num_rumorers:
        break
    
    dist_dict = dict()
    for student in student_set.keys():
        student_set[student].dist = -1

exit()
