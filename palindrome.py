
#palindrome

def is_palindrome(num):
    temp=num
    rev=0
    digit=0
    while(num>0):
        digt=num%10
        rev=rev*10+digt
        num=num//10
    if(temp==rev):
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
num=int(input("Enter a number:"))
is_palindrome(num)
