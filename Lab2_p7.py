
list_p7 = [76, 92.3, 'hello', True, 4, 76]

print list_p7

list_p7.append('apple')
list_p7.append(76)

print list_p7

list_p7.insert(0, 99)

print list_p7

list_p7.insert(3, 'cat')

print list_p7

indexHello = list_p7.index('hello')

print indexHello

count76 = list_p7.count(76)

print count76


list_p7.remove(76)

print list_p7

TrueIndex = list_p7.index(True)

print TrueIndex

list_p7.pop(list_p7.index(True))

#list_p7.pop(4)

print list_p7