f = open("input.txt")
lines = f.readlines()
trees= []
for x, l in enumerate(lines): # Loop therough lines
    trees.append([])
    for y, val in enumerate(l.replace("\n", "")):
        trees[x].append(val)

def isVis(val, blockers):
    # print(val, blockers)
    s = 0
    for b in blockers:
        if val > b:
            s += 1
        else:
            s += 1
            break
    return s
    
# Go through all trees, chick if its visible
bestScore = 0
for x, line in enumerate(trees):
    for y, val in enumerate(line):
        col = [row[y] for row in trees]
        # Check left, right, top, bottom
        score = isVis(val, (line[:y])[::-1]) * \
            isVis(val, line[y+1:]) *\
            isVis(val, (col[:x])[::-1]) * \
            isVis(val, col[x+1:])
        bestScore = max(bestScore, score)
print(bestScore)