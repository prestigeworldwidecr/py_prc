from random import randint

# Question 1: Use list comprehension to update the code below and
# assign my_list to be a list of 200 random integers ranging in values
# between 25 and 500. Hint: Use the randint function
my_list = [1,2,3,4,5] # replace the code to the left
c_list = [randint(25, 501) for num in range(25, 501)]

# my_list = [randint(25, 501) for num 

# for num in range(25, 501) :
#    c_list.append(randint(25, 501))

print (c_list)