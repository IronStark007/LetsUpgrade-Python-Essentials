print("Hello,Pilot !!!")
alt =int(input("Enter the Altitude:"))
if alt <= 1000:
    print("Safe to land")
elif 5000 > alt > 1000:
    print("Bring down to 1000")
else:
    print("Turn Around")
print("Thank You,Pilot!!")
