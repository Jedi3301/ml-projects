str = input("Enter the string: ")
seperated_words = str.split(" ")

seperated_words = list(set(seperated_words))
# seperated_words
seperated_words.sort()
# print(seperated_words)

for i in seperated_words:
    print(i,end=" ")