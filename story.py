def intro():
    print("You wake up in a dark forest. A cold wind whispers your name.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You hesitate. The shadows close in and claim you as their own.")

def left_path():
    print("You walk left and find a sword pulsing with dark light.")
    take = input("Do you pull the sword from the stone? (yes/no): ").strip().lower()
    if take == "yes":
        print("The blade bonds to your will. Power floods you. The forest bows to its new ruler.")
    else:
        print("You step back, but the sword’s whisper follows you... You won’t resist forever.")

def right_path():
    print("You walk right and meet a talking squirrel in ragged armor.")
    duel = input("The squirrel challenges you. Do you fight fair? (yes/no): ").strip().lower()
    if duel == "yes":
        print("You fight with honor—but honor is weak. You lose. Darkness laughs.")
    else:
        print("You feint, then strike from the shadows. The squirrel kneels. The woodland falls in line.")

if __name__ == "__main__":
    intro()
