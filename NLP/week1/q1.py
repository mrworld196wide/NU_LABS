import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
with open ('input.txt') as f:
    text=f.read()
print("Text:", text)

tokens = word_tokenize(text.lower())
print("Tokens:", tokens)
english_stopwords = stopwords.words('english')
tokens_wo_stopwords = [t for t in tokens if t not in english_stopwords]
print("")
print(tokens_wo_stopwords)
#analyze
print(" ")
print("before stopwards:",len(tokens))
print(" ")
print("after stopwards:",len(tokens_wo_stopwords))