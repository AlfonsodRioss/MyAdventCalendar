left_list = []
right_list = []
with open("input.txt" ,"r") as file:
    for line in file.readlines():
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
    
left_list.sort()
right_list.sort()

sum = 0

location_dict = {i:right_list.count(i) for i in right_list}

for j in left_list:
    reps = location_dict.get(j)
    sum += 0 if reps is None else reps * int(j)
    
    
print(sum)