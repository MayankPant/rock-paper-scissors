# stone paper scissors
import random


# for player vs chose player2 rather than a random choice

def startTheGame(numOfGames):
    playerName1 = input("Enter your name player 1 ")
    playerName2 = input("Enter your name player 2 ")
    WinScenarious = {"Stone": "Scissors", "Scissors": "Paper", "Paper": "Stone"}
    score1 = 0
    score2 = 0
    while score1 < numOfGames and score2 < numOfGames:
        player1 = input(f"Enter for {playerName1} : ")
        player2 = random.choice(list(WinScenarious.keys()))

        if player1 in WinScenarious.keys() and player2 in WinScenarious.keys():
            if player2 == WinScenarious.get(player1):
                score1 += 1
                print(f"{playerName2} :", player2)
                print(f"{playerName1} : ", score1, f"{playerName2} : ", score2)
            elif player1 == WinScenarious.get(player2):
                score2 += 1
                print(f"{playerName2} :", player2)
                print(f"{playerName1} : ", score1, f"{playerName2} : ", score2)
            else:
                print("Tied")
                print(f"{playerName1} : ", score1, f"{playerName2} : ", score2)
        else:
            print("Enter a valid Choice Or else you will be penalised by 0.5 points ")
            if player1 not in WinScenarious.keys():
                score1 -= 0.5
                print(f"{playerName1} : ", score1, f"{playerName2} : ", score2)
                continue

            elif player2 not in WinScenarious.keys():
                score2 -= 0.5
                print(f"{playerName1} : ", score1, f"{playerName2} : ", score2)
                continue

    if score1 > score2:
        print(playerName1 + " Won!")
    else:
        print(playerName2 + " Won!")

    wantToContinue = input("Do you want to try an another game? if yes, enter YES else enter NO : ")
    if wantToContinue == "YES":
        noOfGames = input("Enter total no of games you want to play : ")
        startTheGame(noOfGames)


noOfGames = int(input("Please Enter total no of games you want to play : "))
startTheGame(noOfGames)
