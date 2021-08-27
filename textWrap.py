
import textwrap

def textWrap (f_text, f_width):
	return textwrap.fill (f_text, f_width)			# fill method of the textwrap module return the devided elements line by line

text, max_width = input (), int (input ())

print (textWrap (text, max_width))