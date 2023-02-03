## test1.py

def palCheck(pal, l, r) :
    print ('l: ', l, ' r: ', r)

    if (l > r) :
        return True

    elif (pal[l] != pal[r]) :
        return False    
    
    else :
        # print (r)
        return palCheck(pal, l + 1, r - 1)


pals = ['rotator', 'rot', 'racecar', 'bib', 'pizza']
# tmp = pals[0]

for i in range(len(pals)) :
    isPalindrome = palCheck(pals[i], 0, len(pals[i]) - 1)
    print (isPalindrome)

# isPalindrome = palCheck(pals[1], 0, len(pals[1]) - 1)
# print (isPalindrome)