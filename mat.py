import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
BOARD_SIZE = 7
SHIP_SIZES = [3, 2, 2, 1, 1, 1, 1]
EMPTY = " " 
HIT = "X"  
MISS = "O" 
    print("  A B C D E F G")
    print("  ---------------")
def display_grid():
    print("  A B C D E F G")
    for i in range(7):
        print(f"{i+1} ", end="")
        print(" ".join([" "]*7))
display_grid():
def play_game()
  player_name = input("Enter your name: ")
  print("Welcome to Battleship!")


play_game()
