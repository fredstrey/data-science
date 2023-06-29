#este codigo utiliza a biblioteca snscrape para fazer scraping de tweets sobre determinado assunto/pessoa, 
#armazena algumas informaçoes desses twwets (data, url, username, conteudo) em um data frame.
#em seguida, utilizando a api do chat gpt, é feita uma analise de sentimento em cada um dos tweets obtidos atraves do webscraping

import snscrape.modules.twitter as sntwitter
import pandas as pd
import openai

openai.api_key = 'insira aqui sua chave' #aqui você deve inserir sua chave pessoal do api do chatgpt
maxtweets = 20 #por simplicidade foi fixado uma quantidade maxima de 20 tweets à serem armazenados no data frame
i = 0
listatweet = []
#este loop for utiliza a ferramenta snscrape para buscar pelos tweets e armazena-los num dataframe tweets_df
for tweet in sntwitter.TwitterSearchScraper('Felipe Neto since:2023-06-28 until:2023-06-29').get_items(): 
    if i >= maxtweets: 
        break
    listatweet.append([tweet.date, tweet.url, tweet.username, tweet.content])
    i += 1

tweets_df = pd.DataFrame(listatweet, columns=['data', 'url', 'username', 'conteudo'])
 

sentiment_scores = []
#neste loop for, utilizamos a api do chatgpt para analizar o sentimento de cada um dos tweets que salvamos 
for tweet in tweets_df['conteudo']:
    prompt = f"Analyze the sentiment of the following tweet about Felipe Neto:\n{tweet}\nand tell me if it is positive, negative, or neutral (return me only with negative, neutral and positive entrys)."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,  
        n=1,
        stop=None,
        temperature=0.7
    #estes sao alguns parametros internos utilizados pela api do chatgpt, utilizei valores padroes 
    )
   #por fim, é feita a contagem de tweets positivos, negativos e neutros e os valores sao exibidos para o usuario
    sentiment = response.choices[0].text.strip() #esta linha garante que apenas o valor do sentimento seja armazenado na lista(negativo,positivo,neutro)
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
