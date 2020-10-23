# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

ttt = {'TL': ' ', 'TM': ' ', 'TR': ' ', 'ML': ' ', 'MM': ' ', 'MR': ' ', 'BL': ' ', 'BM': ' ', 'BR': ' '}

print("Please select which square you'd like to place your X or O on")
selection = input()

if selection == 'TL':
    print("Would you like to place an X or O there?")
    choice1 = input()
    ttt.update({'TL': choice1})

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









print(ttt)