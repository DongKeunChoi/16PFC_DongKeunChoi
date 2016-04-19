from sys import argv

script, filename = argv

txt=open(filename)

print ("Here's your file %r" % filename)
print (txt.read())

raw_input ("Type the filename again:"  )

txt=open(filename)
print (txt.read())
