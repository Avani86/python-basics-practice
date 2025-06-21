# Palindrome Checker 

n = int(input("Enter a number:  "))
original_no  = n 

rev = 0
while n != 0:
    dig = n%10
    rev = rev*10 + dig
    n = n//10
    
if original_no == rev:
    print("It is a Palindrome Number")
else:
    print("It is a Palindrome Number")
