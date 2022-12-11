import os

file = open('data.txt', 'r')

opponent_dict = {"A":"Rock", "B": "Paper", "C":"Scissors"}
my_dict = {"X":"Rock", "Y": "Paper", "Z":"Scissors"}
outcome_dict = {"X":"Loose", "Y": "Draw", "Z":"Win"}

scores_shape = {"Rock": 1, "Paper": 2, "Scissors" : 3}
scores_outcome = {"Win": 6, "Loose": 0, "Draw": 3}


def who_wins(them, me):
    if them == "Rock":
        if me == "Rock":
            outcome = "Draw"
        if me == "Paper":
            outcome = "Win"
        if me =="Scissors":
            outcome = "Loose"
    if them == "Paper":
        if me == "Rock":
            outcome = "Loose"
        if me == "Paper":
            outcome = "Draw"
        if me =="Scissors":
            outcome = "Win"
    if them == "Scissors":
        if me == "Rock":
            outcome = "Win"
        if me == "Paper":
            outcome = "Loose"
        if me == "Scissors":
            outcome = "Draw"
    return outcome

def part_one():
    total_score = 0
    for line in file:
        opponent = opponent_dict[line.strip()[0]]
        mine = my_dict[line.strip()[2]]
        OutComeScore = scores_outcome[who_wins(opponent,mine)]
        ShapeScore = scores_shape[mine]
        score_overall = ShapeScore + OutComeScore
        total_score += score_overall

    print(total_score)

def what_to_play(them, outcome):

    if them == "Rock":
        if outcome == "Loose":
            me = "Scissors"
        if outcome == "Draw":
            me = "Rock"
        if outcome =="Win":
            me = "Paper"

    if them == "Paper":
        if outcome == "Loose":
            me = "Rock"
        if outcome == "Draw":
            me = "Paper"
        if outcome =="Win":
            me = "Scissors"

    if them == "Scissors":
        if outcome == "Loose":
            me = "Paper"
        if outcome == "Draw":
            me = "Scissors"
        if outcome =="Win":
            me = "Rock"
    return me

def part_two():
    total_score = 0
    for line in file:
        opponent = opponent_dict[line.strip()[0]]
        outcome = outcome_dict[line.strip()[2]]
        iplay = what_to_play(opponent, outcome)
        total_score += (scores_shape[iplay] + scores_outcome[outcome])
    print(total_score)

part_two()