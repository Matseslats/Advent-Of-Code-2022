file = open("input.txt")
lookup = {
    'A': "ROCK",
    'B': "PAPER",
    'C': "SCISSORS",
    'X': "LOSE",
    'Y': "DRAW",
    'Z': "WIN"
}
beats = {
    "ROCK": "B",
    "PAPER": "C",
    "SCISSORS": "A"
}
draws = {
    "ROCK": "A",
    "PAPER": "B",
    "SCISSORS": "C"
}

totScore = 0
for line in file:
    lineNoNL = line.split('\n')
    vals = lineNoNL[0].split(" ")
    
    scoreFromOutcome = 0
    if lookup[vals[1]] == "WIN":
        choose = beats[lookup[vals[0]]]
        scoreFromOutcome = 6
        # print("WIN")
    elif lookup[vals[1]] == "DRAW":
        choose = draws[lookup[vals[0]]]
        scoreFromOutcome = 3
        # print("DRAW")
    else: # Lose game
        # print("LOSE")
        scoreFromOutcome = 0
        if lookup[vals[0]] == "ROCK": # Rock and you: sc
            choose = 'C'
        elif lookup[vals[0]] == "PAPER": # Paper and you: rock
            choose = 'A'
        elif lookup[vals[0]] == "SCISSORS":
            choose = 'B'

    # print(choose)
    scoreFromSel = 0
    if choose == 'B':
        scoreFromSel = 2 # Paper
    elif choose == 'A':
        scoreFromSel = 1 # Rock
    else:
        scoreFromSel = 3 # Si
    # print(scoreFromOutcome, scoreFromSel)
    totScore += scoreFromOutcome + scoreFromSel

print(totScore)
