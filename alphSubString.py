# Longest Substring in Alphabetical Order

temp = ''
re = ''
s = 'azcbobobegghakl'
for ch in s:
    if temp == '':
        temp += ch
    elif temp[-1] <= ch:
        temp += ch
    else:
        if len(temp) > len(re):
            re = temp
            temp = ''
        temp = ''
        temp += ch
if len(temp) > len(re):
    re = temp
    print('Longest substring in alphabetical order is: ' + re)
else:
    print('Longest substring in alphabetical order is: ' + re)
