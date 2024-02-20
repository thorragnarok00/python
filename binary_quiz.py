import random

def generate_binary_number(length):
    binary_number = ''
    for _ in range(length):
        binary_digit = random.choice(['0', '1'])
        binary_number += binary_digit

    return binary_number

def binary_quiz():

    score, items, level = 0, 0, 0

    while True:

        length_of_binary_number = 4 + level
        binary_number = generate_binary_number(length_of_binary_number)
        correct_answer =  int(binary_number, 2)
        print("Binary number:", binary_number)

        while True:
            try:
                user_guess = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        items += 1

        if user_guess == correct_answer:
            print("You got it right!")
            score += 1
        else:
            print("You got it wrong!")

        print(f"Score: {score}/{items}\n")
        response = input("You want to continue (Y/N)? ").upper()
        if response == "Y":
            print()
            level += 1
        elif response == "N":
            print(f"Final Score: {score}/{items}")
            break

if __name__ == "__main__":
    binary_quiz()