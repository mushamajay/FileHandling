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

def file_read(fname):
  content_array=[]
  with open(fname) as f:
    for line in f:
      content_array.append(line)
      print (content_array)
      
file_read('filetest11.txt')
'''
'''
#7
def file_read(fname):
  content_array=[]
  with open(fname) as f:
    for line in f:
      content_array.append(line)
      v=content_array
      print v
      
file_read('filetest11.txt')
'''
