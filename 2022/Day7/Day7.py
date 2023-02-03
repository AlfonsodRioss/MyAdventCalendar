INPUT_FILE = "c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day7\\input.txt"

total_sum = 0
temp_array = [0]
sum_flag = False
min_dir_size = 30000000

with open(INPUT_FILE, "r", encoding="UTF-8") as file:

    ######################################
    ###           Part 1 & 2           ###
    ######################################

    for line in file:
        clean_line = line.strip().split(" ")
        if clean_line[0] == '$' and clean_line[1] == 'ls':
            sum_flag = True

        if clean_line[0] == '$' and clean_line[1] == 'cd':
            sum_flag = False
            if clean_line[2] == '..':
                if temp_array[-1] <= 100000:
                    total_sum += temp_array[-1]

                if temp_array[-1] >= 4965705 and temp_array[-1] < min_dir_size:
                    min_dir_size = temp_array[-1]

                temp_array.pop()
            else:
                temp_array.append(0)

        if sum_flag and clean_line[0].isnumeric():
            temp_array = [x+int(clean_line[0]) for x in temp_array]

print(total_sum, min_dir_size)
