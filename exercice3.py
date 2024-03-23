import random



while True:
    k = random.randint(1, 9)
    print(k)
    choix=input("donner un entier or exit")
    if(choix=="exit"):
        break
    else:
        nb=int(choix)
        if(nb>k):
            print("trop eleve")
        elif(nb<k):
            print("trop faible")
        else:
            print("tout a fait exact!!")

