######################################
###             Part 1             ###
######################################
f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day3\\input.txt", "r")

item_sum = 0
for i in f:
    middle = int((len(i)-1)/2)
    for letter in i[:middle]:
        if letter in i[middle:]:
            if letter.isupper():
                item_sum += ord(letter)-38
            else:
                item_sum += ord(letter)-96
            break
print(item_sum)

######################################
###             Part 2             ###
######################################
f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day3\\input.txt", "r")

badge_sum = 0
f = f.read().splitlines()
file_lines = len(f)

for i in range(0, file_lines, 3):
    team = f[i:i+3]
    for letter in team[0]:
        if letter in team[1] and letter in team[2]:
            if letter.isupper():
                badge_sum += ord(letter)-38
            else:
                badge_sum += ord(letter)-96
            break
print(badge_sum)
