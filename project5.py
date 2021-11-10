#snake water gun
import random
list=["s","w","g"]

chance=10
no_of_chance=0
computer_point=0
human_point=0

print("start the game now")
print("play snake water gun snake for \"s\" water for,\"w\", gun for \"g\"")
while no_of_chance<chance:
    inp=input("enter the choice: ")
    ran=random.choice(list)

    if ran==inp:
        print("game tie!")

    elif ran=="w" and inp=="g":
        computer_point=computer_point+1
        print(f"your choice is {inp} and computer choice is {ran}")
        print("computer win 1 point")
        print(f"computer {computer_point} point and human {human_point} point")

    elif ran=="s" and inp=="g":
        human_point=human_point+1
        print(f"your choice is {inp} and computer choice is {ran}")
        print("human win 1 point")
        print(f"computer {computer_point} point and human {human_point} point")

    elif ran=="g" and inp=="w":
        human_point=human_point+1
        print(f"your choice is {inp} and computer choice is {ran}")
        print("human win 1 point")
        print(f"computer {computer_point} point and human {human_point} point")

    elif ran=="w" and inp=="s":
        computer_point=computer_point+1
        print(f"your choice is {inp} and computer choice is {ran}")
        print("computer win 1 point")
        print(f"computer {computer_point} point and human {human_point} point")

    elif ran=="g" and inp=="s":
        computer_point=computer_point+1
        print(f"your choice is {inp} and computer choice is {ran}")
        print("computer win 1 point")
        print(f"computer {computer_point} point and human {human_point} point")

    else:
        print("wrong input")

    no_of_chance=no_of_chance+1
    print(f"number of chances left out of chances{chance-no_of_chance}")

if computer_point>human_point:
    print("computer win")
    print("Thank you")
else:
    print("human win")
    print("Thank you")


