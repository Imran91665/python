import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sentences = [input("tell something: ")]
for sentence in sentences:
    print(f'For the sentence "{sentence}"')
    polarity = sia.polarity_scores(sentence)
    pos = polarity["pos"]
    neu = polarity["neu"]
    neg = polarity["neg"]
    print(f'The percententage of positive sentiment in :"{sentence}" is : {round(pos*100,2)} %')
    print(f'The percententage of neutral sentiment in :"{sentence}" is : {round(neu*100,2)} %')
    print(f'The percententage of negative sentiment in :"{sentence}" is : {round(neg*100,2)} %')
      