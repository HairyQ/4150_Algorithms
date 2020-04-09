import sys

origA = sys.stdin.readline().split()
origB = sys.stdin.readline().split()
k = int(sys.stdin.readline())

def select1(A, B, intK):
    select(A, 0, len(A) - 1, B, 0, len(B) - 1, intK)

def select(A, loA, hiA, B, loB, hiB, intK):
    if hiA < loA:
        print(intK - loA)
        print (B[intK - loA])
        return 0

    if hiB < loB:
        print(intK - loB)
        print (A[intK - loB])
        return 0

    i = int((loA + hiA) / 2)
    print("loA: " + str(loA) + " hiA: " + str(hiA) + " int i: " + str(i))
    j = int((loB + hiB) / 2)
    print("loB: " + str(loB) + " hiB: " + str(hiB) + " int j: " + str(j))

    if int(A[i]) > int(B[j]):
        if intK <= (i + j):
            return select(A, loA, i - 1, B, loB, hiB, intK)
        else:
            return select(A, loA, hiA, B, j + 1, hiB, intK)
    else:
        if intK <= (i + j):
            return select(A, loA, hiA, B, loB, j - 1, intK)
        else:
            return select(A, i + 1, hiA, B, loB, hiB, intK)

select1(origA, origB, k)
