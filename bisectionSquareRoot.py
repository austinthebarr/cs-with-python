x = -25
ab = abs(x)
epsilon = .01
numGuesses = 0
isNeg = False
low = 0.0
high = max(1.0, ab)
ans = (high+low)/2.0

while abs(ans**2 - ab) > epsilon:
    numGuesses += 1
    if ans**2  < ab:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
if x < 0:
    print('numGuesses =', str(numGuesses))
    print('-' + str(ans), 'is close to the square root')
else:
    print('numGuesses =', numGuesses)
    print( str(ans), 'is close to the square root')


