#append()
list=["kirti","Aishwarya",31304,51004]
list.append(13421)
list.append(31099)
print(list)

#insert
list=[31,11,18,5,31]
list.insert(3,3)
print(list)

#concate
list1=[12,14,16,18,20]
list2=[1,3,5,7,9,11]
l=list1+list2
print(l)

#repetition
list1=[12,14,16,18,20]
l=list1*2
print(l)

#sum
list=[1,2,3,4,5]
print(sum(list))

#count
l=[1,2,3,4,1,2,5,7,1,8,2,3,4,8,9,2,3,1,2,3,4,6,2,6,8,3,3,4]
print(l.count(1))
print(l.count(2))
print(l.count(6))

#len
l=[12,3,4,6,11,3,22,9,65,4,55,73]
print(len(l))

#index
list=[0,3,5,1,8,2]
print(list.index(0))
print(list.index(3))
print(list.index(8))

#del
list=["python",23,"CSE",24]
del list [0]
print(list)
del list [1]
print(list)
del list [0]
print(list)


#remove
list=["python","DBMS","IPR","SDN","DAA"]
list.remove("DAA")
print(list)
list.remove("SDN")
print(list)
list.remove("python")
print(list)