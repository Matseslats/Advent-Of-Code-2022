f = open("input.txt")
sum = 0
cycle = 0
x = 1

def checkClock():
    global sum
    if (cycle - 20) % 40 == 0:
        sum += cycle*x

for line in f.readlines():
    l = line.replace("\n", "")
    if l == "noop":
        cycle += 1
        checkClock()
    instrs = l.split(" ")
    if instrs[0] == "addx":
        cycle += 1
        checkClock()
        cycle += 1
        checkClock()
        x += int(instrs[1])

print(sum)