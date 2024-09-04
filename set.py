

# typecasting 
myset = set(["a", "b", "c"])
print(myset)

myset.add("d")
print(myset)

#days
days={"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"}
print(days)
for i in days:
    print(i)
    
# intersection & Union
days1={"Sunday","Monday","Tuesday","Wednesday"}
days2={"thursday","Friday","saturday","Sunday"}
print(days1 | days2)
print(days1.union(days2))
print(days1.intersection(days2))
print(days1.difference(days2))