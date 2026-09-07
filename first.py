#file handling
# mode === r,w,a,

#open file
file=open('example.txt','r')

# read file
'''
file=open('example.txt','r')
content =file.read()# read () reads entire content of file
print(content)
file.close()


file=open('example.txt','r')
content =file.readline() # read first line
print(content)
file.close()


file=open('example.txt','r')
content =file.readlines() # reads all content into list formate= output is in []
print(content)
file.close()

'''

# write to file
file =open('example2.txt','w')  # if file is not existing it will create file (only happens when you use w as mode)
file.write("namste,kaise ho?")  # this will write to file (if file already has content it will delete existing content and write new content)
file.close()

# append to file
file=open("example2.txt",'a')
file.write("\n i am fine broo") # appends to the file (doesnot delete existing content ,add content at end )
file.close()


# closing of file
#. 2 mathod=== 1.close fucntion  2.with statement

with open('example2.txt','r') as file:
    contnet =file.read()
    print(contnet)
    