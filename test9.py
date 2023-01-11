name= input("Please enter your first name:")
family= input("Please enter your family name:")
course1= float(input("Please enter your first course's grade:"))
course2= float(input("Please enter your second course's grade:"))
course3= float(input("Please enter your third course's grade:"))
average= (course1+course2+course3)/3

if average>=17:
    result= ("Great.")
if 12<=average and average<17:
    result= ("Normal.")
if average<12:
    result= ("Fail.")

print("The student's name is", name, family, "and her/his status is", result)