### Part Three -- your code goes here. 
numbers = [3, 1, 8, 1, 5, 9, 2, 6, 5, 3]      ### List of numbers
numbers.sort()                                ### Numbers sorted in order
while 1 in numbers:                           ### Loop while value 1 in numbers
    numbers.remove(1)                         ### removes value 1 from numbers
numbers.extend([7,8])                         ### Adds the numbers 7 and 8 to the end of the list (now we have numbers that are not sorted at the end)
print(numbers)                                ### Prints Result with values 1 gone and 7 and 8 added at the end
