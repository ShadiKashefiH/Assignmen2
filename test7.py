import math

a= int(input("Please enter a:"))
b= int(input("Please enter b:"))
op= input("choose the operation:")

if op=="+":
    result= a+b

if op=="-":
    result= a-b

if op=="*":
    result= a*b

if op=="/":
    if b==0:
        print("Error")
    else:
        result= a/b

if op== "radical":
    result= math.sqrt(a)

if op== "sin":
    result= math.sin(a)

if op== "cos":
    result= math.cos(a)

if op=="tan":
    result= math.tan(a)

if op== "factorial":
    result= math.factorial(a)

if op== "cot":
    result= math.cos(a)/math.sin(a)

print(result)