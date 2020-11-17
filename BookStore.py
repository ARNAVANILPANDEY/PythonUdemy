a=[0,0,0,0,0]
for e in range (0,5):
    a[e]=int(input("Enter the number of Book {} you want to purchase".format(e+1)))
cost=0
def switch_case(s):
    switcher={0:0.25,
              1:0.2,
              2:0.1,
              3:0.05,
              4:0
              }
    return(switcher[s])

a.sort()
for i in range(0,5):
    if(a[i]==0):
        continue
    else:
        cost=cost+((5-i)*(8-(8*switch_case(i))))
        for j in range(0,5):
            a[j]=a[j]-1



print(cost)






            
