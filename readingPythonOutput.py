# with open("using python 09-05-23 21-45-18.txt","r") as f:
#     print(f.read())


with open("using python 09-05-23 21-45-18.txt","r") as f:
    data = f.read().split('\\n')
    for d in data:
        print(d)