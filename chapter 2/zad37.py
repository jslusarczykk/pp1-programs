b = "Mr. John May, born on 1998-02-16"
#b = "Hello, World!"
#print(b[-5:-2])

desc=str(input("Give me an example: "))
print(desc)

#uogólnienie
for i in range(0,len(desc)):
    empty=" "
    beg=0
    end=999
    name=""
    surname=""
    initials=""
    born=""
    i=0
    i+=1
    if(desc[i]==empty):
        beg=i+1
        for i in range(beg,len(desc)):
            if(desc[i]==empty):
                end=i-1
                name=desc[beg:end]
                print(name)


#??? 

#print("Name: ",desc[4:8])
#print("Surname: ",desc[9:8])