def intro():
    print("You wake up in a dark forest. Somewhere, a faint beacon shines.")
    choice = input("Which direction do you choose? (left/center/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "center":
        center_path()
    elif choice == "right":
        right_path()
    else:
        print("You pause to listen—your courage points the way, but you must choose next time.")

def left_path():
    print("You walk left and find a glowing sword in a stone.")
    take = input("Do you try to pull the sword free? (yes/no): ").strip().lower()
    if take == "yes":
        print("With a steady heart, you lift it. The light answers your courage. You vow to protect the forest.")
    else:
        print("You leave the sword—true heroes know when not to force destiny.")

def center_path():
    print("You follow the beacon to a clearing. A wounded traveler asks for help.")
    help_traveler = input("Do you share your supplies? (yes/no): ").strip().lower()
    if help_traveler == "yes":
        print("Your kindness restores their strength; they bless your journey.")
    else:
        print("You conserve resources, but promise to return—duty calls you onward.")

def right_path():
    print("You walk right and meet a talking squirrel guarding a tiny banner.")
    help_squirrel = input("The squirrel asks for help defending the grove. Help them? (yes/no): ").strip().lower()
    if help_squirrel == "yes":
        print("Together you outsmart the threat. The forest cheers your name.")
    else:
        print("You decline politely and share supplies. Kindness still changes the day.")

if __name__ == "__main__":
    intro()
