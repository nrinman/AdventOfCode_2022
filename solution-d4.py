# Solving part 1
def solvePart1(data):
    #initial variables 
    counter = 0
    # solution logic
    for pair in data:
        if (pair[0] >= pair[2] and pair[1] <= pair[3]) or (pair[2] >= pair[0] and pair[3] <= pair[1]):
            counter += 1
    # store and return answer
    answer = counter # replace 0 with variable holding solution answer
    return answer

# Solving part 2
def solvePart2(data):
    #initial variables 
    counter = 0
    # solution logic
    for pair in data:
        if (pair[0] >= pair[2] and pair[0] <= pair[3]) or (pair[1] >= pair[2] and pair[1] <= pair[3]):
            counter += 1
        elif (pair[2] >= pair[0] and pair[2] <= pair[1]) or (pair[3] >= pair[0] and pair[3] <= pair[1]):
            counter += 1
    # store and return answer
    answer = counter # replace 0 with variable holding solution answer
    return answer

# read and clean input data
def parse(rawInput):
    inputList = list(map(str.strip, rawInput)) #create clean list with each line in input as elements of type string
    parsedInput = []
    for pair in inputList:
        parsedInput.append(tuple(map(int, pair.replace('-',',').split(','))))
    #print(parsedInput)
    return parsedInput

# Read and parse file with example data - update X to current day   
file = open("input-ex-d4.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

# Read and parse file with input data - update X to current day   
file = open("input-d4.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1(exampleData.copy())))
print('Part 1: ' + str(solvePart1(inputData.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy())))
print('Part 2: ' + str(solvePart2(inputData.copy())))


