import times

first = input("Enter a number with less than 7 digits.")
l1 = len(first)
second = input("Enter another number with less than " + str(8-l1) + " 
digits.")
l2 = len(second)
if l1 > l2:
    n = l1
    m = l2
else:
    first, second = second, first
    n = l2
    m = l1

prod = ("0")*(m+n)

while int(second) is not 0:
    second, prod = times.multiply(first, second, prod, n, m)
