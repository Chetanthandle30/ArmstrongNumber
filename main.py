# To check if a number is armstrong without using power function
def armstrong(n):
    s = n
    power = len(str(n))
    sum1 = 0
    while n != 0:
        rem = n % 10
        sum1 = sum1 + rem ** power
        n = n // 10
    if s == sum1:
        return print(s, "is a armstrong number")
    else:
        return print(s, "is not a armstrong number")


number = int(input("Enter the number to check if it is a armstrong or not- "))
armstrong(number)
