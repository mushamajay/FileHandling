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

f=open("filetest11.txt","r")
f1=open("filetest11.txt","r")
print(f.closed)
f.close()
print(f1.closed)
f1.close()
print(f.closed)
print(f1.closed)

 
 
