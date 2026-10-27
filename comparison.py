# age=int(input("What is the age of the children? "))

# if age>=10 and age<=15:
#     print("The children are allowed to go on the rides.")

# else:
#     print("The children are not allowed to go on the rides")


user=int(input("Enter a day: \nMonday-1\nTuesday-2\nWednesday-3\nThursday-4\nFriday-5\nSaturday-6\nSunday-7 "))

if user==6 or user==7:
    print("It is a weekend.")

else:
    print("It is a weekday.")
