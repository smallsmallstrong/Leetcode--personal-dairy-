
# input value, format is a-b 3:2
# 比分获胜+3 比分平各+1 比分为负不加也不减

# Create your dictionary class
class my_dictionary(dict):
    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


dict_obj = my_dictionary()
lines = []
while True:
    ans = input("input:")
    lines.append(ans)
    if ans == "S" : break

#print(lines)
l = len(lines)

"""
input:a-b 3:3
input:a-c 3:2
input:a-d 1:1
"""

for i in range(l-1):
    #print(i,',',list(ch))
    #for j,str in enumerate(ch):
    ch = lines[i].split(" ")
    #name.append(chl[0].split("-"))
    name = ch[0].split("-")
    for j in range(2):
        dict_obj.add(name[j],0)

for i in range(l-1):
    #print(i,',',list(ch))
    #for j,str in enumerate(ch):
    ch = lines[i].split(" ")
    #name.append(chl[0].split("-"))
    name = ch[0].split("-")
    value = ch[1].split(":")

    if int(value[0]) > int(value[1]):
        print(dict_obj[name[0]])
        dict_obj[name[0]] += 3
    elif int(value[0]) < int(value[1]):
        dict_obj[name[1]] += 3
    else:
        dict_obj[name[0]] += 1
        dict_obj[name[1]] += 1

dic = dict(sorted(dict_obj.items(), key=lambda item: item[1], reverse=True))
print(dic)
