Pin = 1234
attempts = 0

while attempts <= 3 :
	password = int(input("Enter your Pin"))
	if password == Pin :
		print("Login Successfully")
		print("="*40)
		print("\tMy name is mini Calculator")
		print("="*40)
		break
		
	attempts += 1
	print("Wrong Pin")
else :
	print("You are Blocked")
	
while True :
	num1 = float(input("Enter your Number"))
	operator = (input("Enter Your Operator : +,-,*,/"))
	num2 = float(input("Enter your Number"))
	
	if operator == '+' :
		print("Here is your Addition result")
		print(num1 + num2)
		print("Thanks For Using Calculator\n")
	elif operator == '-' :
		print("Here is your Substraction result")
		print(num1 - num2)
		print("Thanks For Using Calculator\n")
	elif operator == '*' :
		print("Here is your Multiplication result")
		print(num1 * num2)
		print("Thanks For Using Calculator\n")
	elif operator == '/' :
		if num2 == 0 :
			print("Not Divisible by Zero")
		else :
			print(num1 / num2)
			print("Thanks For Using Calculator\n")
	else :
		print("Wrong Operator ")
		print("Thanks For Using Calculator\n")
		break