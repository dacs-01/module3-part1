# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.


def unique_el(nums):
    list = []
    for i in nums:
        if i not in list:
            list.append(i)
    return list

my_list = [1,2,3,4,4,5,3,-5,-6,-6]

uni_el = unique_el(my_list)
print(uni_el)


