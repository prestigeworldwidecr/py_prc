# branching improvement

# sort of like Case statement here
# just add the two other functions and be done w/it

print("Calculator")
print("-"*30)

msg = "1. Multiply \n\
2. Divide   \n\
3. Add      \n\
4. Subtract\n\
$ "

i = input (msg)
            
if (i == "1" or 
    i == "2" or 
    i == "3" or 
    i == "4"):
    
    num_1 = int(input("1# "))
    num_2 = int(input("2# "))
    
    if i == "1":
        print(f"Product of #1 and #2 is {num_1 * num_2}")
        
    elif i == "2":
        print(f"Quotient of #1 and #2 is {num_1 / num_2}")
    
    elif i == "3":
        print(f"Sum of #1 and #2 is {num_1 + num_2}")
    
    elif i == "4":
        print(f"Difference of #1 and #2 is {num_1 - num_2}")    
    
    else:
        i = -1
        
else:
    print("1-4...")
    