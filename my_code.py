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


print("Please select which square you'd like to place your X or O on")
selection = input()
plays == plays + 1

if selection == 'TL':
    print("Would you like to place an X or O there?")
    choice1 = input()
    ttt['TL'] = choice1

elif selection == 'TM':
    print("Would you like to place an X or O there?")
    choice2 = input()
    ttt.update({'TM': choice2})


elif selection == 'TR':
    print("Would you like to place an X or O there?")
    choice3 = input()
    ttt.update({'TM': choice3})

elif selection == 'ML':
    print("Would you like to place an X or O there?")
    choice4 = input()
    ttt.update({'TM': choice4})

elif selection == 'MM':
    print("Would you like to place an X or O there?")
    choice5 = input()
    ttt.update({'TM': choice5})

elif selection == 'MR':
    print("Would you like to place an X or O there?")
    choice6 = input()
    ttt.update({'TM': choice6})

elif selection == 'BL':
    print("Would you like to place an X or O there?")
    choice7 = input()
    ttt.update({'TM': choice7})

elif selection == 'BM':
    print("Would you like to place an X or O there?")
    choice8 = input()
    ttt.update({'TM': choice8})

elif selection == 'BR':
    print("Would you like to place an X or O there?")
    choice9 = input()
    ttt.update({'TM': choice9})

plays = 0

while plays <= 9:
    if board['TL'] == board['TM'] == board['TR'] or board['ML'] == board['MM'] == board['MR'] or board['BL'] == board["BM"] == board['BR'] or board['TL'] == board['ML'] == board['BL'] or board['TM'] == board['MM'] == board['BM'] or board['TR'] == board['MR'] == board['BR'] or board['TL'] == board['MM'] == board['BR'] or board['TR'] == board['MM'] == board['BL']:
        print("Congrats, you won!")
        break
    elif plays == 9:
        print("No one won:(")
        break

tictactoe(ttt)





