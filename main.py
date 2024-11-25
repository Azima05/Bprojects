def play_game():

    positions = [2, 4, 6] 
    weights = [300, 200, 213]

    total_weight = sum(weights) 

    guessed_weight = 0
    attempts = 0


    print("Welcome to the Martian Cargo Treasure Hunt!")
    print("Try to guess the locations of the 3 hidden cargo boxes.")
    print("The boxes are hidden somewhere between kilometers 1 and 7.")

    while guessed_weight != total_weight:
        guessed_weight = 0
        guessed_positions = []
        for i in range(3):
           guess = int(input(f"Guess the location of box {i+1} (1-7): "))
           if guess in positions:
                guessed_positions.append(guess)
                guessed_weight += weights[positions.index(guess)]
                print(f"Found box {i+1} at kilometer {guess}, it weighs {weights[positions.index(guess)]} kg!")
           else:
               print(f"Box {i+1} is not at kilometer {guess}. Try again!")
        if guessed_weight == total_weight:
            print(f"Congratulations! You've found all the boxes with a total weight of {guessed_weight} kg.")
            break
        else:
            print(f"Sorry, you need to try again! Your current total weight is {guessed_weight} kg.")
        attempts += 1
play_game()
