import os
print("    hello welcome")

def dnfup(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
            x = False

        if z == "y":
            os.system("sudo dnf update -y")
            print("done")
            x = False

def dnfin(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
           x = False
      
        if z == "y":
            c = input("App name: ")
            os.system("sudo dnf in -y "+ c)
            print("done")
            x = False

def dnfremove(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
           x = False
      
        if z == "y":
            c = input("App name: ")
            os.system("sudo dnf remove -y "+ c)
            print("done")
            x = False

def dnfsearch(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
           x = False
      
        if z == "y":
            c = input("App name: ")
            os.system("dnf search "+ c)
            print("done")
            x = False

x = True

while x == True:
    print("""    [1]dnf update 
    [2]dnf install
    [3]dnf remove
    [4]dnf search
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
