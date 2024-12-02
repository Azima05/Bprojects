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
    print("  A B C D E F G")
    print("  ---------------")
    

