import sys

line = sys.stdin.readline().split()
r = int(line[0])
c = int(line[1])

grid = []
count = 0

for line in sys.stdin:
    grid.insert(0, list(map(int, line.split())))
    count += 1
    if count == r:
        break

best_cache = grid[0]
    
i = 1
while i < r:
    new_cache = []
    diag_l = best_cache[c - 1] - grid[i][0]
    diag_r = best_cache[1] - grid[i][0]
    down   = best_cache[0] + grid[i][0]

    new_cache.append(max(diag_l, diag_r, down))

    j = 1

    while j < c - 1:
        diag_l = best_cache[j - 1] - grid[i][j]
        diag_r = best_cache[j + 1] - grid[i][j]
        down   = best_cache[j] + grid[i][j]
      
        new_cache.append(max(diag_l, diag_r, down))

        j += 1

    diag_l = best_cache[c - 2] - grid[i][c - 1]
    diag_r = best_cache[0] - grid[i][c - 1]
    down   = best_cache[c - 1] + grid[i][c - 1]

    new_cache.append(max(diag_l, diag_r, down))
    best_cache = new_cache
    
    i += 1

print(max(best_cache))
exit()
