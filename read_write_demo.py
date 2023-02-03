# file_name = "data.txt"
# first_name = "mashrur"
# last_name = "hossain"
# courses = ['python','ruby','javascript']

file_name = "data.txt"
# f = open(file_name)
# dont have to manage if we use context manager
# open by default only has reading permissions

with open(file_name, "a+") as f:

# (file_name "w", write, "a+", append, "r", read , "+", file doesnt exist, create it
# closes file and does cleanup
# f_contents = f.readline()
# f_contents = f.read()
# NO GOOD --> for item in f.readline()
    new_record = "joe,schmo:python,ruby,javascript"
    
    # for line in f:
        # print(line.strip())
        
    f.write(new_record + '\n')
    # write will replace entire file, will not append
    

#

# print(f_contents)
# f.close()