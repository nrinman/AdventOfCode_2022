# Clean and parse input data. Target: As simple data structure as possible, no further parsing/transformations needed in solver functions.
def parse(rawInput):
    return [[r.split(" ")[0], int(r.split(" ")[1])] for r in list(map(str.strip, rawInput))] #create list of each line in input, where each line is also split into list elements for easy access
    
# Solving part 1 and returning answer
def solvePart1(moves):
    #initial variables 
    H_x = 0
    H_y = 0
    T_x = 0
    T_y = 0
    visited = {(T_x, T_y)}
    # solution logic
    for m in moves:
        direction = m[0]
        distance = m[1]
        dx = 0
        dy = 0
        match direction:
            case "U":
                dy = 1
            case "D":
                dy = -1
            case "R":
                dx = 1
            case "L":
                dx = -1
        for d in range(distance):
            H_x += dx
            H_y += dy
            if abs(H_x - T_x) > 1: #head moves too far away on row
                T_y = H_y #tail jumps to same row in case of horizontal movement too far away
                T_x = H_x-dx #tail follows head on row in case of horizontal movement too far away
                visited.add((T_x, T_y))
            elif abs(H_y - T_y) > 1: #head moves too far away on column
                T_x = H_x #tail jumps to same column in case of vertical movement too far away
                T_y = H_y-dy #tail follows head on column in case of vertical movement too far away
                visited.add((T_x, T_y))
    # store and return answer
    return len(visited)

# Solving part 2 and returning answer
def solvePart2(headMoves):
    #initial variables 
    rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    visited = {tuple(rope[-1])}
    # solution logic
    for m in headMoves:
        #print(m)
        direction = m[0]
        distance = m[1]
        dx = 0
        dy = 0
        match direction:
            case "U":
                dy = 1
            case "D":
                dy = -1
            case "R":
                dx = 1
            case "L":
                dx = -1
        for d in range(distance):
            rope[0][0] += dx
            rope[0][1] += dy
            #print("step: " + str(d+1) + " of " + str(distance))
            for i in range(1, 10):
                if abs(rope[i-1][0] - rope[i][0]) > 1 and abs(rope[i-1][1] - rope[i][1]) > 1: #both horizontal and vertical too far away. Move diagonally
                    match rope[i-1][0] - rope[i][0]:
                        case 2:
                            rope[i][0] += 1
                        case -2:
                            rope[i][0] -= 1
                    match rope[i-1][1] - rope[i][1]:
                        case 2:
                            rope[i][1] += 1
                        case -2:
                            rope[i][1] -= 1
                elif abs(rope[i-1][0] - rope[i][0]) > 1: #previous moves too far away on row
                    match rope[i-1][1] - rope[i][1]:
                        case 0:
                            None #stay on same row
                        case 1:
                            rope[i][1] += 1
                        case -1:
                            rope[i][1] -= 1
                    if rope[i-1][0] > rope[i][0]:
                        rope[i][0] += 1 #current follows previous on row in case of horizontal movement too far away
                    else:
                        rope[i][0] -= 1
                elif abs(rope[i-1][1] - rope[i][1]) > 1: #previous moves too far away on column
                    match rope[i-1][0] - rope[i][0]:
                        case 0:
                            None
                        case 1:
                            rope[i][0] += 1
                        case -1:
                            rope[i][0] -= 1
                    if rope[i-1][1] > rope[i][1]:
                        rope[i][1] += 1 #current follows previous on column in case of vertical movement too far away
                    else:
                        rope[i][1] -= 1
                else: #no movement
                    break
                if i == 9:
                    visited.add(tuple(rope[i])) #add to end of rope visited if end of rope has moved
            #debug
            #print("H: " + str(rope[0]))
            #print("1: " + str(rope[1]))
            #print("2: " + str(rope[2]))
            #print("3: " + str(rope[3]))
            #print("4: " + str(rope[4]))
            #print("5: " + str(rope[5]))
            #print("6: " + str(rope[6]))
            #print("7: " + str(rope[7]))
            #print("8: " + str(rope[8]))
            #print("T: " + str(rope[9]))
            
    # store and return answer
    return len(visited)

# Read and parse file with puzzle example input - update X to current day in filename
file = open("input-ex-d9.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

# Read and parse file with puzzle input  - update X to current day in filename
file = open("input-d9.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1(exampleData.copy())))
print('Part 1: ' + str(solvePart1(inputData.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy())))
print('Part 2: ' + str(solvePart2(inputData.copy())))


