from newspaper import Article
import re

def parse(url):
    result = {}
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return({'fulltext': article.text, 'keywords': article.keywords})
    except Exception as err:
        return ({'err01' : 'nie można połączyć się ze wskazanym adresem'})

def countWords (keywords, fulltext):
    result = {}
    if len(keywords) > 0:
        for keyword in keywords:
            result.update({keyword: str(fulltext.count(keyword))})
    else:
        result = {'err02' : 'nie znaleziono słów kluczowych'}

    return (result)
