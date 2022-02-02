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
        integer = int(val) # converts string into int
        count += 1 # increment counter each successful time
    except ValueError:
        print('Please enter an integer')
        continue # will make user retry if failed
    else:
        list.append(integer) # adds integer to list

print(sum(list)) # prints sum of list
