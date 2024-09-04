def input(n1,n2):
    print("The first number is:",n1)
    print("The second number is:",n2)
    
print("Call to function")
input(25,30)

#Using Arguments
def function(n1,n2=20):
    print("First number is:",n1)
    print("Second number is:",n2)
print("Passing only one argument")
function(40)

print("Passing two arguments:")
function(50,30)
