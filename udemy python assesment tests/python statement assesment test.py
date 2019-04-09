#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for x in st.split():
    if x[0]=='s':
        print(x)
print(' ')

#Use range() to print all the even numbers from 0 to 10.
for x in range(0,11):
    if x%2==0:
        print(x)
print(' ')

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
my_list=[x if x % 3 == 0 else ' ' for x in range(0,51)]
print(my_list)
print(' ')

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
    if len(x)%2==0:
        print(x)
print(' ')

#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
new_list=[]
index=0
for x in st.split():
    for letter in x:
        new_list+=letter[index]
        break
   
print(new_list)











 
    
