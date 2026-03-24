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
    clear()
    print("Welcome to Azure Bank! \nPlease input your name :")
    user = input()
    uid = 80000000 + random.randint(100, 9999)
    reg = True
    return user, uid, reg

def show_menu(money):
    clear()
    while True:
        print("""
            Welcome to Azure Bank! 
            How may i help you today?
            1. Account
            2. Deposit
            3. Withdrawal
            4. Transfer
            5. Exit
            """)
        x = getch()
        if x == "1":
            account(user, uid, money)
        elif x == "2":
            clear()
            money = depo(money)
        elif x == "3":
            clear()
            money = withd(money)
        elif x == "4":
             clear()
             money = trf(money)
        elif x == "5":
             clear()
             exit()
             break

def account(user, uid, money):
    clear()
    while True:
        print(f"""
        Account Details
        User  : {user}
        UID   : {uid}
        Money : {money}
        
        Press 1 to go back
            """)
        x = getch()
        if x == "1":
            break


def depo(money):
    clear()
    while True:
        print("Please add money you want to deposit.")
        
        try:
            add = int(input())
            money += add
            clear()
            print(f"Your Balance is now {money}")
            
            print("Press 1 to go back")
            x = getch()
            if x == "1":
                return money 
            else:
                return money
            
        except ValueError:
            clear()
            print("You should add ONLY number!")

def withd(money):
     clear()
     while True:
        print("Please add money you want to withdraw.")
        try:
            sub = int(input())
            money -= sub
            clear()
            print(f"you have withdrawn {sub}")
            print(f"Your balancce is now {money}")

            print("Press 1 to go back")
            x = getch()
            if x == "1":
                return money
            else:
                return money
            
        except ValueError:
            clear()
            print("You should add ONLY number!")

def trf(money):
    while True:
         try:
            print("Please enter the other party's UID")
            uid = int(input())
            print("Please enter how much balance you want to send.")
            tf = int(input())
            if money < tf:
                clear()
                print("You do not have enough money!")
                trf(money)
            elif money >= tf:
                money -= tf
                clear()
                print(f"You have sent {tf} to {uid}")
                print(f"Your balance is now {money}")

            print("Press 1 to go back")
            x = getch()
            if x == "1":
                return money
            else:
                return money
         except ValueError:
              clear()
              print("You should add ONLY number!")

def exit():
     while True:
        print("Thank You for using Azure Bank!")
        break




#=============MAIN=============
user = None
uid = None
money = 0

reg = False
if reg is False:
    user, uid, reg = register()

if reg is True:
    show_menu(money)
#===============================