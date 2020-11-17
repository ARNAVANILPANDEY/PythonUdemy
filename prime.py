'''import math

m=0

for i in range(2,1000000):
    n=0
    for j in range(2,1+int(math.sqrt(i))):
        if(i%j==0):
            break
        else:
            n=n+1
    if(n==int(math.sqrt(i))-1):
        print(i,' is a prime number')
        m=m+1
        print('(',m,'th prime)')
        if(m==100):
            break'''

import math

m=0
i=1
while(m!=100):
    i=i+1
    n=0
    for j in range(2,1+int(math.sqrt(i))):
        if(i%j==0):
            break
        else:
            n=n+1
    if(n==int(math.sqrt(i))-1):
        print(i,' is a prime number')
        m=m+1
        print('(',m,'th prime)')
        
            
          



          


