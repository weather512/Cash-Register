for i in range(10):
	keyboard.add_hotkey(str(i),partial(type,i))

keyboard.add_hotkey('+',add)
keyboard.add_hotkey('-',subtract)
keyboard.add_hotkey('=',getSubtotal)

keyboard.wait('esc')