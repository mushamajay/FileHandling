with open('filetest11.txt') as fh1, open('test.txt') as fh2:  
    for l1, l2 in zip(f1, f2):  
        # l1 from filetest11.txt, l2 from test.txt 
        print(l1+l2)  
