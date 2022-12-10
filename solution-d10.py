# Clean and parse input data. Target: As simple data structure as possible, no further parsing/transformations needed in solver functions.
def parse(rawInput):
    return [r.split(" ") for r in list(map(str.strip, rawInput))] #create list of each line in input, where each line is also split into list elements for easy access
    #return list(map(str.strip, rawInput)) #create clean list with each line in input as elements of type string
    
    
# Solving part 1 and returning answer
def solvePart1and2(instructions):
    #initial variables
    sum_signal_strenghts = 0
    current_cycle = 0
    check_cycle = 20
    current_instruction_index = 0
    current_instruction_time = 1
    X = 1
    CRT = [""]
    CRT_row = 0
    CRT_row_cycle = 40
    # solution logic
    while current_instruction_index < len(instructions): #run cycles as long as there are instructions left
        current_cycle += 1
        if current_cycle == CRT_row_cycle+1:
            CRT_row_cycle += 40
            CRT_row += 1
            CRT.append("")  
        if len(CRT[CRT_row]) >= X-1 and len(CRT[CRT_row]) <= X+1:
            draw = "#"
        else:
            draw = "."
        CRT[CRT_row] += draw
        if current_cycle == check_cycle:
            sum_signal_strenghts += X * check_cycle
            check_cycle += 40

        current_instruction = instructions[current_instruction_index][0]
        match current_instruction:
            case "noop":
                current_instruction_index += 1
            case "addx":
                if current_instruction_time == 2:
                    X += int(instructions[current_instruction_index][1])
                    current_instruction_time = 1
                    current_instruction_index += 1
                else:
                    current_instruction_time = 2
    # store and return answer
    for r in CRT:
        print(r)
    return sum_signal_strenghts

# Read and parse file with puzzle example input - update X to current day in filename
file = open("input-ex-d10.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

# Read and parse file with puzzle input  - update X to current day in filename
file = open("input-d10.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1and2(exampleData.copy())))
print('Part 1: ' + str(solvePart1and2(inputData.copy())))

