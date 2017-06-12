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

u_input=raw_input("user, enter here :\n ")
longest=0
for word in u_input.split():
  if len(word)>longest:
    longest=len(word)
    longest_word=word
    
print ('The longest word is %s' %longest_word)  
