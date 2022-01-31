import random
computer = 0
human = 0
print("\t\tWelcome to SNAKE WATER GUN ")

for i in range(1, 6):
    list1 = ["s", "w", "g"]
    _random = random.choice(list1)
    print("Press s for Snake.\nPress w for Water.\nPress g for Gun.\n")
    _input = input("Snake Water Gun:")

    if _random == _input:
        print("\nTie Both guess same")
        print(f"Computer Point {computer} and Human Point {human}\n")

    elif _random == "s" and _input == "w":
        computer = computer+1
        print(f"*****You Loss*****\nYou guess Water and Computer guess Snake")
        print(f"Computer Point {computer} and Human Point {human}\n")

    elif _random == "s" and _input == "g":
        human = human+1
        print(f"*****You Win*****\nYou guess Gun and Computer guess Snake")
        print(f"Computer Point {computer} and Human Point {human}\n")

    elif _random == "w" and _input == "s":
        human = human+1
        print(f"*****You Win*****\nYou guess Snake and Computer guess Water")
        print(f"Computer Point {computer} and Human Point {human}\n")

    elif _random == "w" and _input == "g":
        computer = computer+1
        print(f"*****You Loss*****\nYou guess Gun and Computer guess Water")
        print(f"Computer Point {computer} and Human Point {human}\n")

    elif _random == "g" and _input == "s":
        computer = computer+1
        print(f"*****You Loss*****\nYou guess Snake and Computer guess Gun")
        print(f"Computer Point {computer} and Human Point {human}\n")

    elif _random == "g" and _input == "w":
        human = human+1
        print(f"*****You Win*****\nYou guess Water and Computer guess Gun")
        print(f"Computer Point {computer} and Human Point {human}\n")

    else:
        print("Please Input Correct Word:\n")
    print(f"You have {(i-5)} attempts left\n")

if computer > human:
    print("\t\t**Computer Win**\n")
elif human > computer:
    print("\t\t**Human Win**\n")
elif computer == human:
    print("\t\t**Match Tie**\n")

print(f"Final Score: Computer = {computer} Human = {human}\nGame Over\nThanks for Playing")
