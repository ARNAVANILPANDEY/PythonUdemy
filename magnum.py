a=int(input('Enter a Number'))

b=a;
while(b/10!=0):
    s=0
    while(b>0):
        n=b%10
        b=b/10
        s=s+n
    b=s

print(b)    

if(b==1):
    print(a,' is a magic number')
else:
    print(a,' is not a magic number')

