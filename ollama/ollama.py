import os

while True:
	print("""
Install(i)
List model(l-m)
List running(l-r)
Remove(r)
Quit(q)
""")

	choice = input("enter: ")

	if choice == "i":
		while True:
			print("""
Model Name(Type the model you want to download)
Quit(q)
""")
			name = input("Enter: ")
			if name == "q":	
				break
			os.system("ollama pull "+name)
	elif choice == "l-m":
		os.system("ollama list")
	elif choice == "l-r":
		os.system("ollama ps")
	elif choice == "r":
		while True:
			print("""
Model Name(Type the model you want to remove)
Quit(q)
""")
			name = input("Enter: ")
			if name == "q":
				break
			os.system("ollama rm "+name)
	elif choice == "q":
		break
	else:
		print("hmm maybe you can try writing what's in parentheses?")
