import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen():
print("Welcome to Battleship!")

ships = [
    [(2, 2), (2, 3), (2, 4)], 
    [(4, 5), (5, 5)],  
    [(1, 6)],
    [(6, 0)]  
]
board = [['♥' for _ in range(7)] for _ in range(7)]

ship_positions = []
for ship in ships:
    for coord in ship:
        ship_positions.append(coord)
shots = 0

while ship_positions: 
    clear_screen()
    print("   A B C D E F G\n  ---------------")
    for row in range(7):
        print(f"{row + 1} | {' '.join(board[row])}")
    print(f"Shots: {shots}")
 shot = input("Please choose and enter coordinates (e.g., A1): ").strip().upper()

if len(shot) != 2 or shot[0] not in 'ABCDEFG' or not shot[1].isdigit():
        print("Incorrect format. Try again please!")
        input("Click Enter to continue...")
        continue
col, row = 'ABCDEFG'.index(shot[0]), int(shot[1]) - 1
