# Find the number of times bob appears in a string
count = 0
bobs = 0
s = 'azcbobobegghakl'

for i in s:
    if s[count] == 'b':
        if s[count:count+3] == 'bob':
            bobs += 1

    count += 1

print('Number of times bob occurs is: ' + str(bobs))
