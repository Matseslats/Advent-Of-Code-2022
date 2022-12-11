f = open("input.txt")
monkeys = {}

def getLine():
    line = f.readline()
    return line.strip()

mfm = 1
while True:
    try:
        monkey = int(getLine().split(" ")[1][0:1])
    except:
        break
    items = [int(x) for x in getLine().replace(",", "").split(" ")[2:]]
    operation = getLine().replace(",", "").split(" ")[3:]
    test = int(getLine().split(" ")[-1])
    monkeyTrue = int(getLine().split(" ")[-1])
    monkeyFalse = int(getLine().split(" ")[-1])
    mfm *= test
    # for i in items:
    #     mfm *= i
    
    # if operation[0] != "old":
    #     mfm *= int(operation[0])
    # if operation[2] != "old":
    #     mfm *= int(operation[2])
    # print("No:", monkey)
    # print("Items:", items)
    # print("Op:", operation)
    # print("Div by:", test)
    # print("if True:", monkeyTrue)
    # print("if False:", monkeyFalse)
    monkeys[monkey] = {
            "items": items,
            "op": operation,
            "divBy": test,
            "onTrue": monkeyTrue,
            "onFalse": monkeyFalse,
            "inspections": 0
        }
    getLine()

print(mfm)
def doOp(keys, no):
    doFromNo = doToNo = False
    if keys[0] == "old":
        doFromNo = True
    if keys[2] == "old":
        doToNo = True
    
    if keys[1] == "+":
        if doFromNo and doToNo:
            return no+no
        elif doFromNo:
            return no+int(keys[2])
        elif doToNo:
            return int(keys[0])+no
        else:
            print("ERROR ADD:", keys, no)
            exit(1)
    
    elif keys[1] == "*":
        if doFromNo and doToNo:
            return no*no
        elif doFromNo:
            return no*int(keys[2])
        elif doToNo:
            return int(keys[0])*no
        else:
            print("ERROR MULTIPLY:", keys, no)
            exit(1)

def testItem(n, divisor):
    return n % divisor == 0

def throwAround():
    for m, group in monkeys.items(): # Go through monkeys
        # print("GR", group)
        items = group["items"]
        for i in items: # Do op on every item
            group["inspections"] += 1
            keys = group["op"]
            res = doOp(keys, i)
            
            # print(res)
            canDivide = testItem(res, group["divBy"])
            # print(canDivide)
            if canDivide:
                # print("Adding %d to monkey %d" % (res, group["onTrue"]))
                monkeys[group["onTrue"]]["items"].append(res%mfm)
            else:
                # print("Adding %d to monkey %d" % (res, group["onFalse"]))
                monkeys[group["onFalse"]]["items"].append(res%mfm)
        group["items"] = []
        # print(m, group) 

for i in range(1, 10_001):
    throwAround()
    # print(monkeys)
    if i == 1 or i == 20 or i == 1000 or i % 1000 == 0:
        print("=== %d ===" % i)
        for m, g in monkeys.items():
            print("%d: %d" % (m, g["inspections"]))
        print()
        
        # barsToDraw = int(100*i/10_000)
        # print("\rProgress: |%s%s| Sim no %d" % ("#"*barsToDraw, "-"*(100-barsToDraw), int(i)), end="")
print()
mostActive = 0
secondMostActive = 0
for i, m in monkeys.items():
    insp = m["inspections"]
    if insp >= secondMostActive:
        if insp >= mostActive:
            secondMostActive, mostActive = mostActive, insp
        else:
            secondMostActive = insp

monkeyBuinsess = mostActive*secondMostActive
# print(mostActive, secondMostActive, monkeyBuinsess)
# print(monkeys)
print(monkeyBuinsess)