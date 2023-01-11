f = open("input.txt", "r")
sums = []
curr_num = 0
for i in (f):
    if i == '\n':
        sums.append(curr_num)
        curr_num = 0
    else:
        curr_num += int(i)
sums.append(curr_num)
s = sorted(sums, reverse=True)
print(f"Part1: {s[0]}")
print(f"Part2: {sum(s[:3])}")
