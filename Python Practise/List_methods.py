list = ["dhruv","is","the","Student","in ","in "]
print(list)

list.append("in Rajkot")
print(list)

list.pop()
print(list)

list2 = ["in ","Rajkot ","Darshan ","University"]
list.extend(list2)
print(list)

list.remove('dhruv')
print(list)

list.insert(0,"dhruv")
print(list)

list2.clear()
print(list2)

print(list.index('in '))

print(list.count('in '))

list3 = list
list3.reverse()
print(list3)

list.sort()
print(list)