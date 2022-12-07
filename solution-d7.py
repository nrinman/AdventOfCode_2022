# Clean and parse input data. Target: As simple data structure as possible, no further parsing/transformations needed in solver functions.
def parse(rawInput):
    terminalOutput = [command.split(" ") for command in list(map(str.strip, rawInput))] #create list of each line in input, where each line is also split into list elements for easy access
    return terminalOutput
    
def getFolderSizes(terminalOutput): #used for both parts 1 and 2.
    currentPath = ""
    folderSizes = {}  # Key = Path, Value = Folder Size (including sub-folders)
    for line in terminalOutput:
        match line[0]+line[1] : #Match-Case requires python 3.10 or later
            case "$cd": # folder navigation
                target = line[2]
                if target == "/":
                    currentPath = "/"
                elif target == "..":
                    currentPath = currentPath.rsplit("/", 1)[0]
                else:
                    currentPath = currentPath + "/" + target
                #print(currentPath)
            case "$ls": #list folder content
                None
            case _: # info
                if line[0] != "dir": #ignore directories
                    addPath = currentPath
                    fileSize = int(line[0]) #files have their size first in the terminalOutput
                    while addPath != "":
                        if addPath in folderSizes.keys():
                            folderSizes[addPath] += fileSize
                        else:
                            folderSizes[addPath] = fileSize
                        addPath = addPath.rsplit("/", 1)[0]
    return folderSizes
# Solving part 1 and returning answer
def solvePart1(terminalOutput):
    #initial variables
    smallDirSizeSum = 0
    folderSizes = getFolderSizes(terminalOutput)

    # solution logic
    for value in folderSizes.values():
        if value <= 100000:
            smallDirSizeSum += value
        
    # store and return answer
    answer = smallDirSizeSum
    return answer

# Solving part 2 and returning answer
def solvePart2(terminalOutput):
    #initial variables
    folderSizes = getFolderSizes(terminalOutput)
    totalDiskSpace = 70000000
    avalableDiskSpace = totalDiskSpace - folderSizes["/"]
    requiredDiskSpace = 30000000
    neededDiskSpace = requiredDiskSpace - avalableDiskSpace
    deletionCandidate = folderSizes["/"]
    
    # solution logic
    for folderSize in folderSizes.values():
        if deletionCandidate > folderSize >= neededDiskSpace:
            deletionCandidate = folderSize  
    # store and return answer
    answer = deletionCandidate # replace 0 with variable holding solution answer
    return answer

# Read and parse file with puzzle example input - update X to current day in filename
file = open("input-ex-d7.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

# Read and parse file with puzzle input  - update X to current day in filename
file = open("input-d7.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1(exampleData.copy())))
print('Part 1: ' + str(solvePart1(inputData.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy())))
print('Part 2: ' + str(solvePart2(inputData.copy())))


