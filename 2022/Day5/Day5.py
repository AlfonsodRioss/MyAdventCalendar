class Stack:

    # class attributes
    def __init__(self):
        self.crates = []

    # some methods
    def removeCrates(self, quantity):
        tempCrates = self.crates[-quantity:]
        self.crates = self.crates[:len(self.crates)-quantity]
        return tempCrates

    def addCrates(self, crates, v1=True):
        if v1:
            crates.reverse()
        for crate in crates:
            self.crates.append(crate)


######################################
###             Part 1             ###
######################################
f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day5\\input.txt", "r")

for index in range(9):
    globals()[f"S{index+1}"] = Stack()

for index, line in enumerate(f):
    if index < 8:
        counter = 1
        space_counter = 0
        next = False

        for character in line.strip():

            if next:
                globals()[f"S{counter}"].crates.insert(0, character)
                counter += 1
                next = False
                space_counter = 0

            if space_counter >= 4:
                counter += 1
                space_counter = 0

            if character == '[':
                next = True

            elif character == ' ':
                space_counter += 1

    elif index >= 10:
        instruction = line.strip().split(" ")
        move = instruction[1]
        fromStack = instruction[3]
        toStack = instruction[5]

        globals()[f"S{toStack}"].addCrates(
            globals()[f"S{fromStack}"].removeCrates(int(move)))

print('------------------------------------------------------------')
for index in range(9):
    print(f"""{index+1} - {globals()[f"S{index+1}"].crates[-1]}""")


######################################
###             Part 2             ###
f = open("c:\\Users\\AspenTech\\Documents\\Python\\MyAdventCalendar\\2022\\Day5\\input.txt", "r")

for index in range(9):
    globals()[f"S{index+1}"] = Stack()

for index, line in enumerate(f):
    if index < 8:
        counter = 1
        space_counter = 0
        next = False

        for character in line.strip():

            if next:
                globals()[f"S{counter}"].crates.insert(0, character)
                counter += 1
                next = False
                space_counter = 0

            if space_counter >= 4:
                counter += 1
                space_counter = 0

            if character == '[':
                next = True

            elif character == ' ':
                space_counter += 1

    elif index >= 10:
        instruction = line.strip().split(" ")
        move = instruction[1]
        fromStack = instruction[3]
        toStack = instruction[5]

        globals()[f"S{toStack}"].addCrates(
            globals()[f"S{fromStack}"].removeCrates(int(move)), False)

print('------------------------------------------------------------')
for index in range(9):
    print(f"""{index+1} - {globals()[f"S{index+1}"].crates[-1]}""")
