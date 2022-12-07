# Clean and parse input data. Target: As simple data structure as possible, no further parsing/transformations needed in solver functions.
def parse(rawInput):
    return list(map(str.strip, rawInput)) #create clean list with each line in input as elements of type string
    
# Solving part 1 and returning answer
def solvePart1(data):
    #initial variables 
    
    # solution logic
        
    # store and return answer
    answer = 0 # replace 0 with variable holding solution answer
    return answer

# Solving part 2 and returning answer
def solvePart2(data):
    #initial variables

    # solution logic
       
    # store and return answer
    answer = 0 # replace 0 with variable holding solution answer
    return answer

# Read and parse file with puzzle example input - update X to current day in filename
file = open("input-ex-dX.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

# Read and parse file with puzzle input  - update X to current day in filename
file = open("input-dX.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1(exampleData.copy())))
print('Part 1: ' + str(solvePart1(inputData.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy())))
print('Part 2: ' + str(solvePart2(inputData.copy())))


