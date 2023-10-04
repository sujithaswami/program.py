hno = (input("enter a h-no"))
pincode = (input("enter  a pin"))
state = (input("Enter a state"))
street = input("enter a street name")
if (hno.isnumeric()):
        print("address is valid")
elif (hno.isalpha()):
        print("hno should be a number")
elif not(pincode.isnumeric() and len(pincode))== 6:
        print("pincode should be number must be 6 digits")
elif (state.isalpha() and street.isalpha()):
        print("address is valid")

else:
        print("address is not valid")