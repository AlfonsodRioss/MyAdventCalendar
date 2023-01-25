######################################
###             Part 1             ###
######################################
f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day4\\input.txt", "r")

wrong_pair = 0
for pair in f:
    pair = pair.strip().split(",")
    pair1 = pair[0].split("-")
    pair2 = pair[1].split("-")
    if (int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1])) or (int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1])):
        wrong_pair += 1
print(wrong_pair)

######################################
###             Part 1             ###
######################################
f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day4\\input.txt", "r")

wrong_pair = 0
for index, pair in enumerate(f):
    pair = pair.strip().split(",")
    pair1 = pair[0].split("-")
    pair2 = pair[1].split("-")
    if (int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1])) or (int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1])):
        wrong_pair += 1
    else:
        for section in pair1:
            if int(section) >= int(pair2[0]) and int(section) <= int(pair2[1]):
                wrong_pair += 1
                break


print(wrong_pair)
