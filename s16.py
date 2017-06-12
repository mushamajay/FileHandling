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

 
 

def remove_newline(fname):  
    list = open(fname).readlines()  
    return [s.rstrip('\n') for s in list]  
  
print(remove_newline("filetest11.txt"))  
