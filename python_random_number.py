import random
tanzimat=input("heart or normal\n")
if tanzimat=="normal":
    Number_vasat=list( map(int,input("select two number").split()))
    Number_random=random.randint(min(Number_vasat),max (Number_vasat))
    while True:
        Number=int(input("Enter Number: \n"))
        if Number==Number_random:
            print("You Win")
            Number_random=random.randint(min(Number_vasat),max (Number_vasat))
        elif Number<Number_random:
            print(f"The Number Is More Than {Number}")
        elif Number>Number_random:
            print(f"The Number Is lower Than {Number}")
elif tanzimat=="heart":
    meghdar_hp=int(input("enter your amount of heart:\n"))
    hp=meghdar_hp
    Number_vasat=list( map(int,input("select two number \n").split()))
    Number_random=random.randint(min(Number_vasat),max (Number_vasat))
    while True:
        Number=int(input("Enter Number: \n"))
        if Number==Number_random:
            print("You Win")
            hp=meghdar_hp
            Number_random=random.randint(min(Number_vasat),max (Number_vasat))
        elif Number<Number_random:
            print(f"The Number Is More Than {Number}")
            hp-=1
        elif Number>Number_random:
            print(f"The Number Is lower Than {Number}")
            hp-=1
        if hp==0:
            hp=meghdar_hp
            print("you lose")
            print(f"The Number Was {Number_random}")
            Number_random=random.randint(min(Number_vasat),max (Number_vasat))
