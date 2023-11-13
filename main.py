from random import randrange
import time
number=1
while number<=1000:
    a=str(input("Welcome to the 8-ball-program \nEnter your question\n"))
    b=randrange(0,2)
    if(b==0):
        print("Yes")
    else:
        print("No")    
    number+=1    
    time.sleep(3)
else:
    print('1000 questions over! Re-run the program for more!')    