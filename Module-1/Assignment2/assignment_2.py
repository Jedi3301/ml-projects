letters,numbers = 0,0

str = input("Enter the string : ")
for i in str:
    if i.isnumeric():
        numbers += 1 

    if i.isalpha():
        letters+= 1
print(f"LETTERS {letters}\nNUMBERS {numbers}")