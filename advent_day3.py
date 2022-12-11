
import string
from itertools import islice

def split_string(allitems):
    first_half = allitems[0:int(len(allitems)/2)]
    second_half = allitems[int(len(allitems)/2):]
    return first_half, second_half

def identify_matching(comp_1, comp_2):
    match = None
    while match ==None:
        for item in comp_1:
            for item_2 in comp_2:
                if item == item_2:
                    match = item
    return match

def identify_alphabet_pos(letter):
    if letter.isupper() == True:
        position = string.ascii_uppercase.index(letter) + 27
    elif letter.isupper () == False:
        position = string.ascii_lowercase.index(letter) + 1
    return position

def part1():
    file = open('data_day3.txt', 'r')
    sum_priorities = 0
    for line in file:
        split_items = split_string(str(line.strip()))
        matching = identify_matching(*split_items)
        priority = identify_alphabet_pos(matching)
        sum_priorities += priority
        print(sum_priorities)

def grouped(iterator, size):
    yield tuple(next(iterator) for _ in range(size))

def part2():
    sum_score = 0
    with open('data_day3.txt') as file:
        while True:
            Three_rucksacks = list(islice(file, 3))
            if not Three_rucksacks:
                break

            rucksack1 = Three_rucksacks[0].strip()
            rucksack2 = Three_rucksacks[1].strip()
            rucksack3 = Three_rucksacks[2].strip()

            matching_1v2 = []

            badge = None
            for items_1 in rucksack1:
                for items_2 in rucksack2:
                    if items_2 == items_1:
                        matching_1v2.append(items_2)
            for items_3 in rucksack3:
                if items_3 in matching_1v2:
                    badge = items_3
            sum_score += identify_alphabet_pos(badge)

    return sum_score


print(part2())