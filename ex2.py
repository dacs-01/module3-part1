from typing import Counter


def combine_dict(dict1,dict2):
    comb_dict = {} 
    for i, j in dict1.items(): # iterates over all keys and values of first dict
        for x, y in dict2.items(): # iterates over all keys and values of second dict
            if i == x: # if the keys of first and second dicts match
                comb_dict[i] = (j+y) # add the values together and add them to new combined dict
    return comb_dict 


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combination = combine_dict(my_dict_1,my_dict_2)
print(combination)
