import datetime
def fruit():
    print("WELCOME VEGETABLE SECTION")
    print("1.Apple-1kg-RS 80\n2.Banana-1kg-RS 124\n3.mango-1kg-RS 120\n4.grape-1kg-RS 67\n5.Kiwi-1kg-RS 40")
    item={"apple":95,"banana":87,"mango":56,"kiwi":67,"grape":35,"guva":40}
    sum=0
    while True:
        f=open("fruit.txt","a")
        x=input("What do you want?")
        if x in item:
           how_many=int(input("How many kg you want?"))
           sum+=how_many*item[x]
           f.write(f"\n{x} -RS{item[x]} {how_many}kg ")
           again=input("Do you want anything else(YES/NO)")
           if again!='yes':
              break
        else:
          print("Sorry not available\n")
          break

    x=datetime.datetime.now()    
    f.write(f"\nSub total ={sum}\nTime & Date:{x}\nThank You Come Aagin!!\n")    
    return sum   
sum=fruit()
print("Tottal=",sum)


# item={"Aplle":95,"Banana":87,"Mango":56,"Kiwi":67,"Grape":35,"Guva":40}
# i=input("give")
# if i in item:
#     print(i)