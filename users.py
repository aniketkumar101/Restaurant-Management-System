import items

def login():
    print("\n")
    print("                 !!!---CUSTOMERS PAGE---!!!                   ")
    print("\n")
    print("-"*50)
    print("   '1'----->>> New User")
    print("   '2'----->>> Existing User")
    print("-"*50)

    ch1=input("\n   enter the choices : ")

    if ch1=='1':
        fp=open("customers.txt","r")
        c=fp.readlines()
        name=input("\n   enter your name : ")
        p=input("   enter the password : ")
        k=(name + "," + p + "\n")
        flag=0
        for i in c:
            if k in i:
                print("\n   Username already exists")
                print("   !!!---Thank you---!!!\n")
                flag=1
                break
        
        if flag==0:
            di="0123456789"
            ca="QWERTYUIOPASDFGHJKLZXCVBNM"
            sa="qwertyuiopasdfghjklzxcvbnm"
            sc="!@#$%^&*?/"
            d,c,s,sp,flag=0,0,0,0,0
           
            if len(p)>=6:
                for i in p:
                    if i in di:
                        d=d+1
                    elif i in ca:
                        c=c+1
                    elif i in sa:
                        s=s+1
                    elif i in sc:
                        sp=sp+1
                    else:
                        pass
                if d>=1 and c>=1 and s>=1 and sp>=1:
                    print("-"*25)
                    print("   Password successful")
                    print("\n   !!!!!----- ACCOUNT CREATED SUCCESSFULLY -----!!!!!\n")
                    print("-"*25)
                    fp=open("customers.txt","a")
                    fp.writelines( name + "," + p + "\n")
                    fp.close
                    items.itemslist()
            if len(p)>=6 or len(p)<6:
                print("\n")
                if d==0:
                    print("   no digit")
                if c==0:
                    print("   no capital alphabets")
                if s==0:
                    print("   no small alphabets")
                if sp==0:
                    print("   no special characters")
                print("\n")
            if len(p)<6:
                print("\n   length of password should be atleast 6\n")
                flag=1

    elif ch1=='2':
        name=input("\n   enter your name : ")
        p=input("   enter the password : ")
        k=(name + "," + p + "\n")
        flag=0
        fp=open("customers.txt","r")
        c=fp.readlines()
        for i in c :
            if k in i:
                print("-"*25)
                print("   LOGIN SUCCESSFULLY")
                print("-"*25)
                items.itemslist()
                flag=1
                break
        if flag==0:
            print("\n   Invalid username or password")
            print("   !!!---Thank you---!!!\n")
            
    else:
        print("\n   Invalid\n")