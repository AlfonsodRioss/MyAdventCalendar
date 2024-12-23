left_list = []
right_list = []
with open("input.txt" ,"r") as file:
    for line in file.readlines():
        left, right = line.split("   ")
        left_list.append(left)
        right_list.append(right)
    
left_list.sort()
right_list.sort()

sum = 0
for j,k in zip(left_list, right_list):
    sum += abs(int(j)-int(k))
    
print(sum)