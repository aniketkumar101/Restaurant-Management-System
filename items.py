def itemslist():

    import random
    print("\n")
    print("                 !!!---ITEM PAGE---!!!                   ")
    print("\n")
    fp=open("items.txt","r")
    c=fp.read()
    print(c)
    fp.close()
    total=0
    list=[]
    list1=[]
    list2=[]
    fp=open("items.txt",'r')
    cp=fp.readlines()
    while True:
        dn=input("\n\n   Choose the dish number: ")
        list.append(dn)
        q=int(input("   Enter the quantity: "))
        list1.append(q)
        for i in cp:
            k=i.rstrip().split(",")
            if k[0]==dn:
                total = total + (q *int(k[2]))
        ch5=input("   Press 'y' to choose another dish: ").lower()
        if ch5=='y':
            continue
        else:
            on=random.randint(1,1000) + random.randint(1000,2000)
            print("\n   *** YOUR ORDER LIST ***")
            print(f"\nOrder number : {on}")
            list2.append(f"{on},")
            for i in cp:
                k=i.rstrip().split(",")
                for j in range(len(list)):
                    if k[0]==list[j]:
                        print(f"{k[1]},{list1[j]}")
                        list2.append(f"{k[1]},{list1[j]},")
            list2.append("\n")
            print("\n   !!!----->>> TOTAL AMOUNT : ",total," <<<-----!!!")
            break
    ch2=input("   YOU CONFIRM THE ORDER : (YES/NO): ")
    if ch2=='YES':
        print("\n\n\n   !!!----- Order recieved !! Visit Again -----!!!\n")
        ol=open("orderlist.txt",'a')
        ol.writelines(list2)
        ol.close()
    else:
        print("\n\n\n   !!!----- Thank you ! Relogin for new order -----!!!\n")