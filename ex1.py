# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This program will take a hardcoded list and put every number, recurring or 
# non-recurring, into another new list. In this new list, it will contain one of 
# each of all numbers in the original list, making it a unique list.


def unique_el(nums):
    list = []
    for i in nums: # iterates thru inputted list
        if i not in list: # if the number is not in new list already...
            list.append(i) # ...add it to the new list
    return list # return the new list

my_list = [1,2,3,4,4,5,3,-5,-6,-6]

uni_el = unique_el(my_list)
print(uni_el)


