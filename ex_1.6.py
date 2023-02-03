# Question 6: Use slicing notation to print the last 6 letters of the string
# below. Assume you donot know the start index or the length of the string upfront.
# Hint: You will need to use a function to find the length first and then use that,
# in combination with the number to come up with the start index
welcome_message = "Hello and welcome to the land of Python"

j = len(welcome_message)
i = j - 6

# print(len(welcome_message))
print(f"The last 6 letters of the welcome message:\n'{welcome_message}'\nare: '{welcome_message[i: j: ]}'")