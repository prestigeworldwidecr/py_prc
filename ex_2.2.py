from random import randint

# Question 2 (4 parts): 

# Objective Cast my_list to a set and re-assign to my_list as a list.
my_list = [1,2,3,4,5]
my_list = list(set(my_list))

# 2 How many duplicate values were removed? 
0# 

initial_size = len(my_list) # replace the code to the left
print(f"Initial size of my_list: {initial_size}")

# 3 cast the list to a set to remove duplicates and re-assign to my_list as a list
my_list = list(set(my_list)) # replace the code to the left

final_size = len(my_list) # replace the code to the left

print(f"Final size of my_list after removing duplicates: {final_size}")

dups_removed = initial_size - final_size # replace the code to the left
print(f"Number of integers removed: {dups_removed}")
print('-'*40)
print()

## wtf was the point of that??