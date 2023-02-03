# exercise 3 sandboxfrom collections import Counter
from collections import Counter

# stupid counter takes an array as input

buckets = [ ('john.doe@example.com',{'first_name':'john','last_name':'doe'}),
            ('jane.doe@example.com',{'first_name':'jane','last_name':'doe'}),
            ('derek.zoo@example.com',{'first_name':'derek','last_name':'zoolander'}),
            ('murph.cooper@example.com',{'first_name':'murph','last_name':'cooper'}),
            ('ned.stark@example.com',{'first_name':'ned','last_name':'stark'})
            ]

# (CHALLENGE) Question 3: Create a function that can reset the value for first_name
# and last_name for a record found with a specific email address
# while leaving the rest of the list unchanged, if the email address
# does not exist, then append a new record to the list with the new email
# address, first name and last name.
# Hint: Solutions use the enumerate function to track index of a record.
# def update_record(list_of_records, email, first_name, last_name):
    # """
    # fill in docstring
    # """
    ## Write code below ##
    # pass
    ## end of function ##
    
email = 'nbd.stark@example.com'
first_name = 'ned'
last_name = 'stark'
reset_first_name = 'Cam'
reset_last_name = 'Newton'
j = 0 # index of matched record
found = False

# can't change the items of a tuple but since its wrapped in an array, just replace the entire entry

for i, item in enumerate(buckets) :
    buckets_email, full_name = item
    # print(buckets_email)
    
    if (email == buckets_email) :
        found = True
        j = i
        # buckets[i]['first_name'].set(reset_first_name)
        # buckets[i]['last_name'].set(reset_last_name)
        # print (item)
    else :
        5 # thats my do nothing else statement
        
if (found == True) :
    buckets [j] = (email, {'first_name': reset_first_name, 'last_name' : reset_last_name})
    print (buckets[j])
    
else :
    buckets.append((email, {'first_name': reset_first_name, 'last_name' : reset_last_name}))