def list_creator(max_val, inc):
	i = 0
	numbers = []

	while i < max_val:
		print "At the top i is %d" % i
		numbers.append(i)

		i += inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d\n" % i


	print "The numbers: "

	for num in numbers:
		print num

list_creator(10,1)