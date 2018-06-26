number1 = int(input('Enter the first number '))
number2 = int(input('Enter the second number '))
number3 = 0

number3 = number1 + number2
print("In the line 1  - Value of number3 is ", number3, " assigning operator =")

number3 += number1
print("In the line 2 - Value of number3 is ", number3, " assigning operator +=")

number3 -= number1
print("In the line 3 - Value of number3 is ", number3, " assigning operator -=")

number3 *= number1
print("In the line 4 - Value of number3 is ", number3, " assigning operator *=")

number3 /= number1
print("In the line 5 - Value of number3 is ", number3, " assigning operator /=")

number3 = 2
number3 %= number1
print("In the line 6 - Value of number3 is ", number3, " assigning operator %=")
