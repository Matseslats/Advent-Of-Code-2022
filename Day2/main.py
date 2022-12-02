file = open("input.txt")
lookup = {
    'A': "ROCK",
    'B': "PAPER",
    'C': "SCISSORS",
    'X': "ROCK",
    'Y': "PAPER",
    'Z': "SCISSORS"
}

totScore = 0
for line in file:
    lineNoNL = line.split('\n')
    vals = lineNoNL[0].split(" ")
    
    scoreFromSel = 0
    if vals[1] == 'Y':
        scoreFromSel = 2 # Paper
    elif vals[1] == 'X':
        scoreFromSel = 1 # Rock
    else:
        scoreFromSel = 3 # Si
    
    scoreFromOutcome = 0
    if lookup[vals[0]] == "ROCK" and lookup[vals[1]] == "PAPER": # Rock and you: sc
        scoreFromOutcome = 6
    elif lookup[vals[0]] == "PAPER" and lookup[vals[1]] == "SCISSORS": # Paper and you: rock
        scoreFromOutcome = 6
    elif lookup[vals[0]] == "SCISSORS" and lookup[vals[1]] == "ROCK":
        scoreFromOutcome = 6
    elif lookup[vals[0]] == lookup[vals[1]]:
        scoreFromOutcome = 3
    
    totScore += scoreFromOutcome + scoreFromSel

print(totScore)
