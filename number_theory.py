import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def exp(x, y, N):
    z = 1
    for b in bin(y)[2:]:
        if b == '1':
            z = (x*z*z) % N
        else:
            z = (z*z) % N

    return z

def fermat_primality(N):
    a_list = [2, 3, 5]

    for a in a_list:
        if exp(a, N-1, N) != 1:
            return 'no'
    return 'yes'

def ee(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        (x_prime, y_prime, d) = ee(b, a % b)
        return (y_prime, x_prime - (a//b)*y_prime, d)

def ee_inverse(a, N):
    (x, y, d) = ee(a, N)
    if d == 1:
        return x % N
    else:
        return -1

def inverse(a, N, alt):
    mod = N % a
    mult = int((N - mod) / a)
    if mod == 0:
        return 0
    elif mod == 1:
        if alt:
            return mult * -1
        else:
            return mult
    else:
        next = inverse(mod, a, not alt)
        if next == 0:
            return 0
        elif next < 0:
            return int((N*next - 1)/a)
        else:
            return int((N*next + 1)/a)

def inverse_finder(x, y):
    inv = 0
    if x == 0 or y == 0:
        return -1
    elif x == 1:
        return 1
    
    if x > y:
        if x % y == 1:
            return 1
        inv = inverse(x % y, y, True)
    else:
        inv = inverse(x, y, True)
        
    if inv == 0:
        return -1
    elif inv < 0:
        return y + inv
    else:
        return inv

def key(p, q):
    phi = (p-1)*(q-1)
    e = 3
    for e in range(3, phi, 2):
        if gcd(e, phi) == 1:
            break
    d = ee_inverse(e, phi)
    #if d < 0:
        #d = phi - d
    return (p*q, e, d)
        
input = []

for line in sys.stdin:
    input.append(line)

for line in input:
    line_split = line.split()
    op = line_split[0]
    if op == 'gcd':
        print(gcd(int(line_split[1]), int(line_split[2])))
    elif op == 'exp':
        print(exp(int(line_split[1]), int(line_split[2]), int(line_split[3])))
    elif op == 'inverse':
        inv = ee_inverse(int(line_split[1]), int(line_split[2]))
        if inv == -1:
            print('none')
        else:
            print(inv)
    elif op == 'isprime':
        print(fermat_primality(int(line_split[1])))
    else:
        mod, e, d = key(int(line_split[1]), int(line_split[2]))
        print(str(mod) + ' ' + str(e) + ' ' + str(d))
    
exit()
