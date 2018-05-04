import os

while True:
    print("""
                          ####
                      ############
                ########################
    ####R#O#C#K#####P#A#P#E#R######S#C#I#S#S#O#R#S###
    
    Welcome to the good ol' rock-paper-scissors game.
    
    """)

    try:
        print("""Player 1, choose your weapon:
    1 = Rock
    2 = Paper
    3 = Scissors""")
        player1 = int(input())
        os.system('cls')
        assert 0 < player1 < 4, "***ERROR! You must enter a number between 1-3!"
    except Exception:
        raise

    if player1 == 1:
        p1 = "ROCK"
    elif player1 == 2:
        p1 = "PAPER"
    else:
        p1 = "SCISSORS"

    try:
        print("""Player 2, choose your weapon:
        1 = Rock
        2 = Paper
        3 = Scissors""")
        player2 = int(input())
        assert 0 < player2 < 4, "***ERROR! You must enter a number between 1-3!"
        os.system('cls')
    except Exception:
        raise

    if player2 == 1:
        p2 = "ROCK"
    elif player2 == 2:
        p2 = "PAPER"
    else:
        p2 = "SCISSORS"

    if p1 == p2:
        print("""
        **********SAME WEAPON ERROR*************
        
        Snap! Both player chose the same weapon!
        
        **********SAME WEAPON ERROR*************
        """)
        continue


    playerSummed = player1 + player2

    os.system('cls')
    print("Player 1 was playing as: " + p1 + "")
    print("Player 2 was playing as: " + p2 + "\n")

    #Paper wins
    if playerSummed == 3:
        if player1 == 2:
            print("Player 1 won. Congratulations!\n")
        else:
            print("Player 2 won. Congratulations!\n")

    #Rock wins
    elif playerSummed == 4:
        if player1 == 1:
            print("Player 1 won. Congratulations!\n")
        else:
            print("Player 2 won. Congratulations!\n")

    #Scissors wins
    else:
        if player1 == 5:
            print("Player 1 won. Congratulations!\n")
        else:
            print("Player 2 won. Congratulations!\n")

    print("Another round?")

    yesAnswers = ("y","Y","yes","Yes","YES","yeS")
    noAnswers = ("n","N","no","No","NO","nO")
    wannaPlay = str(input())
    assert (wannaPlay in yesAnswers or wannaPlay in noAnswers), "***ERROR! You must answer with 'yes' or 'no'."
    if wannaPlay in yesAnswers:
        os.system('cls')
        continue
    else:
        break
