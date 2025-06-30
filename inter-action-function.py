from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in [1,0,2]:
        guess = int(input("pickup a number : 0, 1, 2:  "))
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 0:
        print('correct guess')
    else:
        print('wrong! better luck next time')
        print(mylist)


mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list,guess)    