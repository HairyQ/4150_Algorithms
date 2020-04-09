import sys

N = int(sys.stdin.readline())
distance_vec = []
penalty_dict = dict()
penalty_dict[N] = 0

i = 0
while i <= N:
    line = sys.stdin.readline()
    distance_vec.append(int(line))
    i += 1

def penalty_iterative(dist_vec, pen_dict):
    idx = N - 1

    while idx >= 0:
        i = N
        start_dist = dist_vec[i] - dist_vec[idx]
        min_penalty = (400 - start_dist)
        min_penalty *= min_penalty

        while i > idx:
            penalty_i = pen_dict[i]
            dist_to_i = dist_vec[i] - dist_vec[idx]
            penalty_to_i = (400 - dist_to_i) * (400 - dist_to_i) + penalty_i
        
            if penalty_to_i < min_penalty:
                min_penalty = penalty_to_i
            i -= 1

        pen_dict[idx] = min_penalty
        idx -= 1

    return min_penalty

print(penalty_iterative(distance_vec, penalty_dict))
    
exit()
