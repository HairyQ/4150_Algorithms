import sys

accepted = set()
rejected = set()
count = 0

line1 = sys.stdin.readline()
firstline = line1.split()

numWords = int(firstline[0])
size = int(firstline[1])

for line in sys.stdin:
    count += 1
    joined = ''.join(sorted(line.rstrip()))

    if joined in accepted:
        accepted.remove(joined)
        rejected.add(joined)

    elif joined not in rejected:
        accepted.add(joined)

    if count >= numWords:
        break
        


print(len(accepted))
sys.exit()
