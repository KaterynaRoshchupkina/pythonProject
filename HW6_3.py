petals = int(input('Please enter the number of petals:'))

if petals % 6 == 1:
    phrase = 'I love you'
elif petals % 6 == 2:
    phrase = 'a little'
elif petals % 6 == 3:
    phrase = 'a lot'
elif petals % 6 == 4:
    phrase = 'passionately'
elif petals % 6 == 5:
    phrase = 'madly'
else:
    phrase = 'not at all'

print('Phrase on the last petal:', phrase)
