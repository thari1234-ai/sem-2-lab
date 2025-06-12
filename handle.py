with open("inputj.txt","r")as inline, open("outputj.txt","w")as outline:
    lines=inline.readlines()
    for i in range(len(lines)):
        if i%2==0:
            outline.write(lines[i])
            print(lines[i].strip())