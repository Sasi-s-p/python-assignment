import datetime
def gro():
    print("WELCOME GROCERIES SECTION")
    print("1.Red_chili-100gm-RS 95\n2.Turmeric_powder-100gm-RS87\n3.Black_papper-100gm-RS 56\n4.Bay_leaf-100gm-RS 67\n5.mustard-100gm-RS 35")
    
    item={"redchilli":95,"turmericpowder":87,"blackpapper":56,"bayleaf":67,"mustard":35}
    sum=0
    #f=open("gro.txt","w")
    while True:
      f=open("gro.txt","a")
      x=input("What you want ?:")

      if x in item:
          how_many=int(input("How many packets do you want?"))
          sum+=how_many*item[x]
          f.write(f"\n{x} -RS{item[x]} {how_many} packets ")
          again=input("Do you want anything else(YES/NO)")
          if again!='yes':
           break
      else:
        print("Sorry not available")
    x=datetime.datetime.now()    
    f.write(f"\nSub total ={sum}\nTime & Date:{x}\nThank You Come Aagin!!\n")    
    return sum   
sum=gro()
print("Tottal=",sum)
