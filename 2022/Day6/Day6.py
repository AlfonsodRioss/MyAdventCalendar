######################################
###             Part 1             ###
######################################
f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day6\\input.txt", "r")

for line in f:
    for index in range(len(line)):
        if len(set(line[index:index+4])) == 4:
            print(index+4, line[index:index+4])
            break

######################################
###             Part 2             ###
######################################
f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day6\\input.txt", "r")

for line in f:
    for index in range(len(line)):
        if len(set(line[index:index+14])) == 14:
            print(index+14, line[index:index+14])
            break
