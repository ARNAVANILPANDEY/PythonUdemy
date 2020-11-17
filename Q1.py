
cp=0
cn=0
cz=0
sump=0
sumn=0

while(True):
    x=input("Enter a number")
    try:
        if(isinstance(x,str)):
           if(x.lower()=='done'):
               break
           else:
                test=int(x)
                if(test>0):
                    cp=cp+1
                    sump=sump+test

                elif(test<0):
                    cn=cn+1
                    sumn=sumn+test

                else:
                    cz=cz+1
                
    except:
        print("Invalid selection")
        



print("Number of positive={}\nNumber of negative={}\nNumber of zeroes={}\n Positive sum={}\nNegative sum={}\n Avg positive={}\nAvg negative={}".format(cp,cn,cz,sump,sumn,(sump/cp),(sumn/cn))) 

        
