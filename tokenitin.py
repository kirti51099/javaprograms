from nltk.tokenize import word_tokenize, sent_tokenize
#tokenization
text="hello,world!'How are you?"
words=nltk.word_tokenize(text)
print(words)