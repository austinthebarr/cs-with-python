#Newton Raphson for Square root

epsilion = 0.01
k = 24
guess = k/2.0
count = 0

while abs(guess*guess)-k >= epsilion:
    count += 1
    guess = guess - (((guess**2)-k)/(2*guess))
print('Square root of ', k, 'is about', guess, ', it took', count, 'iterations to find')