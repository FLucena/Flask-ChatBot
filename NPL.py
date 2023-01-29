from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# Natural Language Tool Kit
# Works for Natural Language Processing. Breaks up a sentence or a word in smaller pieces.
# The stop words would be the words to be ignored
# Breaking down text into smaller pieces is called tokenization. 
sentence = "I love ice cream. I also like steak."
print(sent_tokenize(sentence))

print(stopwords.words("english"))
