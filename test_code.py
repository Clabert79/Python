import sys
print(sys.version)

new_list =[]

def multi_b2(li):
    for item in li:
        new_list.append(item*2)
return new_list


print(multi_b2(1,3,5))

print(new_list)

