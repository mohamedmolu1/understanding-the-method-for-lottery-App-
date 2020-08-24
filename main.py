# we are going to look at how to use the split method, in order to get multiple data points at the same time. 

# Lists are collection of items 

user_input = "1,2,3,3,3,3,4,5,6"
user_numbers = user_input.split(",")
print(user_numbers)

# The append is going to add another value to the list

user_numbers_as_int = []
for number in user_numbers:
  user_numbers_as_int.append(int(number))

# This method below is a simpler method which also converts the string numbers into integer

print([int(number) for number in user_numbers])

# we are going to look at sets, 

# its vey similar to lists however python works the both differently. 
numbers = [1,2,3,3,3,3,4,5]
numbers = set()
numbers.add(3)

# while loop is something that help the code print out a list of numbers no matter if they are duplicate or not. 