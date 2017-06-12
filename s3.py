file=open("filetest11.txt","w+") 

file.write("Hello potti\n") 
file.write("hello Ajay\n") 
file.write("Musham\n")
file.write("hello patil\n") 
file.write("patil\n")
file.write("skanjaj\n") 
file.write("sahshha\n")
file.write("sdfsfsdfsffdA\n") 
file.write("bhjasak\n")
file.write("username\n") 
file.write("mushamajay   \n") 

with open("filetest11","a") as myfile:
  myfile.write("This line is an appending line")
print myfile


'''
file=open("filetest11.txt","a")
file.write("This line is an appending line")
file=open("filetest11.txt","r")
str=file.read()
print str
file.close()
'''
