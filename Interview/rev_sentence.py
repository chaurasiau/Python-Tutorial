# sentence = list(input(f"Enter a sentence : "))
sentence = list(f"Reverse this string")
rev_sentence = ''
# for i in sentence.split(' '):
#     rev_sentence = f"{i} {rev_sentence}"

# print(f"The reverse of {sentence} is \n {rev_sentence.capitalize()}")

# rev_sentence = ' '.join(reversed(sentence.split(' ')))
# print(f"The reverse of {sentence} is \n {rev_sentence.capitalize()}")

new_sentence = ''
word = ''

for char in sentence[::-1]:
    rev_sentence = char + rev_sentence

print(''.join(new_sentence))
