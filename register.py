import keyboard

print("Modes:\nAdd: 1\nSubtract: 2\nSubtotal: 3\nComplete Sale (Only after getting the subtotal): 4")
subtotal=0.00
flag=False
canComplete=False
while not flag:
	mode=int(input("Mode: "))
	if mode == 1:
		price=input("$")
		subtotal+=float(price)
		canComplete=False
	elif mode==2:
		price=input("$")
		subtotal-=float(price)
		canComplete=False
	elif mode==3:
		form="${:,.2f}".format(subtotal)
		print("Subtotal: {}".format(form))
		canComplete=True
	elif mode==4 and canComplete:
		moneyGiven=input("$")
		change=float(moneyGiven)-subtotal
		flag=True
		changeForm="${:,.2f}".format(change)
	else:
		if mode==4:
			print ("You must obtain the subtotal before completing a sale.")
		else:
			print("Error!")
print("Change: {}".format(changeForm))
input("Press any key to exit")
