#!/usr/bin/env python3
"""
Activity 1: Build-Your-Own Escape Room (STARTER)

Follow the numbered TODOs in order. Run the file often to test as you go:
    python code/escape_room_starter.py
"""


def room_one(inventory):
    """Room 1: the player arrives here first."""
    print("You are in a dusty library. There is a door to the LEFT and a desk in front of you.")
    # TODO 1: Print a short description of the starting room.
    # Example: "You wake up in a dusty library. There is a door to the LEFT
    # and a desk in front of you."

    choice = input("What do you do?").lower()

    if choice in ("search desk", "open desk"):
        if has_item(inventory, "key"):
            print("You already have the key.")
        else:
            print("You found a key!")
            inventory.append("key")
        return "room_one"
    elif choice in ("go left", "go through door", "open door"):
        if has_item(inventory, "key"):
            print("You unlocked the door and walk through!")
            return "room_two"
        else:
            print("The door is locked. Maybe there's a key somewhere.")
            return "room_one"
    elif choice == "quit":
        return "quit"
    else:
        print("Try again.")
        return "room_one"


def room_two(inventory):
    """Room 2: reached after leaving room one."""
    print("You are in an abandoned laboratory. There is a door to the RIGHT and a locked cabinet in front of you.")

    choice = input("What do you do? ").lower()

    if choice == "quit":
        return "quit"
    elif choice in ("search cabinet", "open cabinet"):
        if has_item(inventory, "key"):
            print("You unlocked the cabinet and found a mysterious potion!")
            inventory.append("mysterious potion")
            return "room_two"
        else:
            print("The cabinet is locked. You need a key to open it.")
            return "room_two"
    elif choice in ("use potion", "drink potion"):
        if has_item(inventory, "mysterious potion"):
            print("You drink the mysterious potion, shrink, and slip under the door!")
            return "escaped"
        else:
            print("The door is locked. Look around for something that might help you escape.")
            return "room_two"
    else:
        print("Try again.")
        return "room_two"


def has_item(inventory, item_name):
    """Return True if item_name is in the player's inventory."""

    # TODO 6: Use a for loop to check each item in `inventory`.
    # If it matches item_name, return True. If the loop finishes without
    # finding it, return False.
    for item in inventory:
        if item == item_name:
            return True

    return False


def main():
    print("=== Escape Room ===")
    print("Type 'quit' at any time to give up.\n")

    inventory = []
    current_room = "room_one"

    # TODO 2: Set the loop condition so the game keeps running until the
    # player escapes or quits. Hint: use a `playing` boolean flag.
    playing = True
    while playing and current_room != "quit":
        if current_room == "room_one":
            current_room = room_one(inventory)
        elif current_room == "room_two":
            current_room = room_two(inventory)
        elif current_room == "escaped":
            print("\nYou escaped! Congratulations!")
            playing = False

    if current_room == "quit":
        print("\nMaybe next time!")


if __name__ == "__main__":
    main()
