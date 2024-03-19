def split_name(name):
    space = name.find(' ')
    return name[:space] + "\n" + name[space+1:]

def bondify(name):
    space = name.find(' ')
    return name[space+1:] + "... " + name

def find_last(str, target):
    if(str.find(target) == -1):
        return -1
    return len(str) - str[::-1].find(target) - 1

def replace(str, delete, add):
    idx = str.find(delete)
    if(idx == -1):
        return str
    return str[:idx] + add + str[idx + len(delete):]

print(split_name("John Shaft"))
print(bondify("Mr DW"))
print(find_last( 'hello', 'l'))
print(find_last('hello', 'h'))
print(find_last('hello', 'z'))
print(replace("I hate cs!", "hate", "love"))
