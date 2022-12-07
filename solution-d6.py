# Solving part 1
def solvePart1(data):
    #initial variables 
    #print(data)
    charBeforePacketMarker = 0
    # solution logic
    for i in range(0, len(data)-3):
        if len(set(data[i:i+4])) == 4:
            charBeforePacketMarker = i+4
            break
    # store and return answer
    answer = charBeforePacketMarker
    return answer

# Solving part 2
def solvePart2(data):
    #initial variables 
    #print(data)
    charBeforePacketMarker = 0
    # solution logic
    for i in range(0, len(data)-13):
        if len(set(data[i:i+14])) == 14:
            charBeforePacketMarker = i+14
            break
    # store and return answer
    answer = charBeforePacketMarker
    return answer

# read and clean input data
def parse(rawInput):
    return list(map(str.strip, rawInput))[0] #create clean list with each line in input as elements of type string

# Read and parse file with example data - update X to current day   
file = open("input-ex-d6.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

# Read and parse file with input data - update X to current day   
file = open("input-d6.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1(exampleData)))
print('Part 1: ' + str(solvePart1(inputData)))
print('Part 2 Example : ' + str(solvePart2(exampleData)))
print('Part 2: ' + str(solvePart2(inputData)))


