n = int(input("Enter a number:  "))
rev_num = 0

while n != 0:
    dig = n%10
    rev_num = rev_num*10 + dig
    n = n//10
print("Reversed of the number: ", rev_num)
