import keyboard
from functools import partial

num=""
subtotal=0.00
under=False
index=0
departments=[]
numDepartments=0
canComplete=False

while not under:
	numDepartments=int(input("Number of departments (maximum is 26): "))
	if numDepartments>0 and numDepartments<=26:
		under=True

letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
lettersX=[]

def add():
	global subtotal
	global num
	if num=="":
		price=0
	else:
		price=int(num)
	subtotal+=(price/100)
	num=""
	print("\n")

while index<numDepartments:
	lettersX.append(letters[index])
	index+=1

for x in lettersX:
	dep=input("Enter the department for '{}': ".format(x))
	departments.append(dep)
	keyboard.add_hotkey(x,add)


def type(i):
	global num
	num+=str(i)
	print(num,end='\r')

def subtract():
	global subtotal
	global num
	if num=="":
		price=0
	else:
		price=int(num)
	subtotal-=(price/100)
	num=""
	print("\n")
	canComplete=False

def getSubtotal():
	global canComplete
	form="${:,.2f}".format(subtotal)
	print("Subtotal: {}".format(form))
	print("Before: {}".format(canComplete))
	canComplete=True
	print("After: {}".format(canComplete))

def complete():
	global subtotal
	global num
	if canComplete:
		if num=="":
			moneyGiven=0
		else:
			moneyGiven=int(num)
		moneyGiven=float(moneyGiven/100)			
		change=moneyGiven-subtotal
		changeForm="${:,.2f}".format(change)
		print("Change {}".format(changeForm))
	else:
		print("You must obtain the subtotal before completing a sale. Input money again.\n")
		num=""

for i in range(10):
	keyboard.add_hotkey(str(i),partial(type,i))

keyboard.add_hotkey('-',subtract)
keyboard.add_hotkey('=',getSubtotal)
keyboard.add_hotkey('enter',complete)

keyboard.wait('esc')