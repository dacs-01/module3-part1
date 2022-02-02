# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This program takes a string input and returns the amount of each
# character that exists in the string, as well as removing white spaces
# from being counted and making all characters lowercase.

from collections import Counter


string = input('Enter a string: ')
result = Counter(string.lower().replace(' ',''))
print(result)
