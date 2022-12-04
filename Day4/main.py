f = open("input.txt")
contained = 0
for line in f.readlines():
    elfs = line.replace("\n","").split(",")
    firstElf = [int(i) for i in elfs[0].split("-")]
    secondElf = [int(i) for i in elfs[1].split("-")]
    if firstElf[0] <= secondElf[0] and firstElf[1] >= secondElf[1]:
        contained += 1
    else:
        contained += firstElf[0] >= secondElf[0] and firstElf[1] <= secondElf[1]
print(contained)