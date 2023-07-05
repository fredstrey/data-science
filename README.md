# data-science

O projeto 1: analise_de_sentimento_chatgpt.ipynb

faz uma raspagem de dados em tweets utilizando a biblioteca snscrape. 
Os tweets são armazenados em um data frame e posteriormente feita analise de sentimento utilizando o chat GPT, através da biblioteca OpenAi

O projeto 2:titanicDS.ipynb

faz parte de um dos desafios clássico de ciência de dados do kaggle, em que é feito um modelo que utiliza um banco de dados com
informações dos tripulante e cria um modelo que tenta prever se uma pessoa sobreviveu ou não ao naufrágio do navio Titanic em 1909. 
Os resultados da previsão foram salvos no arquivo base_submission (o resultado apresenta 1 se a pessoa sobreviveu e 0 se a pessoa morreu).

O projeto 3 webscrapping.ipynb

utilizando a biblioteca BeautifulSoup para fazer raspagem de dados no site do mercado livre, o algoritmo salva as informações referentes ao titulo do anuncio e preço do produto num arquivo csv product_data.csv

O projeto 4: cafe.ipynb

constitui de uma analise preditiva da produção de cafe no brasil em que, utilizando dados disponibilizados no site https://www.fao.org/faostat/en/#data/QCL, é construído um modelo preditivo utilizando sklearn com médoto de regressão linear de ML. 

O projeto 5: dota2.ipynb

Modelo que busca prever a probabilidade de vitoria de times proficionais em campeonatos de Dota 2. Utilizando como base 
alguns valores médios de estatísicas das partidas (K/D/A, OPM, XPM, LH e Denies), usando dados de majors e dpcs passados 
o modelo tenta prever a winrate dos times da major de Bali utilizando resultados parciais referentes ao dia 05/07/2023.
(bases de dado disponiveis em www.datdota.com)
O modelo ajuda a identificar equipes que estão tendo melhores resultados ao longo do campeonato, podendo ser util para prever o vencedor (o time que apresentar maior winrate).
