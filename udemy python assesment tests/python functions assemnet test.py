#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    for x in range(low,high):
        if num==x:
            return True
    return False        

status=ran_check(5,6,7)
print(status)
print(' ')

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def uppercase_and_lowercase(my_string):
    upper=0
    lower=0
    for x in my_string:
        if x.islower():
            lower+=1
        elif x.isupper():
            upper+=1
    print('upper case: {}'.format(upper))
    print('lower case: {}'.format(lower))

mystring='Hello Mr. Rogers, how are you this fine Tuesday?'
uppercase_and_lowercase(mystring)
print(' ')

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(mylist):
    newlist=set(mylist)
    newlist=list(newlist)
    print(newlist)
    
mylist= [1,1,1,1,2,2,3,3,3,3,4,5]
unique_list(mylist)
print(' ')

#Write a Python function to multiply all the numbers in a list.
def multiply_list(multilist):
    multi=1
    for x in multilist:
        multi*=x
    print(multi)

my_multi_list=[1, 2, 3, -4]
multiply_list(my_multi_list)
print(' ')

#Write a Python function that checks whether a passed in string is palindrome or not.

def check_palindrome(my_string):
    new_string=''
    for x in my_string:
        new_string=x+new_string
    if new_string==my_string:
        print('palindrome')
    else:
        print('not palindrome')

mystring='helleh'
check_palindrome(mystring)












