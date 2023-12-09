#2: DATA PREPARATION


#How to Add an Index Field Using Python

# Original list
original_list = ['apple', 'banana', 'orange', 'grape']

# Adding index starting from 1
indexed_list = list(enumerate(original_list, start=1))
'''
enumerate is a built-in function in Python that is used to iterate over a sequence 
(such as a list, tuple, or string) while keeping track of the index of the current item.'''

# Displaying the result
print(indexed_list)

# output [(1, 'apple'), (2, 'banana'), (3, 'orange'), (4, 'grape')]

