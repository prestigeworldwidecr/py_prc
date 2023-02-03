from random import randint

my_list = [1,2,3,4,5]
my_tuple = tuple(my_list)

# Question 6: What are the last 3 values of my_tuple?
# range(
# s = string(1)
# my_tuple_last_val =  my_tuple[4: 3: -1]# replace the code to the left ## these leaves a tuple as a result
my_tuple_last_val = my_tuple[-1]
# print (my_tuple_last_val)
# my_tuple_sec_last_val = my_tuple[3: 2: -1] # replace the code to the left
my_tuple_sec_last_val = my_tuple[-2]
# print(my_tuple_sec_last_val)
# my_tuple_third_last_val = my_tuple[2: 1: -1] # replace the code to the left
my_tuple_third_last_val = my_tuple[-3]
print(f"The last 3 values of the tuple are {(my_tuple_third_last_val,my_tuple_sec_last_val,my_tuple_last_val)}")
print('-'*40)
print()