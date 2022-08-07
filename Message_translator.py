n = int(input())

for i in range(n):
    inp = input()
    if inp[0] != "!":
        print("The message is invalid")
        continue
    command = inp.split("!")[1]
    if "[" in inp and "]" in inp:  
        alphabetical_string = inp.split("[")
    else:
        print("The message is invalid")
        continue
    if "]" in alphabetical_string[1]:
        alphabetical_string = alphabetical_string[1].replace("]", "")
        
    if len(command) <= 3:  
        print("The message is invalid")
        continue
    boolVal = None
    for i in range(len(command)):
        if i == 0 and not command[i].isupper():
            print("The message is invalid")
            boolVal = True
            break
        elif i != 0 and command[i].isupper():
            print("The message is invalid")
            boolVal = True
            break
    if boolVal:
        continue
    if "!:" not in inp:
        print("The message is invalid")
        continue
    boolVal = None
    for i in alphabetical_string:
        if not i.isalpha():
            print("The message is invalid")
            boolVal = True
            break
    if boolVal:
        continue
    if len(alphabetical_string) <= 7:
        print("The message is invalid")
        continue
    value = []
    for i in alphabetical_string:
        value.append(ord(i))
    value_str = str(value)
    value_str = value_str.replace(",", "")
    value_str = value_str.replace("[", "")
    value_str = value_str.replace("]", "")
    print(f"{command}: {value_str}")
    

