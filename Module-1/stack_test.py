def stack():
    str = ['{' ,'}']
    stack = []
    hashmap = {')':'(','}':'{',']':'['}
    for i in str:
        if i not in hashmap:
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                popped = stack.pop()
                if popped != hashmap[i]:
                    return False
    return not stack
    
stack()
# print(str)