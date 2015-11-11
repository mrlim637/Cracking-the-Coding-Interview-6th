word = "hello"
alpha = {}
unique = True

for char in word:
	if char in alpha:
		unique = False
	else:
		alpha[char] = 1

if unique:
	print "Unique"
else:
	print "Not Unique"