x=int(input("donner un entier: "))
ok=True
for i in range(x):
    if(x%2==0):
        x=x/2


if(x==1):
    print("totallement divisble")
else:
    print("ce nombre n'est pas totallemebnt divisible")