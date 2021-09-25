import requests
from bs4 import BeautifulSoup #pip install bs4(Windows)
import pandas as pd #pip install pandas(Windows)
from datetime import datetime
import os


#Alunos: Guilherme, Philipe, Victória

#Para essa solução pensamos em uma estratégia a fim de garantir a funcionalidade do código mesmo com futuras alterações
#e/ou extensões e previnir que as mudanças feitas em um módulo de propague para outros. Nesse caso nossa função newsGeneric()
#recebe como paramentro a url do site de noticia desejado, um array com as classes para pesquisa e o nome do arquivo.csv que o 
#usuário gostaria que guardasse os dados. Dessa forma é possível que a função seja feita para
#diferentes sites de notícias, mudando apenas os parametros desejados, construímos assim um módulo aberto para extensão

#Funçao generica que recebe como entrada a url do site do pagina
# e um array com as classes para a pesquisa no site.
# A funçao pega as informaçoes do html de uma pagina e
# junta a informaçao relevante em uma lista
def newsGeneric(url, classes):

    lista_noticias = []
    conteudo = requests.get(url).text
    
    soup = BeautifulSoup(conteudo, "lxml")
    noticias = soup.findAll('div', attrs={'class': classes})
    
    for noticia in noticias:
        titulo = noticia.find('a')  
        link = titulo.get('href')
        lista_noticias.append([titulo.text, link])
    
    return lista_noticias


#Coloca em um arquivo csv a lista das noticias de um site
def news_to_csv(lista_noticias, file_name):
    now = datetime.now()
    file_path = os.path.join("News",  now.strftime("%m_%d_%Y") + "_" + file_name)
    news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Link'])
    news.to_csv(file_path, index=False)    


news = newsGeneric("https://g1.globo.com/", 'feed-post-body')
news_to_csv(news, "g1.csv")

news = newsGeneric("https://www.estadao.com.br/", 'intro')
news_to_csv(news, "estadao.csv")

news = newsGeneric("https://www.uol.com.br/", ['submanchete submanchete-destaque submanchete-ultimo has-image','mod-hibrido-manchete area-default manchete-editorial', 'chamada chamada-imagem'])
news_to_csv(news, "uol.csv")
