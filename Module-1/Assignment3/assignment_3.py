lower,upper = 0,0

str = input("Enter the string : ")
for i in str:
    if i.isupper():
        upper += 1 

    if i.islower():
        lower+= 1

print(f"UPPER CASE {upper}\nLOWER CASE {lower}")