from time import sleep
categories = ["alchemy_and_equipment", "camera", "characters", "combat", "gameplay", "quests_and_adventures", "user_interface", "visuals_and_graphics", "miscellaneous"]

def isCategoryInLine(line):
    for cat in categories:
        if cat in line: return True
    return False

# python -m PyInstaller xmlEditor.py --onefile
file = ""
while True:
    try:
        file = input("Enter file name: ")
        if not file.endswith(".xml"): file += ".xml"
        with open(file) as f:
            lineList = f.readlines()
            break
    except FileNotFoundError:
        print("Cannot find file")

i = 0
for i,value in enumerate(categories):
    print(f"{i+1}: {categories[i]}")

num = input("Enter the category index (integer value): ")
while not num.isdigit():
    print("Invalid input. Please enter an integer.")
    num = input("Enter the category index (integer value): ")
num = int(num)
category = categories[num-1]

for i, line in enumerate(lineList):
    if "group id" in line.lower() and not isCategoryInLine(line):
        lineList[i] = line.replace(".", f".{category}.", 1)

with open(file, "w") as f:
    for line in lineList:
        f.write(line)

dx12 = "dx12filelist.txt"
with open(dx12, "r+") as f:
    lineList = f.read()
    if file not in lineList:
        file += ";\n"
        f.write(file)

print("Successful! Exiting in...")
for i in range(3):
    print(3-i)
    sleep(.8)
exit()
