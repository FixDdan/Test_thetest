import time
import math

flie = "main.py"
print(f"flie: {flie}")
passward = int(input("passward: "))
while not passward == 123456:
    print("incorrect")
    passward = int(input("passward"))
else:
    print("correct")
    print("loding...")
    time.sleep(2)
    print("-----wellcome to main.py-----")
    command = input(main.py: )
    while command == "help":
        print(": this is some command to help you")
        print("  help exit")
        command = input(main.py: )
    if command == "exit":
        print("main.py: exit")