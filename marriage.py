gender=input("enter gender(boy/girl):")
age=int(input("enter age:"))
if gender =="boy":
    if age>=21:
        print("boy is eligible for marriage")
    else:
        print("boy is not eligible for marriage")
elif gender == "girl":
    if age >=18:
        print("girl is eligible for marriage")
    else:
        print("girl is not eligible for marriage")