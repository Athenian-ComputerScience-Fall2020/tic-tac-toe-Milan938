# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

def tictactoe(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board["TR"])
    print('--+--+--')
    print(board['ML'] + '|' + board['MM'] + '|' + board["MR"])
    print('--+--+--')
    print(board['BL'] + '|' + board['BM'] + '|' + board["BR"])


ttt = {'TL': ' ', 'TM': ' ', 'TR': ' ', 'ML': ' ', 'MM': ' ', 'MR': ' ', 'BL': ' ', 'BM': ' ', 'BR': ' '}

x = 0

while x <= 9:
    print("Please select which square you'd like to place your X or O on")
    selection = input()
    if selection == 'TL':
        print("Would you like to place an X or O there?")
        choice1 = input()
        ttt['TL'] = choice1
        x = x + 1 
    elif selection == 'TM':
        print("Would you like to place an X or O there?")
        choice2 = input()
        ttt.update({'TM': choice2})
        x = x + 1

    elif selection == 'TR':
        print("Would you like to place an X or O there?")
        choice3 = input()
        ttt.update({'TM': choice3})
        x = x + 1
    elif selection == 'ML':
        print("Would you like to place an X or O there?")
        choice4 = input()
        ttt.update({'TM': choice4})
        x = x + 1
    elif selection == 'MM':
        print("Would you like to place an X or O there?")
        choice5 = input()
        ttt.update({'TM': choice5})
        x = x + 1
    elif selection == 'MR':
        print("Would you like to place an X or O there?")
        choice6 = input()
        ttt.update({'TM': choice6})
        x = x + 1
    elif selection == 'BL':
        print("Would you like to place an X or O there?")
        choice7 = input()
        ttt.update({'TM': choice7})
        x = x + 1
    elif selection == 'BM':
        print("Would you like to place an X or O there?")
        choice8 = input()
        ttt.update({'TM': choice8})
        x = x + 1
    elif selection == 'BR':
        print("Would you like to place an X or O there?")
        choice9 = input()
        ttt.update({'TM': choice9})
        x = x + 1

if ttt['TL'] == ttt['TM'] == ttt['TR'] or ttt['ML'] == ttt['MM'] == ttt['MR'] or ttt['BL'] == ttt["BM"] == ttt['BR'] or ttt['TL'] == ttt['ML'] == ttt['BL'] or ttt['TM'] == ttt['MM'] == ttt['BM'] or ttt['TR'] == ttt['MR'] == ttt['BR'] or ttt['TL'] == ttt['MM'] == ttt['BR'] or ttt['TR'] == ttt['MM'] == ttt['BL']:
    print("Congrats, you won!")
elif x == 9:
    print("No one won:( ")
tictactoe(ttt)





