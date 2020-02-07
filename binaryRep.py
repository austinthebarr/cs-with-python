num = 11
isNeg = False

if num < 0:
    num = abs(num)
    isNeg = True

if num == 0:
    result = '0'

while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result

