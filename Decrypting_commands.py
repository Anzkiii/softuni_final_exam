
decrypting_string = input()

while True:
    command = input()
    command = command.split(" ")
    if "Replace" in command:

        current_char = command[1]
        new_char = command[2]
        
        decrypting_string = decrypting_string.replace(current_char, new_char)
        print(decrypting_string)

    elif "Cut" in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0 or start_index > len(decrypting_string):
            print("Invalid indices!")
            continue
        if end_index < 0 or end_index > len(decrypting_string):
            print("Invalid indices!")
            continue
        substring = decrypting_string[start_index:end_index + 1]
        decrypting_string = decrypting_string.replace(substring, "")
        print(decrypting_string)
    elif "Make" in command:
        if command[1] == "Upper":
            decrypting_string = decrypting_string.upper()
            print(decrypting_string)
        elif command[1] == "Lower":
            decrypting_string = decrypting_string.lower()
            print(decrypting_string)
    elif "Check" in command:

        if command[1] in decrypting_string:
            print(f"Message contains: {command[1]}")
        else:
            print(f"Message doesn't contain {command[1]}")
    elif "Sum" in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0 or start_index > len(decrypting_string):
            print("Invalid indices!")
            continue
        if end_index < 0 or end_index > len(decrypting_string):
            print("Invalid indices!")
            continue        
        substring = decrypting_string[start_index:end_index + 1]
        value = 0
        for i in substring:
            value += ord(i)
        print(value)
    if command == "Finish":
        break