print("Welcome to Python Pizza")
print("Pizza Available in the following sizes")
print("1.Small size-$15\n2.Medium size-$20\n3.Large size-&25")
size=int(input("1/2/3="))
print('''Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3''')
pepperoni=input("need pepperoni (y/n)=")
print("cheese for any size pizza: +$1")
cheese=input("need cheese (y/n)=")
cost=0
if size==1:
    cost=cost+15
elif size==2:
    cost=cost+20
elif size==3:
    cost=cost+25

if pepperoni=="y":
    if size==1:
        cost=cost+2
    else:
        cost=cost+3
if cheese=="y":
    cost=cost+1
print(f"Your pizza order cost is ${cost}")
"""import vigmod
print(vigmod.random.randint(10,20))"""

"""user_input=input("yes/no:")
while (user_input!="yes" and user_input!="y"):
    print("Hi")
    user_input = input("yes/no:")"""