import users
import owner

print("\n!!!!!---------------*****------------------- WELCOME TO AK RESTAURANT --------------*****--------------------!!!!!\n")

print("   '1'----->>> Customer")
print("   '2'----->>> Restaurant Staff")

ch=input("\n   enter the choices : ")

if ch=='1':
    users.login()
elif ch=='2':
    owner.login()
else:
    print("\n!---invalid choices---!")
    print("please choice above option\n")