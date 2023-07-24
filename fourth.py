default = "Password1234"
attempt = 3
while True:
	password = (input("ENTER PASSWORD:"))
	if password == default:
		print("CORRECT")
		break
	else:
		attempt-=1
		print("INCORRECT. TRIES REMAINING -  "+str(attempt))
		
		if attempt ==0:
			print("ACCESS REVOKED. PLEASE TRY AGAIN LATER")
			break

