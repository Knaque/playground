"""Shows the differences between lists and dicts."""
from quikr import clear

clear()

print("First, you'll see how lists work.")
print("You can add items to this list by typing each value and hitting enter.")
print("When you're done, press enter with nothing typed.")

my_list = []

while True:
    my_input = input()
    try:
        my_input = int(my_input)
    except ValueError:
        None
    if my_input != "":
        my_list.append(my_input)
    else:
        if len(my_list) == 0:
            print("Please enter at least one item.")
            continue
        else:
            break

clear()

print(f"You've just made a list with {len(my_list)} items:")
print(my_list)
print(f"Now you can type the index (0-{len(my_list)-1}) to get that",
      "respective item!")
print("When you're done, press enter with nothing typed.")

while True:
    my_input = input()
    try:
        my_input = int(my_input)
    except ValueError:
        if my_input == "":
            break
        else:
            print("Indexes must be integers!")
            continue
    try:
        print(f"Value at index '{my_input}' = '{my_list[my_input]}'")
    except IndexError:
        print("That index is invalid!")

# =============================================================================

clear()

print("Now, you'll see how dictionaries (dicts) work.")
print("You can add items to this dict by typing a key and hitting enter,",
      "then typing a value and hitting enter again.")
print("Just like a real dictionary, you have the word (key), and the",
      "definition (value).")
print("When you're done, press enter with nothing typed.")

my_dict = {}

while True:
    my_key = input()
    if my_key == "":
        if len(my_dict) == 0:
            print("Please enter at least one item.")
            continue
        else:
            break

    my_value = input()
    try:
        my_value = int(my_value)
    except ValueError:
        None

    my_dict[my_key] = my_value


clear()

print(f"You've just made a dict with {len(my_dict)} items:")
print(my_dict)
print(f"Now you can type the key to get that respective item!")
print("When you're done, press enter with nothing typed.")

while True:
    my_input = input()
    if my_input != "":
        try:
            print(f"Value at key '{my_input}' = '{my_dict[my_input]}'")
        except KeyError:
            print("That key doesn't exist!")
    else:
        break

clear()

print("So, as you can tell, lists and dicts are pretty similar.")
print("The key difference being the keys that dictionaries use,")
print("instead of the indexes of lists.")
print("If you want, you can think of lists as dictionaries where all")
print("the keys are numbers instead of text.")
print("Great! Now you've learned how lists and dicts work.")
print("Hit enter to close.")

input()

clear()
