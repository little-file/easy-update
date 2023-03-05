import os
print("    hello welcome")

def dnfup(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
            x = False

        if z == "y":
            os.system("sudo pacman -Syu --noconfirm")
            print("done")
            x = False

def dnfin(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
           x = False
      
        if z == "y":
            c = input("App name: ")
            os.system("sudo pacman -S --noconfirm"+ c)
            print("done")
            x = False

def dnfremove(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
           x = False
      
        if z == "y":
            c = input("App name: ")
            os.system("sudo pacman -Rs "+ c)
            print("done")
            x = False

def dnfsearch(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
           x = False
      
        if z == "y":
            c = input("App name: ")
            os.system("sudo pacman -Ss "+ c)
            print("done")
            x = False

x = True

while x == True:
    print("""    [1]pacman update 
    [2]pacman install
    [3]pacman remove
    [4]pacman search
    [5]reboot
    [6]quit
    """)
    z = int(input("please number enter: "))
    if z== 1:
        dnfup()
    elif z == 2:
        dnfin()
    elif z == 3:
        dnfremove()
    elif z == 4:
        dnfsearch()
    elif z == 5:
        os.system("reboot")
    elif z == 6:
        x = False