try:
    cb=float(input("Enter the cost of book:\t"))
    nb=float(input("Enter the number of books:\t"))
    sc=float(input("Enter the shipping charge of book:\t"))
    if(cb<0 or nb<0 or sc<0):
        test=(cb/0)+(nb/0)+(sc/0)
    if(nb<50):
        tp=(cb*nb)
        scost=(sc*nb)
    else:
        tp=(cb*50) + ((nb-50)*cb*0.75)
        if(nb>100):
            scost=(sc*100)+(0.85*sc*(nb-100))
        else:
            scost=sc*nb

except:
    print("\n Invalid choice")
    exit()

print(" Total price ={:.2f}\nTotal shipment charge={:.2f}\nGrant total={:.2f}\n Rounded grand total={:.2f}"
            .format(tp,scost,(scost+tp),round((scost+tp),0)))  
    
        
    
