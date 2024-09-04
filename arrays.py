#Program using array and array functions
flowers=["Rose","Mogra","Dahlia"]

print(flowers)
a=flowers[0]
print(a)
b=flowers[1]
c=flowers[2]
print(b)
print(c)
print("Modifying the value of the first array item:")
flowers[0]="Hibiscus"
print(flowers)
l=len(flowers)
print("The length of given array is :",l)
print("Using append():")
flowers.append("Champa")
print(flowers)
flowers.pop(2)
print("The array after removing the 3rd item:",flowers)