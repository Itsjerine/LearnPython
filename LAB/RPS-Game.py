import random
def rules():
    print("Rock-Paper-Scissors GAME!!")
    print("RULES-------------")
    print("1 = Rock")
    print("2 = Paper")
    print("3 = Scissors")
    print("You can selact 1 time per game")
    print()


def game():
    player = 0
    Bot = 0

    while player != 5 and Bot != 5:
        Bot = random.randrange(1, 4, 1)
        choice = {
            1: "Rock",  # Key : Value
            2: "Paper",
            3: "Scissors"
        }

        player = int(input("Type your choice : "))
        print()
        if player >= 1 and player <= 3:
            print("Bot : ", choice[Bot])
            print("Bot : ", choice[player])
            if player == Bot:
                print("Darw")
                print("--------------------")
            # Rock vs Paper
            elif player == 1 and Bot == 2:
                print("You lose ,pls try again")
                print("--------------------")
            # Rock vs Scissors
            elif player == 1 and Bot == 3:
                print("YOU WIN!!")
                print("--------------------")
            # Paper vs Scissors
            elif player == 2 and Bot == 3:
                print("You lose ,pls try again")
                print("--------------------")
            # Paper vs Rock
            elif player == 2 and Bot == 1:
                print("YOU WIN!!")
                print("--------------------")
            # Scissors vs Rock
            elif player == 3 and Bot == 1:
                print("You lose ,pls try again")
                print("--------------------")
            # Scissors vs Paper
            elif player == 3 and Bot == 2:
                print("YOU WIN!!")
                print("--------------------")
        else:
            print("ERROR")


rules()
game()
