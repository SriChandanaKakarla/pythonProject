a = int(input("Enter num1: "))
b= int(input("Enter num2: "))
print("1. + \n 2. - \n 3. * \n 4. / \n")
ch = input("Enter operation +,-,*,/ : ")
c = 0
if ch == '+':
    c = a + b
elif ch == '-':
    c = a - b
elif ch == '*':
    c = a * b
elif ch == '/':
    c = a / b
else:
    print("enter correct data")
print(a,ch,b, ":", c)