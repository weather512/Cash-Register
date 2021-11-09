import keyboard
from functools import partial

num=""
subtotal=0.00
under=False
index=0
departments=[]
numDepartments=0

while not under:
	numDepartments=int(input("Number of departments (maximum is 26): "))
	if numDepartments>0 and numDepartments<=26:
		under=True

letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

def type(i):
	global num
	num+=str(i)
	print(num,end='\r')

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
	#print("Hi")

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

def getSubtotal():
	print("Subtotal: {}".format(subtotal))

for i in range(10):
	keyboard.add_hotkey(str(i),partial(type,i))

keyboard.add_hotkey('+',add)
keyboard.add_hotkey('-',subtract)
keyboard.add_hotkey('=',getSubtotal)

keyboard.wait('esc')
