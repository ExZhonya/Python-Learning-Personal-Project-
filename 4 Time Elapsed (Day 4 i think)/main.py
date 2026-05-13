import time
import os
import sys

def clear(): #cls for win and clear for linux, apparently it'll show error code if i kept use "cls;clear"
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")


label = "Screen Time"
scr_tm = 0

#the real things here
start_time = time.perf_counter()
time.sleep(5)

print("sum shit")
print(f"Time Elapsed:{time.perf_counter() - start_time:.2f}")

def start():
    clear()
    while True:
        print("""
        1. Check Your Screentime
        2. Exit
            """)
        x = input()
        try:
            if x == "1":
                stats()
        except ValueError:
            print("Only 1-2!")
            clear()

def stats():
    clear()
    print(f"""
    Time Elapsed:{time.perf_counter() - start_time:.2f}
""") 
    x = input("1.Main Menu")
    try:
        if x == "1":
            start()
    except ValueError:
        print("Only 1-2!")
        clear()

start()