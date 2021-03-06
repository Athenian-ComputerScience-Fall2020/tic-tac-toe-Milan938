# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# Megan 
# A note on style: Dictionaries can be defined before or after functions.
print("Use two letter abreviations to place your piece. Type the letter"
      "of the row first, T for top, M for middle, B for bottom. "
      "Then put where in the row you want your piece. "
      "R for right, M for middle, L for left. For example,"
      "if you want to play the top left square, write TL when asked.")

def tictactoe(board):
    print(board['TL'] + ' |' + board['TM'] + ' |' + board["TR"])
    print('--+--+--')
    print(board['ML'] + ' |' + board['MM'] + ' |' + board["MR"])
    print('--+--+--')
    print(board['BL'] + ' |' + board['BM'] + ' |' + board["BR"])

def winner(ttt):
    if ttt['TL'] == ttt['TM'] == ttt['TR'] == "X" or ttt['TL'] == ttt['TM'] == ttt['TR'] == "O":
        print("Congrats, you won!")
        tictactoe(ttt)
        quit()
    elif ttt['ML'] == ttt['MM'] == ttt['MR'] == "X" or ttt['ML'] == ttt['MM'] == ttt['MR'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()
    elif ttt['BL'] == ttt["BM"] == ttt['BR'] == "X" or ttt['BL'] == ttt["BM"] == ttt['BR'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()
    elif ttt['TL'] == ttt['ML'] == ttt['BL'] == "X" or ttt['TL'] == ttt['ML'] == ttt['BL'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()
    elif ttt['TM'] == ttt['MM'] == ttt['BM'] == "X" or ttt['TM'] == ttt['MM'] == ttt['BM'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()    
    elif ttt['TR'] == ttt['MR'] == ttt['BR'] == "X" or ttt['TR'] == ttt['MR'] == ttt['BR'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()    
    elif ttt['TL'] == ttt['MM'] == ttt['BR'] == "X" or ttt['TL'] == ttt['MM'] == ttt['BR'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()    
    elif ttt['TR'] == ttt['MM'] == ttt['BL'] == "X" or ttt['TR'] == ttt['MM'] == ttt['BL'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()    
    elif ttt['TL'] == ttt['TM'] == ttt['TR'] == "X" or ttt['TL'] == ttt['TM'] == ttt['TR'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()
    elif ttt['ML'] == ttt['MM'] == ttt['MR'] == "X" or ttt['ML'] == ttt['MM'] == ttt['MR'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()
    elif ttt['BL'] == ttt['BM'] == ttt['BR'] == "X" or ttt['BL'] == ttt['BM'] == ttt['BR'] == "O":
        print("Congrats, you won")
        tictactoe(ttt)
        quit()
    tictactoe(ttt)

ttt = {'TL': ' ', 'TM': ' ', 'TR': ' ', 'ML': ' ', 'MM': ' ', 'MR': ' ', 'BL': ' ', 'BM': ' ', 'BR': ' '}

x = 0

while x < 9:
    print("Please select which square you'd like to place your X or O on")
    selection = input()
    if selection == 'TL':
        if ttt['TL'] == ' ':
            print("Would you like to place an X or O there?")
            choice1 = input()
            ttt['TL'] = choice1
            x = x + 1 
            winner(ttt)
        else:
            print("Invalid Input")
    elif selection == 'TM':
        if ttt['TM'] == ' ':
            print("Would you like to place an X or O there?")
            choice2 = input()
            ttt.update({'TM': choice2})
            x = x + 1
            winner(ttt)
        else:
            print("Invalid Input")
    elif selection == 'TR':
        if ttt['TR'] == ' ':
            print("Would you like to place an X or O there?")
            choice3 = input()
            ttt.update({'TR': choice3})
            x = x + 1
            winner(ttt)
        else:
            print("Invalid Input")
    elif selection == 'ML':
        if ttt['ML'] == ' ':
            print("Would you like to place an X or O there?")
            choice4 = input()
            ttt.update({'ML': choice4})
            x = x + 1
            winner(ttt)
        else:
            print("Invalid Input")
    elif selection == 'MM':
        if ttt['MM'] == ' ':
            print("Would you like to place an X or O there?")
            choice5 = input()
            ttt.update({'MM': choice5})
            x = x + 1
            winner(ttt)
        else:
            print("Invalid Input")
    elif selection == 'MR':
        if ttt['MR'] == ' ':
            print("Would you like to place an X or O there?")
            choice6 = input()
            ttt.update({'MR': choice6})
            x = x + 1
            winner(ttt)
        else:
            print("Invalid Input")
    elif selection == 'BL':
        if ttt['BL'] == ' ':
            print("Would you like to place an X or O there?")
            choice7 = input()
            ttt.update({'BL': choice7})
            x = x + 1
            winner(ttt)
        else:
            print("Invalid Input")
    elif selection == 'BM':
        if ttt['BM'] == ' ':
            print("Would you like to place an X or O there?")
            choice8 = input()
            ttt.update({'BM': choice8})
            x = x + 1
            winner(ttt)
        else:
            print("Invalid Input")
    elif selection == 'BR':
        if ttt['BR'] == ' ':
            print("Would you like to place an X or O there?")
            choice9 = input()
            ttt.update({'BR': choice9})
            x = x + 1
            winner(ttt)
        else:
            print("Invalid Input")

if x == 9:
    print("No one won:( ")
    tictactoe(ttt)
    quit()







