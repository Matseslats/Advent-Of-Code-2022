f = open("input.txt")
contained = 0
for line in f.readlines():
    elfs = line.replace("\n","").split(",")
    firstElf = [int(i) for i in elfs[0].split("-")]
    secondElf = [int(i) for i in elfs[1].split("-")]
    contained += firstElf[0] in range(secondElf[0], secondElf[1]+1) \
        or firstElf[1] in range(secondElf[0], secondElf[1]+1) \
        or secondElf[0] in range(firstElf[0], firstElf[1]+1) \
        or secondElf[1] in range(firstElf[0], firstElf[1]+1)
print(contained)