largest = None
smallest = None
while True:
    num = input("Enter a number or 'done' for end: ")
    if num == "done":
        break
    try:
        num = float(num)

        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num
    except:
         print('Invalid input')
if largest is not None and smallest is not None:
    print("Maximum", largest)
    print("Minimum", smallest)
else:
    print ('no valid input entered')
