import sys

class BinaryTree: #Make sure you're only adding ints!!!
    def __init__(self, data):
        self.data = data #ROOT
        self.right = None
        self.left = None

    def add_item(self, item):
        if self.data:
            if item < self.data:
                if self.left is None:
                    self.left = BinaryTree(item)
                else:
                    self.left.add_item(item)

            else:
                if self.right is None:
                    self.right = BinaryTree(item)
                else:
                    self.right.add_item(item)

        else:
            self.data = item
        
    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

def makeTree(line, size):
    listLine = line.split()
    tree = BinaryTree(int(listLine[0]))
    idx = 1
    while idx < size:
        tree.add_item(int(listLine[idx]))
        idx += 1
    return tree

def sameShape(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True;

    if tree1 != None and tree2 != None:
        return sameShape(tree1.left, tree2.left) and sameShape(tree1.right, tree2.right)

    return False


uniques = set()

firstLine = sys.stdin.readline().split()

n = int(firstLine[0])
k = int(firstLine[1])
count = 1

nextLine = sys.stdin.readline()
firstTree = makeTree(nextLine, k)
uniques.add(firstTree)

if count == n:
    print(1)
    exit()

for line in sys.stdin:
    count += 1

    currTree = makeTree(line, k)
    unique = True
    for uniqueTree in uniques:
        if sameShape(currTree, uniqueTree):
            unique = False
            break

    if unique:
        uniques.add(currTree)
    
    if count >= n:
        break

print(len(uniques))
exit()
