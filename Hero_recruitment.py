collection = {}
while True:
    command = input()
    if command == "End":
        break
    command = command.split(" ")
    if "Enroll" in command:
        hero = command[1]
        if hero in collection:
            print(f"{hero} is already enrolled.")
        else:
            collection.update({hero:""})
    elif "Learn" in command:
        hero = command[1]
        spell = command[2]
        if hero not in collection:
            print(f"{hero} doesn't exist.")
            continue
        if collection[hero] == spell:
            print(f"{hero} has already learnt {spell}.")
        else:
            collection.update({hero:spell})
    elif "Unlearn" in command:
        hero = command[1]
        spell = command[2]
        if hero not in collection:
            print(f"{hero} doesn't exist.")
        elif collection[hero] != spell:
            print(f"{hero} doesn't know {spell}.")
        else:
            collection[hero] = ""
print("Heroes:")
for index, value in enumerate(collection):
    print(f"== {value}: {collection[value]}")