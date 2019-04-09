
#קלוט מהמשתמש מספר
#אם המספר בן ספרה יש להדפיס את הסיפרה במילה
#אם המספר בן 2 ספרות יש להדפיס הודעה מתאימה ואת סכום הספרות
#אם המספר בן 3 ספרות יש להדפיס הודעה מתאימה ואת מכפלת הספרות
#אחרת - הדפס הודעה שהמספר גדול מ3 ספרות


my_dict={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
user_input=int(input('please enter a number '))
sum_digits=0
if user_input>=1 and user_input<=9:
    print('your number has 1 digit')
    for key in my_dict:
        if user_input==key:
            print(my_dict.get(key))
elif user_input>=10 and user_input<=99:
    print('number has 2 digits')
    while user_input!=0:
        digit=int(user_input%10)
        sum_digits+=digit
        user_input/=10
    print(sum_digits)
elif user_input>=100 and user_input<=999:
    print('number has 3 digits')
    while user_input!=0:
        digit=int(user_input%10)
        sum_digits+=digit
        user_input/=10
    print(sum_digits)
elif user_input>=1000:
    print('number has more then 3 digits')


    
    

        


