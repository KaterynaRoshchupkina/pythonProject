input_string = 'hello 1 one two three 15 world'
words_in_a_row = input_string.split()

for i in range(len(words_in_a_row) - 2):
    if words_in_a_row[i].isalnum() and words_in_a_row[i + 1].isalnum() and words_in_a_row[i + 2].isalnum():
        print('The string contains three words in a row')
        break
    else:
        print('The string does not contain three words in a row')
        