import os
dirSize = 70000000
soFarBest = dirSize

def checkDelete(min: int, thisVal: int):
    # Check if this dir is amaller than the last dir to be deleted,
    # but also large enough to free up required space
    global soFarBest
    if thisVal >= min:
        if thisVal < soFarBest:
            soFarBest = thisVal
            print("New Best:", soFarBest)
        # else:
        #     print("Not better than", soFarBest)
    # else:
    #     print("Dir too small!")

def scan(mustDelete, checkBest = True):
    path = [["/", 0]]
    sum = 0
    f = open("input.txt")
    for line in f.readlines(): # Go through each line
        l = line.replace("\n", "")
        params = l.split(" ")

        if params[0] == '$': # New command incoming
            if params[1] == "ls": # Lists files
                """"""
                # print("List dir")
            elif params[1] == "cd": # Change dir
                dest = params[2]
                if dest == "/":
                    # Reset dir to home
                    path = [["/", 0]]
                elif dest == "..": # Go up one dir
                    # Check if val should be added to sum
                    val = path[-1][1]
                    if checkBest:
                        checkDelete(mustDelete, val)
                    # print("Dir size:", val)
                    if val <= 100000:
                        sum += val
                        # print("Added dir:", sum)
                    # Go up one dir
                    path.pop(-1)

                else: # Change to this dir: params[2]
                    path.append([params[2], 0])
                
                # print(path)


        elif params[0] == 'dir': # dir incoming
            """"""
            # print("Adding dir", params[1])
            # fileSys.update({thisDir: dir})
            # print(fileSys)
            # dir = {}
        else: # file incoming
            """"""
            # Get size of file
            val = int(params[0])
            # Add size to dir and all parrent dirs
            for i in range(len(path)):
                path[i][1] += val
        # print(path)
    for i in path:
        if checkBest:
            checkDelete(mustDelete, i[1])
    
    return path[0][1] # Return used storage

usedStorage = scan(dirSize, False)
freeSpace = 70000000-usedStorage
neededDeletion = 30000000-freeSpace
print("Free space:", freeSpace)
print("Needed deletion:", neededDeletion)
scan(neededDeletion, True)
print(soFarBest)
