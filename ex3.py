from collections import Counter


string = input('Enter a string: ')
result = Counter(string.lower().replace(' ',''))
print(result)