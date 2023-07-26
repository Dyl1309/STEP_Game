num1 = int(input("INPUT NUMBER 1 : "))
num2 = int(input("INPUT NUMBER 2 : "))
num3 = int(input("INPUT NUMBER 3 : "))
if num1 > num2 and num1 > num3:
    print(str(num1)+ " IS THE GREATEST")
    if num2 > num3:
        print(str(num2)+ " IS THE MEDIAN")
        print(str(num3)+ " IS THE least")
    else:
        print(str(num3)+ " IS THE MEDIAN")
        print(str(num2)+ " IS THE least")
if num2 > num1 and num2 > num3:
    print(str(num2)+ " IS THE GREATEST")
    if num1 > num3:
        print(str(num1)+ " IS THE MEDIAN")
        print(str(num3)+ " IS THE least")
    else:
        print(str(num3)+ " IS THE MEDIAN")
        print(str(num1)+ " IS THE least")
if num3 > num2 and num3 > num1:
    print(str(num3)+ " IS THE GREATEST")
    if num2 > num1:
        print(str(num2)+ " IS THE MEDIAN")
        print(str(num1)+ " IS THE least")
    else:
        print(str(num2)+ " IS THE MEDIAN")
        print(str(num1)+ " IS THE least")

