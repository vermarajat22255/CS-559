from typing import Dict, List
import random

#r -> Rock, p -> Paper, s-> Scissors
choices: List[str] = ['r','p','s'] 

# Mapping Names with abbreviation for better output
names: Dict[str, str] = {
    "r":"Rocks",
    "p":"Papers",
    "s":"Scissors"
}

# rules dictionary to help decide the winner
rules: Dict[tuple, str] = {
    ("p","s"): "s",
    ("s","p"): "s",
    ("p","r"): "p",
    ("r","p"): "p",
    ("s","r"): "r",
    ("r","s"): "r",
}

def get_computer_move() -> str:
    """ randomly choose and return one of the choice in ['r', 'p', 's'] """
    move: str = random.choice(choices)
    return move

def get_winner(selection1: str, selection2: str) -> str:
    """ returns the winner from the given selection paramenter based on logics from rules dictionary"""
    if selection1 == selection2:
        return "tie"
    else:
        return rules[(selection1, selection2)]

def play_game() -> bool:
    """ An interactive rock, paper, scissors game that allows a human to play against a computer indefinitely until human quit.
    The winner is determined by the set of rules"""

    print("\n--------- Starting a new game for you ------------\n")
    user_move:str = input("\nPlease choose 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' to quit:")
    user_move = user_move.lower()
    
    if user_move=='q':
        return False    #Quit game
    
    elif user_move in choices:
        comp_move: str = get_computer_move();
        result:str = get_winner(user_move, comp_move)
        if result == comp_move:
            print(f"You Lost!!! \nyou selected {names[user_move]} and computer selected {names[comp_move]}, so winner is {names[comp_move]}")
        elif result=="tie":
            print(f"Tie!!! \n That was a good choice you both selected {names[user_move]}")
        else:
            print(f"Voilaa! You Win!!! \nyou selected {names[user_move]} and computer selected {names[comp_move]}, so winner is {names[user_move]}")
    
    else:
        print("You have made an invalid choice, try again with correct Input")
    
    return True

def main() -> None:
    """ Play multiple games until the human asks to stop """
    print("Hello, Let's begin to play Rock, Paper & Scissors")
    play_again: bool = True
    
    while play_again:
        play_again = play_game()
    
    print("You have ended the game, Bye bye\n")

if __name__ == "__main__":
    main()