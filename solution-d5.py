# Solving part 1
def solvePart1(moves, stacks): #moves = # of crates, from, to
    #initial variables
    topCrates = ""
    # solution logic
    #print(stacks)
    for move in moves:
        #print[move]
        noOfCrates = move[0]
        fromStack = move[1]
        toStack = move[2]
        for i in range (0, noOfCrates):
            stacks[toStack] = stacks[fromStack][:1] + stacks[toStack]
            stacks[fromStack] = stacks[fromStack][1:]
        #print(stacks)
    for s in stacks.values():
        topCrates += s[0]
    # store and return answer
    answer = topCrates
    return answer
    
# Solving part 2
def solvePart2(moves, stacks): #moves = # of crates, from, to
    #initial variables
    topCrates = ""
    # solution logic
    #print(stacks)
    for move in moves:
        #print[move]
        noOfCrates = move[0]
        fromStack = move[1]
        toStack = move[2]
        stacks[toStack] = stacks[fromStack][:noOfCrates] + stacks[toStack]
        stacks[fromStack] = stacks[fromStack][noOfCrates:]
        #print(stacks)
    for s in stacks.values():
        topCrates += s[0]
    # store and return answer
    answer = topCrates
    return answer

# read and clean input data
def parse(rawInput):
    inputList = list(map(str.strip, rawInput)) #create clean list with each line in input as elements of type string
    parsedInput = []
    while True: #remove starting stacks
        if len(inputList[0]) > 0:
            if inputList[0][0] == 'm':
                break
            else:
                del inputList[0]
        else:
            del inputList[0]
    for move in inputList: #create list of tuples with int values for the moves
        parsedInput.append(tuple(map(int, move.replace('move ','').replace(' from ',',').replace(' to ',',').split(','))))
    #print(parsedInput)
    return parsedInput

# Read and parse file with example data - update X to current day   
file = open("input-ex-d5.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)
startingStacksExample = {1: "NZ", 2: "DCM", 3: "P"}


# Read and parse file with input data - update X to current day   
file = open("input-d5.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)
startingStacks = {1: "RHMPZ", 2: "BJCP", 3: "DCLGHNS", 4: "LRSQDMTF", 5: "MZTBQPSF", 6: "GBZSFT", 7: "VRN", 8: "MCVDTLGP", 9: "LMFJNQW"} 

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1(exampleData.copy(), startingStacksExample.copy())))
print('Part 1: ' + str(solvePart1(inputData.copy(), startingStacks.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy(), startingStacksExample.copy())))
print('Part 2: ' + str(solvePart2(inputData.copy(), startingStacks.copy())))


