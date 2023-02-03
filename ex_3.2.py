# exercise 3 sandboxfrom collections import Counter
from collections import Counter

# stupid counter takes an array as input

buckets = [ ('john.doe@example.com',{'first_name':'john','last_name':'doe'}),
            ('jane.doe@example.com',{'first_name':'jane','last_name':'doe'}),
            ('derek.zoo@example.com',{'first_name':'derek','last_name':'zoolander'}),
            ('murph.cooper@example.com',{'first_name':'murph','last_name':'cooper'}),
            ('ned.stark@example.com',{'first_name':'ned','last_name':'stark'})
            ]

# Question 2: Create a function that compares first and last names of records
# given the email address, first and last names to compare. Exact matches only,
# ignore case. Return True if exact match, return False otherwise.

# def compare_full_name(list_of_records, email, first_name, last_name):
email = 'ned.stark@example.com'
first_name = 'ned'
last_name = 'stark'

for item in buckets :
    buckets_email, full_name = item
    # first_name = full_name['first_name']
    # first_name = full_name['first_name']
    if (email == buckets_email and first_name == full_name['first_name'] and last_name == full_name['last_name']) :
        print("true")
    else :
        5 #keep going
        
print("false")