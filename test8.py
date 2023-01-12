a= float(input("Please enter a="))
b= float(input("Please enter b="))
c= float(input("Please enter c="))

if a+b>c and a+c>b and b+c>a:
    result= print("It is a triangle.")
else:
    result= print("It is not a triangle.")

print(result)