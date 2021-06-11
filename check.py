def six(string, int, char):
	if int < 0:
		return False
	elif int > len(string):
		return False
	elif string[int-1].lower() == char:
		return True
	else:
		return False

print(six("Hi-There", 10, "e"))