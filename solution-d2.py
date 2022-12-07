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
    shapeScores = 0
    roundScores = 0
    
    # solution logic
    for round in data:
        if round[-1] == 'X':
            shapeScores += 1
        elif round[-1] == 'Y':
            shapeScores += 2
        else:
            shapeScores += 3
        if (round[0] == 'A' and round[-1] == 'X') or (round[0] == 'B' and round[-1] == 'Y') or (round[0] == 'C' and round[-1] == 'Z'):
            roundScores += 3
        elif round[0] == 'A' and round[-1] == 'Y':
            roundScores += 6
        elif round[0] == 'B' and round[-1] == 'Z':
            roundScores += 6
        elif round[0] == 'C' and round[-1] == 'X':
            roundScores += 6
        else:
            roundScores += 0

    # store and return answer
    answer = shapeScores + roundScores
    return answer

def solvePart2(data):
    #initial variables
    shapeScores = 0
    roundScores = 0
    # solution logic
    for round in data:
        if round[-1] == 'X':
            roundScores += 0
            if round[0] == 'A':
                shapeScores += 3
            elif round[0] == 'B':
                shapeScores += 1
            else:
                shapeScores += 2
        elif round[-1] == 'Y':
            roundScores += 3
            if round[0] == 'A':
                shapeScores += 1
            elif round[0] == 'B':
                shapeScores += 2
            else:
                shapeScores += 3
        else:
            roundScores += 6
            if round[0] == 'A':
                shapeScores += 2
            elif round[0] == 'B':
                shapeScores += 3
            else:
                shapeScores += 1
       
    # store and return answer
    answer = shapeScores + roundScores
    return answer
    
file = open("input-ex-d2.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

file = open("input-d2.txt", "r")
rawInput = file.readlines()
file.close()
data = parse(rawInput)
print('Part 1 Example : ' + str(solvePart1(exampleData.copy())))
print('Part 1: ' + str(solvePart1(data.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy())))
print('Part 2: ' + str(solvePart2(data.copy())))


