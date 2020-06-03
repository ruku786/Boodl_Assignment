# Problem 2 :- Palindrom

reverse = 0
def integer_reverse(num):
    global reverse

    if (num > 0):
        reminder = num % 10
        reverse = (reverse * 10) + reminder
        integer_reverse(num // 10)
    return reverse


num = int(input("Enter a number:"))
rev = integer_reverse(num)

print("reverse of a given no. is= %d" % rev)

if (num == rev):
    print("%d is Palindrome" % num)
else:
    print("%d is not Palindrome" % num)
