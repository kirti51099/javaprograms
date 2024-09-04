with open('example.txt','w')as f:
    f.write('hello this is a line of text\n')
    f.write('this s another line f text \n')
    
with open('example.txt','r') as f:
    content=f.read()
    print(content)
    
