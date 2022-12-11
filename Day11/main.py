f = open("input.txt")
monkeys = {}

def getLine():
    line = f.readline()
    return line.strip()

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
            "inspections": 0,
        }
    getLine()

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
            res = doOp(group["op"], i)//3
            # print(res)
            canDivide = testItem(res, group["divBy"])
            # print(canDivide)
            if canDivide:
                # print("Adding %d to monkey %d" % (res, group["onTrue"]))
                monkeys[group["onTrue"]]["items"].append(res)
            else:
                # print("Adding %d to monkey %d" % (res, group["onFalse"]))
                monkeys[group["onFalse"]]["items"].append(res)
        group["items"] = []
        # print(m, group) 

for i in range(20):
    throwAround()

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