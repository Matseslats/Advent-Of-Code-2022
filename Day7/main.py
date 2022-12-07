import os
f = open("input.txt")
path = [["/", 0]]
sum = 0

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

print(sum)
