num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)
'''
The above code will output 34,damn why??
It's because whenever we're taking inputs in python by default it considers the 
input as string. That is why result = num1 + num2 actually concatenates the strings
The solution is typecasting the variables
'''
#result = int(num1) + int(num2)
print(result)

result = float(num1) + float(num2)
print(result)
