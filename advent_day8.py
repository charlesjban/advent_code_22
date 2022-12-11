
file = open("data_day8.txt",'r')



# for line in file:
#     print(line)


def look_into_forest(row):
    for i in range(0,len(row)):
        tree = row[i]
        for previous_tree in range(0,int(row[i])):
            print(tree, row[i])



# for line in file:
#     look_into_forest(line)

look_into_forest("0244111344919512155434523410312")


file.close()