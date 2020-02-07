print('Please think of a number between 0 and 100!')
low = 0
high = 100


while(True):
    ans = (low + high) // 2
    print('Is your secret number ' + str(ans) + '?')
    i = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    if i in 'lhc':
        if i == 'l':
            low = ans
        elif i == 'c':
            print('Game over. Your secret number was: ' + str(ans))
            break
        else:
            high = ans
    else:
        print('I am sorry, I did not understand your input')