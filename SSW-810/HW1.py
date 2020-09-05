from typing import Dict, List
import random

#r -> Rock, p -> Paper, s-> Scissors
choices: List[str] = ['r','p','s'] 
names: Dict[str, str] = {
    "r":"Rocks",
    "p":"Papers",
    "s":"Scissors"
}
rules: Dict[tuple, str] = {
    ("p","s"): "s",
    ("s","p"): "s",

    ("p","r"): "p",
    ("r","p"): "p",

    ("s","r"): "r",
    ("r","s"): "r",
}
def get_computer_move() -> str:
    """ randomly choose and return one of the choice in ['rock', 'paper', 'scissors'] """
    move: str = random.choice(choices)
    return move

def get_winner(selection1: str, selection2: str) -> int:
    """ returns the winner from the given selection paramenter based on logics from dictionary"""
    if selection1 == selection2:
        return "tie"
    else:
        return rules[(selection1, selection2)]

while True:
    print("\n--------- Starting a new game for you ------------\n")
    user_move:str = input("\nPlease choose 'r', 'p', 's' or 'q' to quit:")
    user_move = user_move.lower()
    if user_move=='q':
        print("You have ended the game, Bye bye :)")
        break
    elif(user_move == 'r' or user_move == 'p' or user_move == 's'):
        comp_move: str = get_computer_move();
        result:str = get_winner(user_move, comp_move)
        if(result == comp_move):
            print(f"You Lost!!! \nyou selected {names[user_move]} and computer selected {names[comp_move]}, so winner is {names[comp_move]}")
        elif result=="tie":
            print(f"Tie!!! \n That was a good choice you both selected {names[user_move]}")
        else:
            print(f"Voilaa! You Win!!! \nyou selected {names[user_move]} and computer selected {names[comp_move]}, so winner is {names[user_move]}")
    else:
        print("You have made an invalid choice, try again with correct Input")