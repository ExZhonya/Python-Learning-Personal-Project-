import os, sys
def clear(): #cls for win and clear for linux, apparently it'll show error code if i kept use "cls;clear"
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")




def main():
    clear()
    while True:
        try:
            num_1 = int(input("Input the first number: "))
            num_2 = int(input("Input the second number: "))
            op = input("Input the operation you wanted(+ - * / // %): ")

            if op == "+":
                print(f"{num_1} + {num_2} = {num_1 + num_2}")
                break
            elif op == "-":
                print(f"{num_1} - {num_2} = {num_1 - num_2}")
                break
            elif op == "*":
                print(f"{num_1} * {num_2} = {num_1 * num_2}")
                break
            elif op == "/":
                print(f"{num_1} / {num_2} = {num_1 / num_2}")
                break
            elif op == "//":
                print(f"{num_1} // {num_2} = {num_1 // num_2}")
                break
            elif op == "%":
                print(f"{num_1} % {num_2} = {num_1 % num_2}")
                break
            else:
                 print("Please put a valid operation!")
                 break
                 
                 
        except ValueError:
             clear()
             print("Please put numbers!")

main()