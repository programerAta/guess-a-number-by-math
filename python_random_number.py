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
    meghdar_jan=int(input("enter your amount of heart:\n"))
    jan=meghdar_jan
    Number_vasat=list( map(int,input("select two number \n").split()))
    Number_random=random.randint(min(Number_vasat),max (Number_vasat))
    while True:
        Number=int(input("Enter Number: \n"))
        if Number==Number_random:
            print("You Win")
            jan=meghdar_jan
            Number_random=random.randint(min(Number_vasat),max (Number_vasat))
        elif Number<Number_random:
            print(f"The Number Is More Than {Number}")
            jan-=1
        elif Number>Number_random:
            print(f"The Number Is lower Than {Number}")
            jan-=1
        if jan==0:
            jan=meghdar_jan
            print("you lose")
            print(f"The Number Was {Number_random}")
            Number_random=random.randint(min(Number_vasat),max (Number_vasat))
