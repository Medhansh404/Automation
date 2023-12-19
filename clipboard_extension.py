import sys
import clipboard
import json

# clipboard.copy("abc")
# x = clipboard.paste()

# The way i am going to approach this is:
# Based on the sys arg we give on the terminal there will be two things
# 1.to see what is on the clipboard
# 2. to use the copied thing on clipboard or basically paste stuff
# For this we also will have to add some function that stores the copied stuff.
# Declaration of required variables
inp = ''
SAVED_DATA = "clipboard.json"


# creating the Json file to store stuff


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data

    except:
        return {}


def clear_data(filepath):
    with open(filepath, "w") as f:
        json.dump({}, f)


def last_key(data):
    if len(data) == 0:
        return 0
    else:
        keys = []
        for i in data:
            keys.append(i)
        keys.sort()
        x = int(keys[-1].split(" ")[1]) + 1
        return x


if len(sys.argv) == 2:
    data = load_items(SAVED_DATA)
    inp = sys.argv[1]

    # 1.to see what is on the clipboard
    if inp == "list":
        print(f"The content on the clipboard is:")
        for i in data:
            print(f"{data[i] + ' '}")
    # 2. add element to the clipboard
    if inp == "save":
        key = inp + " " + str(last_key(data))
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
    # 3. use the element from the clipboard
    if inp == "paste":
        key = input("Enter the position of the data you wish to paste")
        for i, item in enumerate(data):
            if int(key) <= len(data):
                if i == int(key) - 1:
                    clipboard.copy(data[item])
                    print(f"You can now paste the data you requested")
                    break
            else:
                print(f"Enter valid Number")
    # 4.Clearing the json file
    if inp == "clear":
        clear_data(SAVED_DATA)
