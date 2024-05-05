import users
def login():
    print("\n")
    print("                 !!!---OWNER PAGE---!!!                   ")
    print("\n")
    pd="Owner@123"
    pwd=input("\n   enter the password : ")
    if pwd==pd:
        print("\n   !!!--- Login successfull ---!!!\n")
        while True:
            print("\n---------------------- What do you want to do? ----------------------\n")
            print("   '1' ----->>> View items list")
            print("   '2' ----->>> Update items in the list")
            print("   '3' ----->>> Dispatch order")
            print("   '4' ----->>> Close")
            print()
            ch = input("\n   Enter your choice : ")
            if ch =='1':
                print("\n")
                print("="*20," !! ITEMS PAGE !!","="*30)
                print()
                fp = open("items.txt")
                c=fp.read()
                print(c)
                fp.close()
            elif ch == '2':
                l=[]
                fp=open("items.txt","r")
                cp=fp.readlines()
                for i in cp:
                    k=i.rstrip().split(",")
                    l.append(k[0])
                print("\n   1----->>> Add new item ")
                print("   2----->>> Delete new item ")
                print("   3----->>> Update the price of an item ")
                ch1=input("\nEnter your choice : ")
                if ch1=='1':
                    item_no=input("Enter the item no : ")
                    if item_no in l:
                        print("Item no is already present !!")
                        break
                    else:
                        item_name=input("Enter the item name : ")
                        item_price=input("Enter the item price : ")
                        fp=open("items.txt","a")
                        fp.writelines(item_no + "," + item_name + "," + item_price + "\n")
                        print("\n !! Item has been added successfully !!\n")
                elif ch1 =='2':
                    fp = open("items.txt","r+")
                    c=fp.readlines()
                    fp.seek(0)
                    ch5=input("Enter the item number to be deleted from the list: ")
                    if ch5 in l:
                        for i in c:
                            k=i.rstrip().split(",")
                            if k[0]!= ch5:
                                fp.write(i)
                        fp.truncate()
                        print("********** Item has been deleted **********")
                    else:
                        print("!!  Item number is not present !! ")
                elif ch1 =='3':
                    flag = 0
                    fp=open("items.txt",'r')
                    cp=fp.readlines()
                    itemno = input("Enter the item number : ")
                    if itemno in l:
                        name=input("Enter the name of the item whoose price you want to update: ")
                        price = input("Enter the price to be updated : ")
                        if price.isdigit():
                            for i in  range(len(cp)):
                                if name in cp[i]:
                                    cp[i] = itemno + ","+ name + "," + price + "\n"
                                    print(cp[i])
                                    print("\nItem Successfully UPDATED ")
                                    flag=1
                                    break
                            if flag ==0 :
                                print("\nItem not found")
                        else:
                            print("\n!! Price should only contain Digits !!")
                        
                        fp=open("items.txt","w")
                        op =fp.writelines(cp)
                    else:
                        print("!! Item no. not present !!")
                else:
                    print("!! INVALID CHOICE !!")
                 
            elif ch == '3':
                fp = open("orderlist.txt","r")
                c=fp.readlines()
                print("The List is : ")
                for i in c:
                    print(i)
                fp1=open("orderlist.txt","r+")
                cp=fp1.readlines()
                fp1.seek(0)
                l1=[]
                for i in cp:
                    k1=i.rstrip().split(",")
                    l1.append(k1[0])
                print()
                print(l1)
                print()
                choice=input("Choose order no. to dispatch : ")
                if choice in l1:
                    for i in cp:
                        k1=i.rstrip().split(",")
                        if k1[0]!=choice:
                            fp1.write(i)
                    fp1.truncate()
                    print("\n---------- Item Dispatched ----------")
                else :
                    print("\n!!   Item not present   !! ")

            elif ch == '4':
                print("\n\n")
                print("-"*30," !! THANK YOU !! ","-"*30)
                break
    else:
        print("========== Invalid password ! ==========")
        print()
        print("-"*40,"*"*20,"-"*40)



            
