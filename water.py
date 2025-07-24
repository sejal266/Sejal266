total_bottles = int(input("enter the number of bottles:"))
per_day=int(input("enter the bottles number drink per day"))
day=1
while total_bottles > 0:
    if total_bottles >=per_day:
        print(f"Day{day}:drink{per_day} bottles.{total_bottles_per_day}left.")
        total_bottles=per_day

    else:
        print(f"Day{day}:drank{total_bottles bottle{'s' if total_bottles > 1 else ''}.0 left.")
        total_bottles=0
        day+=1
        print("No more bottles left now")