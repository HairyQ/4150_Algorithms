import sys

def gallerize_NisK(gallery):
    total_0 = 0
    total_1 = 0
    
    for (zero, one) in gallery:
        total_0 += zero
        total_1 += one

    return max(total_0, total_1)

def gallerize(gallery, N, row, do_not_close, k, cache):
    if row >= N:
        return 0
    
    row_0, row_1 = gallery[row]
    
    if k == N - row:
        if do_not_close == -1:
            if (row + 1, 0, k - 1) not in cache:
                dont_close_0 = gallerize(gallery,
                                         N,
                                         row + 1,
                                         0,
                                         k - 1,
                                         cache)
                cache[(row + 1, 0, k - 1)] = dont_close_0
            else:
                dont_close_0 = cache[(row + 1, 0, k - 1)]

            if (row + 1, 1, k - 1) not in cache:
                dont_close_1 = gallerize(gallery,
                                         N,
                                         row + 1,
                                         1,
                                         k - 1,
                                         cache)
                cache[(row + 1, 1, k - 1)] = dont_close_1
            else:
                dont_close_1 = cache[(row + 1, 1, k - 1)]

            return max(row_0 + dont_close_0, row_1 + dont_close_1)

        elif do_not_close == 1:
            if (row + 1, 1, k - 1) not in cache:
                dont_close_1 = gallerize(gallery,
                                         N,
                                         row + 1,
                                         1,
                                         k - 1,
                                         cache)
                cache[(row + 1, 1, k - 1)] = dont_close_1
            else:
                dont_close_1 = cache[(row + 1, 1, k - 1)]
                
                return row_1 + dont_close_1

        else:
            if (row + 1, 0, k - 1) not in cache:
                dont_close_0 = gallerize(gallery,
                                         N,
                                         row + 1,
                                         0,
                                         k - 1,
                                         cache)
                cache[(row + 1, 0, k - 1)] = dont_close_0
            else:
                dont_close_0 = cache[(row + 1, 0, k - 1)]
                
                return row_0 + dont_close_0
            
    else:
        if do_not_close == 0:
            if (row + 1, 0, k - 1) not in cache:
                dont_close_0 = gallerize(gallery,
                                         N,
                                         row + 1,
                                         0,
                                         k - 1,
                                         cache)
                cache[(row + 1, 0, k - 1)] = dont_close_0
            else:
                dont_close_0 = cache[(row + 1, 0, k - 1)]

            if (row + 1, -1, k) not in cache:
                dont_close_either = gallerize(gallery,
                                              N,
                                              row + 1,
                                              -1,
                                              k,
                                              cache)
                cache[(row + 1, -1, k)] = dont_close_either
            else:
                dont_close_either = cache[(row + 1, -1, k)]
                
            return max(row_0 + dont_close_0,
                       row_0 + row_1 + dont_close_either)
            
        elif do_not_close == 1:
            if (row + 1, 1, k - 1) not in cache:
                dont_close_1 = gallerize(gallery,
                                         N,
                                         row + 1,
                                         1,
                                         k - 1,
                                         cache)
                cache[(row + 1, 1, k - 1)] = dont_close_1
            else:
                dont_close_1 = cache[(row + 1, 1, k - 1)]

            if (row + 1, -1, k) not in cache:
                dont_close_either = gallerize(gallery,
                                              N,
                                              row + 1,
                                              -1,
                                              k,
                                              cache)
                cache[(row + 1, -1, k)] = dont_close_either
            else:
                dont_close_either = cache[(row + 1, -1, k)]
                
            return max(row_1 + dont_close_1,
                       row_0 + row_1 + dont_close_either)

        elif do_not_close == -1:
            if (row + 1, 1, k - 1) not in cache:
                dont_close_1 = gallerize(gallery,
                                         N,
                                         row + 1,
                                         1,
                                         k - 1,
                                         cache)
                cache[(row + 1, 1, k - 1)] = dont_close_1
            else:
                dont_close_1 = cache[(row + 1, 1, k - 1)]

            if (row + 1, 0, k - 1) not in cache:
                dont_close_0 = gallerize(gallery,
                                         N,
                                         row + 1,
                                         0,
                                         k - 1,
                                         cache)
                cache[(row + 1, 0, k-1)] = dont_close_0
            else:
                dont_close_0 = cache[(row + 1, 0, k - 1)]

            if (row + 1, -1, k) not in cache:
                dont_close_either = gallerize(gallery,
                                              N,
                                              row + 1,
                                              -1,
                                              k,
                                              cache)
                cache[(row + 1, -1, k)] = dont_close_either
            else:
                dont_close_either = cache[(row + 1, -1, k)]
                
            return max(row_1 + dont_close_1,
                       row_0 + dont_close_0,
                       row_0 + row_1 + dont_close_either) 


problems = []

for line in sys.stdin:
    problem = []
    i = 0
    line_split = line.split()
    N = int(line_split[0])
    k = int(line_split[1])
    problem.append((N, k))

    while i < N:
        rooms = sys.stdin.readline().split()
        problem.append((int(rooms[0]), int(rooms[1])))
        i += 1

    problems.append(problem)
        
    # Read off last line: 0, 0
    sys.stdin.readline()

final_output = ''
for problem in problems:
    N, k = problem.pop(0)
    cache = dict()
    if N == k:
        final_output += str(gallerize_NisK(problem)) + '\n'
    else:
        final_output += str(gallerize(problem, N, 0, -1, k, cache)) + '\n'

print(final_output[:-1])

exit()
