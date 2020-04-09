import sys, random, string, time

n_arr = [63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]
k_arr = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]

def randomString(size):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))

def algorithm(n, k):
    count = 0

    accepted = set()
    rejected = set()
    
    for i in range(n):
        line = randomString(size)
        
        count += 1
        joined = ''.join(sorted(line.rstrip()))
        
        if joined in accepted:
            accepted.remove(joined)
            rejected.add(joined)

        elif joined not in rejected:
            accepted.add(joined)

        if count > n:
            break

def time_constK(k):
    for n in n_arr:
        finalTime = 0
        for i in range(999):
            tic = time.process_time()
            algorithm(n, k)
            toc = time.process_time()
            
            elapsed = toc - tic
            
            tic2 = time.process_time()
            for i in range(n):
                randomString(k)
            toc2 = time.process_time()
                
            elapsed2 = toc2 - tic2
            finalTime = finalTime + (elapsed - elapsed2) * 1000

        finalTime = finalTime / 1000

        print("Total time for " + str(n) + ": " + str(elapsed) + " overhead: " + str(elapsed2) + "\n Total - overhead: " + str(finalTime) + " ms\n")
        
def time_constN(n):
    for k in k_arr:
        finalTime = 0

        for i in range(999):
            tic = time.process_time()
            algorithm(n, k)
            toc = time.process_time()

            elapsed = toc - tic
            
            finalTime = finalTime + elapsed * 1000

        finalTime = finalTime / 1000

        print("Total time for word size " + str(k) + ": " + str(finalTime) + " ms\n")
        
line1 = sys.stdin.readline()
firstline = line1.split()

numWords = int(firstline[0])
size = int(firstline[1])
is_constN = int(firstline[2])

if (is_constN == 1):
    time_constN(numWords)
elif (is_constN == 0):
    time_constK(size)

#print(len(accepted))
sys.exit()
