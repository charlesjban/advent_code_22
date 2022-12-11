# open file
file = open("data_day4.txt", "r")

# pass the string of numbers and return them as 'lower' and 'upper' integers
def range(number_section):
    lower = int(number_section.split("-")[0])
    upper = int(number_section.split("-")[1])
    return lower,upper

# check for full overlaps (part 1)
# pass 2 sets of tuples (elf 1 upper and lower, elf2 upper and lower)
# and return 1 for an overlap and 0 for no overlap
def check_full_overlaps(elf1, elf2):
    # check if elf1 contained within elf2
    if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]
    or elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
        return 1
    else:
        return 0

# check for partial overlaps (part 2)
# pass 2 sets of tuples (elf 1 upper and lower, elf2 upper and lower)
# and return 1 for an overlap and 0 for no overlap
def check_part_overlaps(elf1,elf2):
    if (elf1[0] >= elf2[0] and elf1[0] <= elf2[1]
    or elf2[0] >= elf1[0] and elf2[0] <= elf1[1]):
        return 1
    else:
        return 0



def part1_part2():
    full_overlap_counter = 0
    part_overlap_counter = 0
    for line in file:
        # separate text from row into each elf, separating by ','
        elf1 = range(line.split(",")[0])
        elf2 = range(line.split(",")[1])

        # add the returned score from overlap checkers to counters
        full_overlap_counter += check_full_overlaps(elf1, elf2)
        part_overlap_counter += check_part_overlaps(elf1, elf2)

    print("There are %s full overlaps"%full_overlap_counter)
    print("There are %s partial overlaps" % part_overlap_counter)



part1_part2()









file.close()