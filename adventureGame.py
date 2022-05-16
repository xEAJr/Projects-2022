from ast import Continue, If, Return
import time
import random
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)


def valid_input(prompt, options):

 while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


player_name = input(
    "Welcome, tarnished, What name do you want to go by?\n")


def chapel_of_anticipation():
    print_pause(
        f"{player_name},One day You find yourself\n\n"
        "in the chapel of anticipation\n")
    print_pause(
        "With no memory as to your past you decide\n\n"
        "to look for answers.\n")
    print_pause(
        "You are dressed in armor that is suited for battle.\n")
    print_pause(
        "You have a shield in your left hand and a sword in your right.\n")
    print_pause(
        "You exit the chapel after you look for loot and find nothing.\n")
    print_pause(
        "You open the doors and are greeted by a\n\n"
        "wonderful view of Limgraveat night. \n")
    print_pause(
        "You descend the steps of the chapel and head north.\n")
    print_pause(
        "All of a sudden you are attacked by the 'Grafted Scion'\n")
    grafted_scion()


def grafted_scion():
    choice = valid_input(
        "Do you wish to fight the Grafted Scion?"
        "(1.Yes or 2.No", ['1', '2'])
    if "1" in choice:
        correctPath = random.randint(1, 2)
        if choice == str(correctPath):
            print_pause(
                "You bide your time and look for an opening.\n")
            print_pause(
                "He charges you and you roll\n\n"
                "and as you roll you spot it.\n")
            print_pause(
                "You spot an opening in his body\n\n"
                "that exposes his heart when he attacks.\n")
            print_pause(
                "The next hime he attacks, you\n\n"
                "take advantage and you spear his heart.\n")
            print_pause(
                "Congratulations! you have\n\n"
                "defeated the 'Grafted Scion'!\n")
            print_pause(
                "You pick up the\n\n"
                "'Rivers of Blood'!\n")
            items.append("Rivers of Blood")
            limgrave()

        else:
            print_pause(
                "You charge the Grafted Scion\n")
            print_pause(
                "You swing your sword as he does the same.\n")
            print_pause(
                "both your strikes hit at the same time\n\n"
                "however the Grafted Scion's is much more powerful\n")
            print_pause(
                "You fall to the ground as you\n\n"
                "feel your life fade away.\n")
            print_pause(
                f"The story of {player_name}, has ended.\n")
            play_again()

    else:
        print_pause(
            "You decide that he looks too\n\n"
            "powerful and try to sneak past him.\n")
        print_pause(
            "He notices you and lunges in to attack.\n")
        print_pause(
            "His attack is so powerful he staggers you.\n")
        print_pause(
            "You try to recover but he attacks again.\n")
        print_pause(
            "You manage to dodge and run away!\n")
        limgrave()


def limgrave():
    print_pause(
        "You are now on your way to\n\n"
        "Leyndell in search of the Elden Ring\n")
    print_pause(
        "All of a sudden you hear a horse patrolling the area.\n")
    print_pause(
        "You look around to see where it is coming\n\n"
        "from and you see a general draped in Gold Armor.\n")
    print_pause(
        "He is riding his horse that is also draped in gold armor.")
    print_pause(
        "This is the one they call the 'Tree Sentinel'\n")
    tree_sentinel()


def tree_sentinel():
    choice = valid_input(

"Do you wish to fight the tree sentinel?"
        "(1.Yes 2.No)", ['1', '2'])
    if '1' in choice:

        if "Rivers of Blood" in items:
            print_pause(
                "You approach the Tree Sentinel cautiously\n")
            print_pause(
                "He attacks and you dodge!\n")
            print_pause(
                "You prepare to unleash everything\n\n"
                "you got into one attack.\n")
            print_pause(
                "You lift your sword and charge \n\n"
                "all your energy into a flame.\n")
            print_pause(
                "As he charges you again you unleash\n\n"
                "a flame so high it lights up the dark sky.\n")
            print_pause(
                "You land a fatal blow eliminating the Tree Sentinel!\n")
            print_pause(
                f"Congratulations {player_name}, you have won the game!\n")
            print_pause(
                "Best of luck in your search of the Elden Ring! TBC...\n")
            play_again()
        else:

            print_pause(
                "You decide that he looks slow\n\n"
                "and clunky in his heavy armor.\n")
            print_pause(
                "Oh no! as you try and sneak\n\n"
                "up to him he notices you!\n")
            print_pause(
                "His attack is so powerful he staggers you.\n")
            print_pause(
                "You try to recover but he\n\n"
                "attacks again and this time...")
            print_pause(
                "it is the final blow.\n")
            print_pause(
                f"The story of {player_name}has ended.\n")
            play_again()

    elif '2' in choice:
        print_pause(
            "You decide to run away but\n\n"
            "he spots and grabs you!\n")
        print_pause(
            "You take a giant swing and\n\n"
            "escape his grasp.\n")
        print_pause(
            "You run away after realizing\n\n"
            "he is too powerful for you\n")
        return_to()

        return tree_sentinel()


def return_to():
    choice = valid_input(
        "Where would you like to go? 1. Return to the Grafted Scion"
        "2. The Tree Sentinel", ['1', '2'])
    if choice == '1':
        grafted_scion()

    elif choice == '2':
        tree_sentinel()


def play_again():
    choice = valid_input("Play again? [y|n]", ['y', 'n'])
    if choice == 'y':
        chapel_of_anticipation()
    elif choice == 'n':
        print_pause("Goodbye! Thanks for playing!")
        exit(0)


def game():
    chapel_of_anticipation()
    limgrave()


if __name__ == '__main__':
    game()

