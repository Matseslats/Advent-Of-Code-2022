f = open("input.txt")
visits = []
tx = ty = hx = hy = 0
ropeLen = 10
coords = []
for i in range(ropeLen):
    coords.append({"x": 0, "y": 0})
visits.append((tx,ty))
for line in f.readlines():
    l = line.replace("\n", "").split(" ")
    # Do move
    for move in range(int(l[1])):
        # Update head
        if l[0] == "U":
            coords[0]["y"] += 1
        if l[0] == "D":
            coords[0]["y"] -= 1
        if l[0] == "L":
            coords[0]["x"] -= 1
        if l[0] == "R":
            coords[0]["x"] += 1
        for i in range(ropeLen-1): # Go through all tail coords and update
            # Update tail
            deltaX = coords[i]["x"]-coords[i+1]["x"]
            deltaY = coords[i]["y"]-coords[i+1]["y"]
            separation = abs(deltaX) + abs(deltaY)
            if separation > 2: # Gap bigger than 2, move diagonally
                if deltaX >= 1:
                    coords[i+1]["x"] += 1
                if deltaX <= -1:
                    coords[i+1]["x"] -= 1
                if deltaY >= 1:
                    coords[i+1]["y"] += 1
                if deltaY <= -1:
                    coords[i+1]["y"] -= 1
                
            else: # Move one direction
                if deltaX > 1:
                    coords[i+1]["x"] += 1
                if deltaX < -1:
                    coords[i+1]["x"] -= 1
                if deltaY > 1:
                    coords[i+1]["y"] += 1
                if deltaY < -1:
                    coords[i+1]["y"] -= 1
        
        visits.append((coords[-1]["x"],coords[-1]["y"])) # Save last index's coords

print("No visits:", len(visits))
# print(visits)
origVisits = set(visits)
print("No unique:", len(origVisits)) # No 3,1
# print(origVisits)