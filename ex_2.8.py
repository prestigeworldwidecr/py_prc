import random

# Question 8: Does the first value of my_new_tuple match my_tuple_last_val?
my_new_tuple = (5,4,3,2,1) # replace the code to the left
my_tuple_last_val = my_new_tuple[-1]
# my_new_tuple = my_new_tuple[-1: -6: -1]

# Enter in the conditional below that will evaluate to True or False
# if  (my_new_tuple[0] == my_tuple_last_val):
#    comparison = True
# else:
#     comparison = False # replace the code to the left

comparison = (my_new_tuple[0] == my_tuple_last_val)

print(f"First integer of my_tuple matches last integer of my_new_tuple is a {comparison} statement")
print('-'*40)
print()