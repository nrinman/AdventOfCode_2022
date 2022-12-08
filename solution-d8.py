# Clean and parse input data. Target: As simple data structure as possible, no further parsing/transformations needed in solver functions.
def parse(rawInput):
    cleanInput = list(map(str.strip, rawInput)) #create clean list with each line in input as elements of type string
    tree_map = []
    for row in cleanInput:
        tree_map.append(list(map(int, row))) #convert each row to list of integers
    #print(tree_map)
    return tree_map
    
# Solving part 1 and returning answer
def solvePart1(treeMap):
    #initial variables 
    visibilityCounter = 0
    lastRowIndex = len(treeMap)-1
    lastColIndex = len(treeMap[0])-1
    # solution logic
    for c in range(0, lastColIndex+1): #columns in top and bottom rows
        visibilityCounter += 2
    for r in range(1,lastRowIndex): #left and right column, excluding corners
        visibilityCounter += 2
    #print(str(visibilityCounter) + " outer trees")
    
    for r in range(1, lastRowIndex): # excluding first and last row
        for c in range(1, lastColIndex): # excluding outer columns
            current_height = treeMap[r][c]

            highest_left = max(treeMap[r][:c]) # max of all heights to the left in same row
            highest_right = max(treeMap[r][c+1:]) # max of all heighs to the right in same row
            highest_up = max([row[c] for row in treeMap[:r]]) # max of all heights in same column in above rows
            highest_down = max([row[c] for row in treeMap[r+1:]]) # max of all heights in same column in below rows
            
            if current_height > min([highest_left, highest_right, highest_up, highest_down]):
                visibilityCounter += 1
                
    # return answer
    return visibilityCounter

# Solving part 2 and returning answer
def solvePart2(treeMap):
    #initial variables
    scenicScores = []
    lastRowIndex = len(treeMap)-1
    lastColIndex = len(treeMap[0])-1
    
    # solution logic
    for r in range(1, lastRowIndex): # excluding first and last row since the score will always be 0
        for c in range(1, lastColIndex): # excluding outer columns since the score will always be 0
            left_score = 0
            right_score = 0
            up_score = 0
            down_score = 0
            current_height = treeMap[r][c]
            
            view_left = treeMap[r][:c] # all heights to the left in same row
            view_right = treeMap[r][c+1:] # all heighs to the right in same row
            view_up = [row[c] for row in treeMap[:r]] # all heights in same column in above rows
            view_down = [row[c] for row in treeMap[r+1:]] # max of all heights in same column in below rows
            
            #find scenic score contribution in each direction
            for tree in reversed(view_left):
                if tree < current_height:
                    left_score += 1
                elif tree >= current_height:
                    left_score += 1
                    break
                else:
                    None
            for tree in view_right:
                if tree < current_height:
                    right_score += 1
                elif tree >= current_height:
                    right_score += 1
                    break
                else:
                    None
            
            for tree in reversed(view_up):
                if tree < current_height:
                    up_score += 1
                elif tree >= current_height:
                    up_score += 1
                    break
                else:
                    None
                    
            for tree in view_down:
                if tree < current_height:
                    down_score += 1
                elif tree >= current_height:
                    down_score += 1
                    break
                else:
                    None
            
            scenicScores.append(left_score*right_score*up_score*down_score) #list all scenic scores
                    
       
    # store and return answer
    return max(scenicScores)

# Read and parse file with puzzle example input - update X to current day in filename
file = open("input-ex-d8.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

# Read and parse file with puzzle input  - update X to current day in filename
file = open("input-d8.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1(exampleData.copy())))
print('Part 1: ' + str(solvePart1(inputData.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy())))
print('Part 2: ' + str(solvePart2(inputData.copy())))


