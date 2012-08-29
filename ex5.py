name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "He weighs %d kilograms." % (weight / 2.2)
print "Actually tha's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "I have %s hair and %r eyes." % ("brown", "black")
print "I am %r years old." % 29