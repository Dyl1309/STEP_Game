import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')
url = 'https://apple.com'
article = Article(url)
article.download()
article.parse()
article.nlp()
text = article.summary
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
