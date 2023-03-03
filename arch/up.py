import os
print("    hello welcome")

def dnf(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
            x = False

        if z == "y":
            os.system("sudo pacman -Syyuu --noconfirm")
            print("done")
            x = False

def flatpak(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
           x = False
      
        if z == "y":
            os.system("flatpak update -y")
            print("done")
            x = False

x = True

while x == True:
    print("""    [1]pacman update 
    [2]flatpak update
    [3]reboot
    [4]quit
    """)
    z = int(input("please number enter: "))
    if z== 1:
        dnf()
    if z == 2:
        flatpak()
    if z == 3:
         os.system("reboot")
    if z == 4:
        x = False
