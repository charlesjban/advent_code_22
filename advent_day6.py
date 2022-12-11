file = open("data_day6.txt", "r")

signal = file.read()


practice_string = "cfgcgjqgkjkjtpwdfgfhjkfdljfhqww"

def identify_start_sig(signal):

    list_of_letters = []

    for i in range(0,len(signal)):
        list_of_letters.append(signal[i])
        unique = len(set(list_of_letters[-4:]))
        if unique == 4:
            break
    return len(list_of_letters)

def identify_start_message(signal):
    list_of_letters = []

    for i in range(0,len(signal)):
        list_of_letters.append(signal[i])
        unique = len(set(list_of_letters[-14:]))
        if unique == 14:
            break
    return len(list_of_letters)



print(identify_start_sig(signal))
print(identify_start_message(signal))

file.close()
