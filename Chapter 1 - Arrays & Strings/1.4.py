#Palindrone Permutation

word = "civic"

palin = {}
isPalin = {'even' : 0, 'odd': 0}

word = word.replace(' ', '').lower()

for char in word:
	if char.isalnum():
		if char not in palin:
			palin[char] = 1
		else:
			palin[char] += 1

for key in palin:
	if palin[key] % 2 == 0:
		isPalin['even'] += 1
	else:
		isPalin['odd'] +=1

if (isPalin['even'] > 0 and isPalin['odd'] <= 1) or isPalin['odd'] == 1:
	print "Palindrome" 
else:
	print "Not Palindrome"