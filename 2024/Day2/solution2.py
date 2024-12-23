
safe_count = 0
with open("input.txt" ,"r") as file:
    for line in file.readlines():
        report = line.strip().split(" ")
        break_line = False
        decreasing = False
        increasing = False
        error = 0
        for i in range(1, len(report)):
            decreasing = int(report[i-1])-int(report[i]) < 0 if not decreasing else decreasing
            increasing = int(report[i-1])-int(report[i]) > 0 if not increasing else increasing
            if (abs(int(report[i-1])-int(report[i])) == 0 or abs(int(report[i-1])-int(report[i])) > 3) or (decreasing and increasing):
                error += 1
                if error > 1:
                    break_line = True
                    break
        if break_line:
            break_line = False
            continue
        safe_count += 1

print(safe_count)
