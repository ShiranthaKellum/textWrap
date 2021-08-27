
import textwrap

def textWrap (fText, fWidth):
    wrappedList = textwrap.wrap(fText, fWidth)
    for i in wrappedList:
        print (i)

text, max_width = input (), int (input ())

textWrap (text, max_width)
