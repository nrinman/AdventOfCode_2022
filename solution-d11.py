# Clean and parse input data. Target: As simple data structure as possible, no further parsing/transformations needed in solver functions.
import math

def parse(rawInput):
    cleanInput = list(map(str.strip, rawInput)) #create clean list with each line in input as elements of type string
    monkeys = []
    monkey_index = -1
    for row in cleanInput:
        r = row.replace(":", "").replace(",", "").split(" ")
        #print(r)
        match r[0]:
            case "Monkey":
                monkeys.append({"monkey": int(r[1])})
                monkey_index += 1
                monkeys[monkey_index].update({"inspections": 0})
            case "Starting":
                monkeys[monkey_index].update({"starting_items": list(map(int, r[2:]))})
            case "Operation":
                monkeys[monkey_index].update({"operation": (r[-2], r[-1])})
            case "Test":
                monkeys[monkey_index].update({"test_divisible": int(r[-1])})
            case "If":
                if r[1] == "true":
                    monkeys[monkey_index].update({"true_throw": int(r[-1])})
                else:
                    monkeys[monkey_index].update({"false_throw": int(r[-1])})
            case _: #empty line
                None
    return monkeys
    
    
# Solving part 1 and returning answer
def solvePart1(monkeys):
    #initial variables 
    rounds = 20
    monkey_business = 0
    total_inspections = []
    # solution logic
    for i in range(rounds):
        for monkey in monkeys:
            while len(monkey["starting_items"]) > 0:
                monkey["inspections"] += 1
                inspected_item = monkey["starting_items"].pop(0)
                operation_size = inspected_item if monkey["operation"][1] == "old" else int(monkey["operation"][1])
                match monkey["operation"][0]:
                    case "+":
                        inspected_item += operation_size
                    case "*":
                        inspected_item *= operation_size
                    case _:
                        print("Unknown operation")
                inspected_item = int(inspected_item/3)
                if inspected_item % monkey["test_divisible"] == 0:
                    monkeys[monkey["true_throw"]]["starting_items"].append(inspected_item)
                else:
                    monkeys[monkey["false_throw"]]["starting_items"].append(inspected_item)
    for monkey in monkeys:
        total_inspections.append(monkey["inspections"])
    total_inspections.sort()
    monkey_business = total_inspections[-1] * total_inspections[-2]
        
    # store and return answer
    return monkey_business


# Solving part 2 and returning answer

# !!!! Some bug is causing part 2 to return incorrect answer
# !!!! Work around by commenting out part 1 on rows 120 & 121
def solvePart2(monkeys_p2):
    #initial variables 
    rounds = 10000
    monkey_business = 0
    total_inspections_p2 = []
    worry_reduce_factor = 1
    for monkey in monkeys_p2:
        worry_reduce_factor *= monkey["test_divisible"]

    # solution logic
    for i in range(rounds):
        for monkey in monkeys_p2:
            while len(monkey["starting_items"]) > 0:
                monkey["inspections"] += 1
                inspected_item = monkey["starting_items"].pop(0)
                operation_size = inspected_item if monkey["operation"][1] == "old" else int(monkey["operation"][1])
                match monkey["operation"][0]:
                    case "+":
                        inspected_item += operation_size
                    case "*":
                        inspected_item *= operation_size
                    case _:
                        print("Unknown operation")
                inspected_item = inspected_item % worry_reduce_factor
                #print(inspected_item)
                if inspected_item % monkey["test_divisible"] == 0:
                    monkeys_p2[monkey["true_throw"]]["starting_items"].append(inspected_item)
                else:
                    monkeys_p2[monkey["false_throw"]]["starting_items"].append(inspected_item)
    for monkey in monkeys_p2:
        total_inspections_p2.append(monkey["inspections"])
    total_inspections_p2.sort()
    monkey_business = total_inspections_p2[-1] * total_inspections_p2[-2]
        
    # store and return answer
    return monkey_business

# Read and parse file with puzzle example input - update X to current day in filename
file = open("input-ex-d11.txt", "r")
rawExampleInput = file.readlines()
file.close()
exampleData = parse(rawExampleInput)

# Read and parse file with puzzle input  - update X to current day in filename
file = open("input-d11.txt", "r")
rawInput = file.readlines()
file.close()
inputData = parse(rawInput)

# Call problem solver functions for part 1 & 2 with example and input data, print returned answers   
print('Part 1 Example : ' + str(solvePart1(exampleData.copy())))
print('Part 1: ' + str(solvePart1(inputData.copy())))
print('Part 2 Example : ' + str(solvePart2(exampleData.copy())))
print('Part 2: ' + str(solvePart2(inputData.copy())))


