import textwrap                                             # import  textwrap module

def wrapper (string, max_width):

    list = textwrap.wrap (string, max_width)        # wrap method in textwrap module, wrapes text in to given width element and return a list             

    for i in list:
        print (i)

text = input()
width = int(input())                                                        

wrapper (text, width)
