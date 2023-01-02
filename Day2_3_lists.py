
list0 = [1,3,5,7,9]
print(list0, type(list0))
print(f"list0 의 사이즈 : {len(list0)}")

list0.append(6)
print(list0)
popOut = list0.pop(0)
print(f"popOut : {popOut}")
print(list0)


list0.remove(5)
print(list0)
list0.insert(1, 11)
print(list0)