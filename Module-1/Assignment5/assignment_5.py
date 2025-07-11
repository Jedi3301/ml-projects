str = input("Enter the String: ")
upper, lower, number, special = 0, 0, 0, 0
if 8 <= len(str) <= 14:
    if not any(word in str for word in ["password", "12345", "qwerty", "admin", "username"]):
        for i in str:
            if i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            elif i.isdigit():
                number += 1
            else:
                special += 1
        # print(upper, lower, number, special)

        if upper >= 2 and lower >= 2 and number >= 2 and special >= 2:
            print("Strong")
        elif upper >= 1 and lower >= 1 and number >= 1 and special >= 1 and (upper >= 2 or lower >= 2 or number >= 2 or special >= 2):
            print("High")
        elif upper >= 1 and lower >= 1 and number >= 1 and special >= 1:
            print("Moderate")
        else:
            print("Weak")
    else:
        print("Password doesnt meet criteria!")
else:
    print("Password doesnt meet criteria!")