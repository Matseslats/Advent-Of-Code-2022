f = open("input.txt")
lines = f.readlines()
trees= []
for x, l in enumerate(lines): # Loop therough lines
    trees.append([])
    for y, val in enumerate(l.replace("\n", "")):
        trees[x].append(val)

def isVis(val, blockers):
    for b in blockers:
        if val <= b:
            return False
    return True
    
# Go through all trees, chick if its visible
numVisible = 0
for x, line in enumerate(trees):
    for y, val in enumerate(line):
        col = [row[y] for row in trees]
        # Check left, right, top, bottom
        if isVis(val, line[:y]) or \
            isVis(val, line[y+1:]) or\
            isVis(val, col[:x]) or \
            isVis(val, col[x+1:]):
            numVisible += 1
print(numVisible)