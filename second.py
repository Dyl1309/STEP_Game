while True:
	num1 = float(input("Enter the first number: "))
	operator = input("Enter an operator (+,-,*,/): ")
	num2 = float(input("Enter the second numer: "))

	if operator == "+" :
		print(num1+num2)
	elif operator == "-":
		print(num1-num2)
	elif operator == "*":
		print(num1*num2)
	elif operator == "/":
		if(num2==0):
			print("Can't divide by a zero")
		else:
			print(num1/num2)
	else:
		print("Invalid operator. Please try again.")