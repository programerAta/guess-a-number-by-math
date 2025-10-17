import random
tanzimat=input("heart or normal\n")
if tanzimat=="normal":
    adad_vasat=list( map(int,input("select two number").split()))
    adad_random=random.randint(min(adad_vasat),max (adad_vasat))
    while True:
        adad=int(input("Enter Number: \n"))
        if adad==adad_random:
            print("You Win")
            adad_random=random.randint(min(adad_vasat),max (adad_vasat))
        elif adad<adad_random:
            print(f"The Number Is More Than {adad}")
        elif adad>adad_random:
            print(f"The Number Is lower Than {adad}")
elif tanzimat=="heart":
    meghdar_jan=int(input("enter your amount of heart:\n"))
    jan=meghdar_jan
    adad_vasat=list( map(int,input("select two number \n").split()))
    adad_random=random.randint(min(adad_vasat),max (adad_vasat))
    while True:
        adad=int(input("Enter Number: \n"))
        if adad==adad_random:
            print("You Win")
            jan=meghdar_jan
            adad_random=random.randint(min(adad_vasat),max (adad_vasat))
        elif adad<adad_random:
            print(f"The Number Is More Than {adad}")
            jan-=1
        elif adad>adad_random:
            print(f"The Number Is lower Than {adad}")
            jan-=1
        if jan==0:
            jan=meghdar_jan
            print("you lose")
            print(f"The Number Was {adad_random}")
            adad_random=random.randint(min(adad_vasat),max (adad_vasat))
