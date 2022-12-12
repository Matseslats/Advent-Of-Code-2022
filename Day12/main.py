# PATH FINDING USING A* ALGORITHM
from collections import deque
 
class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        # H = {
        #     'A': 1,
        #     'B': 1,
        #     'C': 1,
        #     'D': 1
        # }
 
        return 1
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None

# adjac_lis = {
#     '0,0': [('B', 1), ('C', 1), ('D', 1)],
#     'B': [('D', 1)],
#     'C': [('D', 1)]
# }

# My code:

nodes = {}
f = open("input.txt")
vals = []
start = ""
end = ""
mazeWidth = 0
mazeHeight = 0
for x, l in enumerate(f.readlines()):
    cl = l.strip()
    vals.append([])
    mazeHeight += 1
    if mazeWidth == 0:
        mazeWidth = len(cl)
    for y, char in enumerate(cl):
        value = -1
        if char == 'S':
            start = f"{x}-{y}"
            value = 100
        elif char == 'E':
            end = f"{x}-{y}"
            value = 101
        else:
            value = ord(char)-ord('a')
        vals[x].append(value)

print(mazeWidth, mazeHeight)

def getVal(x: int, y: int):
    if x >= 0 and x < mazeHeight:
        if  y >= 0 and y < mazeWidth:
            # print("\rGetting:", x,y, len(vals), len(vals[x]), end="")
            return vals[x][y]
    return -1

# Generate graph
for x, line in enumerate(vals):
    for y, val in enumerate(line):
        key = f"{x}-{y}"
        val = getVal(x,y)
        conns = []

        # Get north
        valN = getVal(x,y+1)
        if valN != -1:
            if valN-1 <= val or val >= 100 or (val == 25): # One up, same height, or below, or this is start square
                conns.append((f"{x}-{y+1}", 1))
        # Get South
        valN = getVal(x,y-1)
        if valN != -1:
            if valN-1 <= val or val >= 100 or (val == 25): # One up, same height, or below, or this is start square
                conns.append((f"{x}-{y-1}", 1))
        # Get East
        valN = getVal(x+1,y)
        if valN != -1:
            if valN-1 <= val or val >= 100 or (val == 25): # One up, same height, or below, or this is start square
                conns.append((f"{x+1}-{y}", 1))
        # Get West
        valN = getVal(x-1,y)
        if valN != -1:
            if valN-1 <= val or val >= 100 or (val == 25): # One up, same height, or below, or this is start square
                conns.append((f"{x-1}-{y}", 1))
        nodes[key] = conns
        # print(key, nodes[key])

# print(vals)
print(start, end)
# print(nodes)
# print(nodes[start])
# print(nodes["1-0"])
graph1 = Graph(nodes)
path = graph1.a_star_algorithm(start, end)
if path != None:
    print(len(path)-1)
    # print("\n")
    # for no, i in enumerate(path):
    #     # print(i)
    #     i = i.split("-")
    #     # print(i)
    #     char = getVal(int(i[0]), int(i[1]))
    #     # if char < 100:
    #         # char = chr(char+97)
    #     # print(no, i[0], i[1], char)
    #     print(char,end=" ")