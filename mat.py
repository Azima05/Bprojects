import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def randomize_ships():
   
    available_coords = [(row, col) for row in range(7) for col in range(7)]
    random.shuffle(available_coords)

    ships = [
        [(2, 2), (2, 3), (2, 4)],  
        [(4, 5), (5, 5)],
        [(4, 1), (4, 2)],    
        [(1, 6)],
        [(0, 3)], 
        [(0, 0)],   
        [(6, 0)] 
    ]
    random_ships = []
    available_index = 0
    
    for ship in ships:
        new_ship = []
        for _ in ship:
            new_ship.append(available_coords[available_index])
            available_index += 1
        random_ships.append(new_ship)

    return random_ships
    
print("Welcome to ALA-TOO Battleship!")
name = input("WHAT IS YOUR NAME? ")

play_again = True
while play_again:
   
    ships = [
        [(2, 2), (2, 3), (2, 4)],  
        [(4, 5), (5, 5)],
        [(4, 1), (4, 2)],    
        [(1, 6)],
        [(0, 3)], 
        [(0, 0)],   
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
        print(f"Welcome, {name}!")
        print("   A Z I M B D S \n  ---------------")
    
        for row in range(7):
            print(f"{row + 1} | {' '.join(board[row])}")
        print(f"Shots: {shots}")
        shot = input("Please choose and enter coordinates (e.g., A1): ").strip().upper()

        if len(shot) != 2 or shot[0] not in 'AZIMBDS' or not shot[1].isdigit():
            print("Incorrect format. Try again please!")
            input("Click Enter to continue...")
            continue
        col, row = 'AZIMBDS'.index(shot[0]), int(shot[1]) - 1

        if not (0 <= row < 7 and 0 <= col < 7) or board[row][col] != '♥':
            print("Invalid or already shot! Try again.")
            input("Click Enter to continue...")
            continue

        shots += 1

        if (row, col) in ship_positions:
            print("Hit!")
            board[row][col] = 'H'  
            ship_positions.remove((row, col))  
        else:
            print("Miss!")
            board[row][col] = 'M'
    
        input("Press Enter to continue...")

    print(f"Congratulations, {name}! You sank all the ships in {shots} shots!")
    play_again_input = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again_input == 'yes':
        play_again = True 
    else:
        play_again = False 
        print("Thank you for playing!")

    

