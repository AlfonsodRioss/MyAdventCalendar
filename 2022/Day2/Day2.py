f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day2\\input.txt", "r")
# B - X = 1 --> lose
# C - Y = 1 --> lose
# A - Z = -2 --> lose 0

# C - X = 2 ---> win
# A - Y = -1 ---> win
# B - Z = -1 ---> win 6

# A - X = 0 ---> tie 3
# B - Y = 0 ---> tie
# C - Z = 0 ---> tie

######################################
###             Part 1             ###
######################################

# score = 0
# for i in f:
#     opponent = ord(i[0])-64
#     mine = ord(i[2])-87

#     result = opponent-mine

#     if result == 0:
#         score += 3 + mine
#     elif result == -1 or result == 2:
#         score += 6 + mine
#     else:
#         score += mine

#     print(f"{i[0]} - {i[2]} = {opponent-mine} {score}")
# print(score)


######################################
###             Part 2             ###
######################################

# A - X = 0 ---> lose
# B - X = 1 --> lose
# C - X = 2 ---> lose

# A - Y = -1 ---> tie
# B - Y = 0 ---> tie
# C - Y = 1 --> tie

# A - Z = -2 --> win
# B - Z = -1 ---> win
# C - Z = 0 ---> win

# X = 1
# Y = 2
# Z = 3

# A = 1
# B = 2
# C = 3

score = 0
for i in f:

    opponent = ord(i[0])-64
    result = ord(i[2])-87

    match result:
        case 1:  # Lose
            match opponent:
                case 1:
                    score += 3
                case 2:
                    score += 1
                case 3:
                    score += 2

        case 2:  # Tie
            score += 3 + opponent

        case 3:  # Win
            match opponent:
                case 1:
                    score += 6 + 2
                case 2:
                    score += 6 + 3
                case 3:
                    score += 6 + 1

    print(f"{i[0]} - {i[2]} = {opponent} {score}")
print(score)
