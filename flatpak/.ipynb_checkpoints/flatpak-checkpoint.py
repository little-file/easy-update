import os
print("    hello welcome")

def flatpakup(x = True):
    while x == True:
        z = input("y/n: ")
        if z == "n":
           x = False
      
        if z == "y":
            os.system("flatpak update -y")
            print("done")
            x = False
def flatpakin(x = True):
    while x == True:
        z = input("app name: ")
        print("flatpak install -y", z)
        y = input("do you approve ? y/n: ")
        if y == "y":
            os.system("flatpak install -y "+ z)
        if y == "n":
            x = False

def flatpakremove(x = True):
    while x == True:
        z = input("app name: ")
        print("flatpak remove -y", z)
        y = input("do you approve ? y/n: ")
        if y == "y":
            os.system("flatpak remove -y "+ z)
        if y == "n":
            x = False

def flatpaksearch(x = True):
    while x == True:
        z = input("app name: ")
        print("flatpak search", z)
        y = input("do you approve ? y/n: ")
        if y == "y":
            os.system("flatpak search "+ z)
        if y == "n":
            x = False
x = True

while x == True:
    print("""    [1]flatpak update 
    [2]flatpak install apps
    [3]flatpak remove apps
    [4]flatpak search apps
    [5]reboot
    [6]quit
    """)
    z = int(input("please number enter: "))
    if z== 1:
        flatpakup()
    if z == 2:
        flatpakin()
    if z == 3:
         flatpakremove()
    if z == 4:
        flatpaksearch()
    if z == 5:
        os.system("reboot")
    if z == 6:
        x = False