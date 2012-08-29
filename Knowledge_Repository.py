
print "Hello World"
print "Hey %s there." % "you" #format string (single)
print "I have %s hair and %s eyes." % ("brown", "black") #format string (multiple)
print "I am %d years old." % 29 #format number (single)
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight) #format number (multiple)
print "I have %r hair and %d eyes." % ("brown", 2) # %r prints anything

print "Jan\nFeb\nMar" # will print Feb and Mar on new lines

print """
Allows you to print multiple lines
Like these ones
"""

""" also called documentation comments - shows up in help (function) """

print "\t" produces an indent
print "\n" produces a new line
print "\\" produces a backslash
print "\r" produces a carriage return (return to front of line)
print "\b" produces a backspace

# comments are prefaced by 'hash' / 'octothorpe' / 'mesh' / 'pound' / 'oxgrid'

# MATH OPERATORS
+ plus
- minus
/ divide without remainder (for integers)
* asterisk
% modulus

= Assignment OPERATOR

# COMPARING
< less-than
> greater-than
<= less-than-equal
>= greater-than-equal
== equal

# FUNCTIONS
round() eg. round(1.7333) rounds the number down
raw_input() gets a str input from the user. can include a prompt between the brackets
int(raw_input()) tries to get integer input

# FUNCTIONS CHECKLISTS
Did you start your function definition with def?
Does your function name have only characters and _ (underscore) characters?
Did you put an open parenthesis ( right after the function name?
Did you put your arguments after the parenthesis ( separated by commas?
Did you make each argument unique (meaning no duplicated names).
Did you put a close parenthesis and a colon ): after the arguments?
Did you indent all lines of code you want in the function 4 spaces? No more, no less.
Did you "end" your function by going back to writing with no indent (dedenting we call it)?

And when you run ("use" or "call") a function, check these things:

	Did you call/use/run this function by typing its name?
	Did you put ( character after the name to run it?
	Did you put the values you want into the parenthesis separated by commas?
	Did you end the function call with a ) character?



# FILE METHODS
.close
.read
.readline
.truncate
.write(stuff)


#LOGIC OPERATORS
and
or
not
!= (not equal) / also <>
== (equal)
>  (greater-than)
<  (less-than)
>= (greater-than-equal)
<= (less-than-equal)
True
False

