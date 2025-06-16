#write a program to greet all the person names stored in a list "L" and which starts with s. L=["Smriti", "arna", "shayma", "ashiraa"]


L=["Smriti", "arna", "shayma", "ashiraa"]

for name in L:
    if(name.startswith("s")):
        print(f"Hello {name}")