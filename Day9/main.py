f = open("input.txt")
visits = []
tx = ty = hx = hy = 0
visits.append((tx,ty))
for line in f.readlines():
    l = line.replace("\n", "").split(" ")
    # Do move
    for i in range(int(l[1])):
        if l[0] == "U":
            hy += 1
        if l[0] == "D":
            hy -= 1
        if l[0] == "L":
            hx -= 1
        if l[0] == "R":
            hx += 1
        # Update tail
        deltaX = hx-tx
        deltaY = hy-ty
        separation = abs(deltaX) + abs(deltaY)
        if separation > 2: # Bigger than sqrt 2, move diagonally
            if deltaX >= 1:
                tx += 1
            if deltaX <= -1:
                tx -= 1
            if deltaY >= 1:
                ty += 1
            if deltaY <= -1:
                ty -= 1
            
        else:
            if deltaX > 1:
                tx += 1
            if deltaX < -1:
                tx -= 1
            if deltaY > 1:
                ty += 1
            if deltaY < -1:
                ty -= 1

        visits.append((tx,ty))

print("No visits:", len(visits))
# print(visits)
origVisits = set(visits)
print("No unique:", len(origVisits)) # No 3,1
# print(origVisits)