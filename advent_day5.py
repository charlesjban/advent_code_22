from typing import List, Any

file = open ('data_day5.txt', 'r')

lines = []
for line in file:
    lines.append(line.replace("    ","[ ]").replace('\n',"").replace("] ","]").replace('][','],[').replace('[',"").replace("]","").split(","))

crates = lines[0:8]

instructions = lines[10:]

pile1 = []
pile2 = []
pile3 = []
pile4 = []
pile5 = []
pile6 = []
pile7 = []
pile8 = []
pile9 = []

piles: List[List[Any]] = [pile1,pile2,pile3,
          pile4,pile5,pile6,
          pile7,pile8,pile9]

def extract_instruction(line):
    instruction = line[0].replace("move ","").replace(" from ",",").replace(" to ",",").split(",")
    print(instruction)
    n_boxes, from_pile, to_pile = int(instruction[0]),int(instruction[1]),int(instruction[2])
    print(n_boxes, from_pile, to_pile)
    return n_boxes, from_pile, to_pile

def move_crates_stacked(n_boxes, from_pile, to_pile):
    current_pile = piles[(from_pile-1)]
    crates = current_pile[0:n_boxes]
    print(crates)
    del current_pile[:n_boxes]
    piles[(from_pile-1)] = current_pile
    print(piles[(from_pile-1)])
    piles[(to_pile-1)] = crates + piles[(to_pile-1)]
    print(piles[(to_pile-1)])

def move_crates_ind(n_boxes, from_pile, to_pile):
    current_pile = piles[(from_pile-1)]
    crates = current_pile[0:n_boxes]
    del current_pile[:n_boxes]
    piles[(from_pile-1)] = current_pile
    for i in range(0,n_boxes):
        piles[(to_pile-1)].insert(0,crates[i])


for line in crates:
    for i in range(0,9):
        if line[i] != " ":
            piles[i].append(line[i])

for line in instructions:
    instruction = extract_instruction(line)
    move_crates_stacked(*instruction)

for stack in piles:
    print(stack[0], end ="")

file.close()
