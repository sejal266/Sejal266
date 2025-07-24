bill amount=float(input("enter total_bill_amount"))
tip_percent=int(input("enter tip_percentage(10 to 50):"))
friends=int(input("enter the number of friends to split the bill"))
if tip_percent <10 or tip_percent >50:
    print("tip percent is between 10 and 50")
else:
    tip_amount=(tip_percent/100)*bill_amount
    total_bill=bill_amount+tip_amount
each_person=total_bill/friends
print("\n---bill sumarry---")
print(f"Bill amount:{bill_amount:.2f}")
print(f"Tip{tip_percent}%):{tip_amount:.2f}")
print(f"Total with tip:{total bill:.2f}")
printf(f"each person share:{each_person:.2f}")