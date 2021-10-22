import random

f=list()
s=list()

num = int(input('Enter the number of friends you have: '))

for i in range(num):
    a=input(f"Enter the name of friend {i+1}: ")

    g = a.split()    #by default it splits the string where it finds a white space
    #Now g is a list
    f.append(g[0])   #Appending the first element  of list g  
    f.append(g[1])
    s.append(g[1])
    print(len(f))
#Now f is a list ..
for i in range(len(f)):  

    if i%2 == 0:

        r = random.randint(0 ,len(s)-1)
        if r == len(s) - 1:
            print(f"{f[i]} {s[r-1]}")
        else:
            print(f"{f[i]} {s[r+1]}")
                
    else:
        continue