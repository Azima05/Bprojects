import random

def find_cargo():
    my_entered_positions = [2, 4, 6]
    weights = [250,240,223]
    total_weight_must_be = 713
    positions = my_entered_positions[:]

    while True:
        teacher_positions = []
        for i in range(3):
            km = int(input(f"Please Mr. Tauheed Khan enter the kilometer for box {i + 1}: "))
            teacher_positions.append(km)
            
        total_found_weight = 0
        for km in teacher_positions:
            if km in positions:
                total_found_weight += weights[positions.index(km)]

        if total_found_weight == total_weight_must_be:
            print("Cargo found and the total weight is correct!")
            break
        else:
            print(" Unfortunately incorrect. The positions of the boxes will change. It is okay, you can try again.")
            positions = random.sample(range(1, 7), 3)
find_cargo()
