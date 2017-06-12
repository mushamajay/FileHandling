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


wordstring = 'it was the best of times it was the worst of times '

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))
 
'''

'''
#9
string=raw_input("user, enter here:\n")
wordlist=string.split()

wordfreq=[]
for w in wordlist:
  wordfreq.append(wordlist.count(w))
print ("pairs\n" +str(zip(wordlist,wordfreq)))

'''
#9

'''
from collections import Counter 
     with open("filetest11.txt","r") as f:  
          return Counter(f.read().split())  
print("Number of words in the file :",word_count("filetest11.txt"))  
'''
