input_string = 'hello 1 one two three 15 world'
words_in_a_row = input_string.split()

found_three_words = False

for i in range(len(words_in_a_row) - 2):
    if words_in_a_row[i].isalpha() and words_in_a_row[i + 1].isalpha() and words_in_a_row[i + 2].isalpha():
        found_three_words = True
        break

if found_three_words:
    print('The string contains three words in a row')
else:
    print('The string does not contain three words in a row')
        