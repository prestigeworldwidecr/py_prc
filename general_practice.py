from random import randint
# first comment in Python

# import string
# from string import ascii_lowercase

my_Message = "eat ass1"
other_Message = 'eat ass2'
thirdMsg = "012345"

# print("eat ass")

# print(my_Message)
# print(other_Message)

# thirdMsg[-4] = '%%'
other_Message = "%"
# print(thirdMsg[2:5:2])
# print(capitalize(my_Message))

# len() length of string
# type() what type of object
# id the address
# dir provides all possible methods you cal apply to the object
# can chain methods .strip().lower()

# lists...



# print(other_Message, 12)

# {} curly braces are placeholder

# print("butthole {}".format(my_Message))

# print(my_Message*30)

fLis = [1, "4", other_Message]

# print(first_List)

# first Dictionary

fDic = {1 : "taco", 3 : "pizza"}

# print(first_Dictionary["hello"])

# set
fSet = {1, "4", other_Message, 7, 9}
sSet = {1, "4", other_Message, "why not?"}
# sets dump duplicates
# no indexing, no order

# tuple
fTup = (1, "4", other_Message)
sTup = (1, "4", 5, "why not?")
# cant change the elements

# print(first_Tuple[2 :0 : -1])

# in, index, sort, sorted... differences between methods and functions

# foober = [9, "pizza", "saints suck"]
# print(foober)

# for k, v in first_Dictionary.items() :
#    print(k, v)

# print("In BOTH", fSet.intersection(sSet))
# print("In ALL", fSet.union(sSet))
# print("Not in Common", fSet.difference(sSet))
sum = 0
num_list = [3, 3, 0, 2, 9, 10]

# for item in num_list :
#     sum  = item + sum
    
# print(sum)

# range() is a generator, has its own type
# range is almost same as [ : : ]

# generate random numebrs 1 to 100
# l = []
# l.append("string")

# print[0]
# print(type(l))

# i was gonna craete a list from 5-100, then turn it into a set

# you can generate an entire list with a loop on generation

# for i in range(5, 100) :
#    l.append(randint(3, 100))

# l = [num for num in range(1, 100)]
# s = {1, 2, "taco", 4, 6, 8}
    
# print(s)

# can replace with item for append in front of for loop within assignment!!
# choice() selects a random object

## while loops
## 
i = 0
# li = [randint(1,1000) for num in range(1, 1000)]
# print(li.index(1000))
search = 25

# print (len(li))
# print (search)

# while (i < len(li)):
    # print(li[i])
#    if (li[i] == search):
#        print(f"number: ", {search},  "index: ", {i})
#    i = i + 1
    
# print(len(li))
# print(float(str((enumerate(li,4)))))
# generator functions enumerate turns your tuple into enumerate
# you can specify a start value alomg the object and you can iterate on it
#zip
l1 = ['balls', 'ass', 'needle']
l2 = ['steroid', 'cake', 'plant']

# tupled_list = zip(l2, l1)
# print(list(tupled_list))


def first_function():
    """
    People throw function descriptions in here
    """
    print("hi")
 # else:
 
 
first_function()
    #    i = i + 1
    # print("balls ", i)
    # 
    #else:
        
        # print(i)
    
# 1000 random numbers in list