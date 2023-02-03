# Question 12: Given the dictionary below, create a list called my_al_list
# which includes only the values (meaning) associated with each word.
# my_al_list should look like ['the round fruit of a tree of the rose family',
# 'an insect which cleans up the floor'......].
# Obviously do this programmatically and don't hardcode it, you may use
# other lines of code and variables as you see fit. Solution code has a couple of
# options displayed.

word_dict = {'a':
                {
                 'apple': 'the round fruit of a tree of the rose family',
                 'ant': 'an insect which cleans up the floor'
                },
             'b':
                {
                 'bad': 'of poor quaity or low standard',
                 'business': 'season 8 of GOT',
                 'c' :
                     {
                        'a': 'b'
                     }
                }
            }

# print(word_dict[]['apple'])
# print(len(word_dict.values()))
my_al_list = []

for i, j in word_dict.items() :
    for k in j.values() :
        my_al_list.append(k)
    # my_al_list [k] = word_dict[k][v]

# my_al_list = ['hi'] # replace the code to the left
print(f"The meanings in the dictionary are {my_al_list}")