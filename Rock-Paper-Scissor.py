import random  #imports random nuber
import os

playercount=0
compcount=0
while True:
    print("\n\t\t\t\t!!!ROCK PAPER SCISSOR GAME!!!")

    #displaying score
    print("\nSCORE:")
    print(f"computer:{compcount} player: {playercount} ")

    #game algorithm
    def game(comp,player):
        if comp==player:
            return None
        elif comp == 'r':
            if player=='p':
                return True
            elif player == 's':
                return False
        elif comp == 'p':
            if player=='r':
                return False
            elif player == 's':
                return True
        elif comp == 's':
            if player=='r':
                return True
            elif player == 'p':
                return False

    # assigning computer'r variable
    print("\n\nComputer turn: Rock(r)/Paper(p)/Scissors(s)")
    radNum= random.randint(1,3) #chooses random number from range 1-3 i.e. 1,2and3
    if radNum == 1:
        comp='r'
    elif radNum == 2:
        comp='p'
    elif radNum == 3:
        comp='s'

    # taking input from user
    player=input("Your turn: Rock(r)/Paper(p)/Scissors(s): ")
    a=game(comp,player)
    print(f"\nComputer chose {comp}")
    print(f"You chose {player}\n")

    # printing result
    if a==None:
        print("Tie Round!")
    elif a:
        print("You get 1 point")
        playercount=playercount+1
    else:
        print("Computer gets 1 point")
        compcount=compcount+1

    #final win, counts who has scored 5 frist
    if(playercount==5 and compcount<playercount):
        os.system('cls')
        print("\n\n\n\n\n\t\t\t\t!!!YOU WIN!!!")
        playercount=0
        compcount=0
        b=input("\n\n\tDo you want to play again?(Y/N): ")
        os.system('cls')
        if b=='n'or b=='N':
            break
    elif(compcount==5 and compcount>playercount):
        os.system('cls')
        print("\n\n\n\n\n\t\t\t\t!!!YOU LOSE!!!")
        playercount=0
        compcount=0
        b=input("\n\n\tDo you want to play again?(Y/N): ")
        os.system('cls')
        if b=='n'or b=='N':
            break

    input()
    os.system('cls')