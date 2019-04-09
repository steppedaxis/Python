string=input('please enter a string ')
new_string=''

for x in string:
    new_string=x+new_string
print('new string is {}'.format(new_string))

if new_string==string:
    print('palindrome')
else:
    print('not palindrome')

