import random
print('welcome our hangman game')
word_list = ['apple','mango','banana','orange','jackfruit']
choice_list = random.choice(word_list)
print(choice_list)
blank_display = []

# for i in choice_list:
#     blank_display.append('_')
# print(blank_display)

# for i in range(len(choice_list)):
#     blank_display.append('-')
# print(blank_display)

for i in choice_list:
    blank_display+='_'
print(blank_display)













