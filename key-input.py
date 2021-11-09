'''import keyboard

running =True
price=""

while running:
	if keyboard.is_pressed("1"):
		price+="1"
	if keyboard.is_pressed("2"):
		price+="2"
	if keyboard.is_pressed("3"):
		price+="3"
	if keyboard.is_pressed("4"):
		price+="4"
	if keyboard.is_pressed("5"):
		price+="5"
	if keyboard.is_pressed("6"):
		price+="6"
	if keyboard.is_pressed("7"):
		price+="7"
	if keyboard.is_pressed("8"):
		price+="8"
	if keyboard.is_pressed("9"):
		price+="9"
	if keyboard.is_pressed("0"):
		price+="0"
	if keyboard.is_pressed("Enter"):
		running=False

subtotal=int(price)
print(subtotal)
subtotal=float(subtotal)/100

print("Subtotal: {}".format(subtotal))'''

import keyboard
from functools import partial 

num = ""

def add(i):
	global num
	num += str(i)
	print(num, end='\r')

for i in range(10): # numbers 0...9
	keyboard.add_hotkey(str(i),partial(add, i)) # add hotkeys
	#keyboard.add_hotkey(str(i),add(i))

keyboard.wait('enter') # block process until "ENTER" is pressed

subtotal=int(num)
subtotal=float(subtotal)/100
print("Subtotal: {}".format(subtotal))
#print("\nNum:{}".format(num))