#==============IMPORT==============
import random
import sys
import os
#==============GETCH===============
if sys.platform == "win32":
	import msvcrt

	def getch():
		return msvcrt.getch().decode('utf-8')
#=============Clear===============
def clear(): #cls for win and clear for linux, apparently it'll show error code if i kept use "cls;clear"
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
#===================================


def register():
    print("Welcome to Azure Bank! \nPlease input your name :")
    user = input()
    uid = 80000000 + random.randint(100, 9999)
    reg = True
    return user, uid, reg

def show_menu(user, uid, money):
    clear()
    print("""
        Welcome to Azure Bank! 
        How may i help you today?
        1. Account
          """)
    x = getch()
    if x == "1":
        account(user, uid, money)

def account(user, uid, money):
    clear()
    while True:
        print(f"""
        Account Details
        User : {user}
        Uid : {uid}
        Money : {money}
        
        Press 1 to go back
            """)
        x = getch()
        if x == "1":
            show_menu()




user = None
uid = None
money = 0


reg = False
if reg is False:
    user, uid, reg = register()

if reg is True:
    show_menu(user, uid, money)

