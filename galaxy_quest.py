import sys

line1 = sys.stdin.readline().split()
d = int(line1[0])
d_squared = d*d
star_count = int(line1[1])
count = 0
stars = []

for line in sys.stdin:
    count += 1
    
    currLine = line.split()
    stars.append(int(currLine[0]))
    stars.append(int(currLine[1]))

    if count >= star_count:
        break

def findMajority(A):
    if len(A) is 0:
        return -1, -1
    elif len(A) is 2:
        return A[0], A[1]
    else:
        A_prime = []
        i = 0
        j = 0
        y_x = -1
        y_y = -1
        while i < (len(A) - 2):
            j = i
            x_0 = A[i]
            y_0 = A[i+1]
            x_1 = A[i+2]
            y_1 = A[i+3]

            if (x_0 - x_1) * (x_0 - x_1) + (y_0 - y_1) * (y_0 - y_1) <= d_squared:
                A_prime.append(x_0)
                A_prime.append(y_0)

            i += 4

        if (j + 4 < len(A)): # Odd num of elements
            y_x = A[j + 4]
            y_y = A[j + 5]

        x_x, x_y = findMajority(A_prime)

        if x_x is -1:
            if y_x is not -1:
                y_count = count_occurrences(A, y_x, y_y, d_squared)
                half = int(len(A) / 4)
                
                if y_count > half:
                    return y_x, y_y
                else:
                    return -1, -1

            else:
                return -1, -1

        else:
            x_count = count_occurrences(A, x_x, x_y, d_squared)
            half = int(len(A) / 4)

            if x_count > half:
                return x_x, x_y
            else:
                return -1, -1


def count_occurrences(A_list, star_x, star_y, d_sq):
    i = 0
    curr_count = 0
    while i < len(A_list):
        x_0 = A_list[i]
        y_0 = A_list[i+1]

        if (star_x - x_0) * (star_x - x_0) + (star_y - y_0) * (star_y - y_0) <= d_sq:
            curr_count += 1

        i += 2

    return curr_count

fin_x, fin_y = findMajority(stars)
if fin_x is -1:
    print('NO')
else:
    size = count_occurrences(stars, fin_x, fin_y, d_squared)
    print(size)

exit()
