# Vowel Counter
vowels = 'aeiou'
count = 0
s = 'azcbobobegghakl'
for i in s:
    for v in vowels:
        if i == v:
            count += 1
print('Number of vowels: ' + str(count))
