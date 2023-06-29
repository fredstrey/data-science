import snscrape.modules.twitter as sntwitter
import pandas as pd
import openai

openai.api_key = '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'
maxtweets = 20
i = 0
listatweet = []

for tweet in sntwitter.TwitterSearchScraper('Felipe Neto since:2023-06-28 until:2023-06-29').get_items():
    if i >= maxtweets: 
        break
    listatweet.append([tweet.date, tweet.url, tweet.username, tweet.content])
    i += 1

tweets_df = pd.DataFrame(listatweet, columns=['data', 'url', 'username', 'conteudo'])
 

sentiment_scores = []

for tweet in tweets_df['conteudo']:
    prompt = f"Analyze the sentiment of the following tweet about Felipe Neto:\n{tweet}\nand tell me if it is positive, negative, or neutral (return me only with negative, neutral and positive entrys)."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,  
        n=1,
        stop=None,
        temperature=0.7
    )
   
    sentiment_scores.append(sentiment)
positivo=0
negativo=0
print(sentiment_scores)
for score in sentiment_scores:
  if 'positive' in score:
    positivo+=1
  if 'negative' in score:
    negativo+=1
tweets_df
print("tweets positivos: " + str(positivo))
print("tweets negativos: " + str(negativo))
print("tweets neutros: " + str(abs(positivo+negativo-maxtweets)))
tweets_df
