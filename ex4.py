# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This program will get the sum of 5 inputted ints, if inputted correctly.
# Otherwise, the program will prompt the user to re-enter an int at the 
# same index until the counter hits 5.

list = []
count = 0
while(count < 5):
    val = input('Enter int #' + str(count+1) + ': ')
    try:
        integer = int(val)
        count += 1
    except ValueError:
        print('Please enter an integer')
        continue
    else:
        list.append(integer)

print(sum(list))
