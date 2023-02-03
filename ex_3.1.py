# exercise 3 sandboxfrom collections import Counter
from collections import Counter

# stupid counter takes an array as input

buckets = [ ('john.doe@example.com',{'first_name':'john','last_name':'doe'}),
            ('jane.doe@example.com',{'first_name':'jane','last_name':'doe'}),
            ('derek.zoo@example.com',{'first_name':'derek','last_name':'zoolander'}),
            ('murph.cooper@example.com',{'first_name':'murph','last_name':'cooper'}),
            ('ned.stark@example.com',{'first_name':'ned','last_name':'stark'})
            ]
            
# i = 0
# a = buckets [0][1]['last_name']
# b = []
list_of_last_names = []
cnt = Counter()

for item in buckets :
   email, full_name = item
   list_of_last_names.append(full_name['last_name'])
   
cnt = Counter(list_of_last_names)
print (cnt)
#print (list_of_last_names)

# for i, word in buckets [i][1]['last_name'] :
#    cnt = cnt + 1

