from collections import Counter

str = input("Enter the string: ")
list = str.split(" ")
count_dict = Counter(list)
# for i in count_dict:
#     print(count_dict.keys())


for key, value in sorted(count_dict.items()):
	print(f"{key}:{value}")