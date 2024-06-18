#Assignment 3
#Name: SASIKUMAR S
#--------------------------------------------------------------------------------#
#**ST~SUPERMARKET**
import datetime
def main():
    import newmail()
    print("***ST~SuperMarket***")
    print("SECTIONS\n1.groceries\n2.vegetables\n3.fruit")
    
    try:
        section=int(input("what section will you visited"))
        if section==1:
            import groceries
            sum1=groceries.groc()
        elif section==3:
            import fruit
            sum2=fruit.fruit()        
    except ValueError:
        print("HEllO type number only ex:1 2 3")
    return sum1+sum2
    newmail.send_email()
 #   f.write(f"sub Total={return}")

main()

