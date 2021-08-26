from random import randrange
import time
from time import sleep
number=1
while number<=1000:
    a=str(input("Welcome to YAG's 8 ball \nEnter your question\n"))
    b=randrange(0,2)
    if(b==0):
        print("Yes")
    else:
        print("No")    
    number+=1    
    time.sleep(3)
else:
    print('rip')    


        