#re.findall
import re
string="""Hello my number is 12345689 and my friend number is 987654321"""
redex='\d+'
match=re.findall(redex,string)
print(match)

#re.compile()
import re
p=re.compile('[a-e]')
print(p.findall("Aye,said mr.Gienson stark"))

import re
p=re.compile('\d')
print(p.findall("i went to him tt 11 AM on 4th july 1886"))
p=re.compile('\d+')
print(p.findall("I went to him at 11 am on 4th july 186"))

import re
p=re.compile('\w')
print(p.findall("He said in some_lang."))
p=re.compile('\w+')
print(p.findall("I went to him at 11 am, he\said *** in some_language."))
p=re.compile('\W')
print(p.findall("he said *** in some_languge."))

import re
p=re.compile('ab*')
print(p.findall("ababbaabbb"))

#split
from re import split
print(split('\W','Words,words,Words'))
print(split('\W+',"Word's words words"))
print(split('\W+','on 12th jan 2016,at 11:02 Am'))
print(split('\d+','on 12th jan 2016, at 11:02 Am'))


#sub()
import re 
print(re.sub('ub','~*','Subject has uber booked already',flags=re.IGNORECASE))
print(re.sub('ub','~*','Subjct has uber booked already'))
print(re.sub('ub','~*','subject has uber booked already',count=1,flags=re.IGNORECASE))
print(re.sub(r'\sAND\s','&','Bake beans and spam',flags=re.IGNORECASE))