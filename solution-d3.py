# function for parsing raw puzzle input
def parse(rawInput):
    cleanInput = list(map(str.strip, rawInput))
    data = cleanInput
    #data = list(map(int, data))
    #
    #for row in data:
    #    for i in range(0, 2):
    #        row[i] = tuple(map(int, row[i].split(',')))
    #print(data)
    return data
    

# function for solving part 1
def solvePart1(data):
    #initial variables
    prioritySum = 0
    commonTypes = []
    priorityList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    
    # solution logic
    for rucksack in data:
        compIndex = int(len(rucksack)/2)
        comp1Types = set(rucksack[:compIndex])
        comp2Types = set(rucksack[compIndex:])
        commonType = comp1Types.intersection(comp2Types)
        commonTypes.append(str(commonType))
    priority = 1
    for type in priorityList:
        for commonType in commonTypes:
            if type in commonType:
                prioritySum += priority
        priority += 1
        
    # store and return answer
    answer = prioritySum
    return answer

def solvePart2(data):
    #initial variables
    prioritySum = 0
    commonTypes = []
    priorityList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # solution logic
    for i in range(0, len(data), 3):
        r1 = set(data[i])
        r2 = set(data[i+1])
        r3 = set(data[i+2])
        commonType = r1.intersection(r2).intersection(r3)
        commonTypes.append(commonType)
        
    priority = 1
    for type in priorityList:
        for commonType in commonTypes:
            if type in commonType:
                prioritySum += priority
        priority += 1
       
    # store and return answer
    answer = prioritySum
    return answer
    
file = open("input-ex-d3.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

file = open("input-d3.txt", "r")
rawInput = file.readlines()
file.close()
data = parse(rawInput)
print('Part 1 Example : ' + str(solvePart1(exampleData.copy())))
print('Part 1: ' + str(solvePart1(data.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy())))
print('Part 2: ' + str(solvePart2(data.copy())))


