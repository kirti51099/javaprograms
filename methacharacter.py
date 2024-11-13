#backslash
import re
s='geeks.forgeeks'
match=re.search(r'.',s)
print(match)
match=re.search(r'\.',s)
print(match)

#squareBrackets
import re
string="the quick brown fox jum over the lazy dog"
pattern="[a-m]"
result=re.findall(pattern,string)
print(result)

#caret
import re
regex=r'^The'
strings=['The arrow','The lazy dog','A quick boy']
for string in strings:
    if re.match(regex,string):
        print('Matched:{string}')
    else:
        print('Not matched:{string}')
        
#doller
import re
string="hello world!"
pattern=r"world!$"

match=re.search(pattern,string)
if match:
    print("match found!")
else:
    print("match not found.")
    
#dot(.)
import re
string="Hello programmer"
pattern=r"kirti"
match=re.search(pattern,string)
if match:
    print("Match found")
else:
    print("match not found.")
    
