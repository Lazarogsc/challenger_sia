import os
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

google_baseurl = os.getenv('GOOGLE_RSS_URL')
palavras_positivas = ["avanço", "benefício", "melhora", "solução", "inovação", "sucesso", "promissor", "positivo", "ganho"]
palavras_negativas = ["problema", "risco", "crise", "falha", "ameaça", "prejuízo", "dificuldade", "negativo", "perda"]

def classificar_sentimento(texto):
    texto = texto.lower()
    score_pos = sum(p in texto for p in palavras_positivas)
    score_neg = sum(p in texto for p in palavras_negativas)

    if score_pos > score_neg:
        return "positivo"
    elif score_neg > score_pos:
        return "negativo"
    else:
        return "neutro"
    

def limpar_html_e_caracteres_especiais(texto_html):
    
    texto = BeautifulSoup(texto_html or '', "html.parser").get_text()
    texto = re.sub(r'[^\w\sÀ-ÿ]', '', texto, flags=re.UNICODE)

    return texto.strip()


def coleta_googlerss(termo, qty_noticias):
 
    resp = requests.get(f'{google_baseurl}/search?q={termo}&hl=pt-br&gl=BR&ceid=BR:pt-br')
    root = ET.fromstring(resp.content)  # Converte o XML em raiz de árvore
    noticias = []

    for item in root.findall('.//item'):
        titulo = item.find('title').text
        link = item.find('link').text
        pubDate = item.find('pubDate').text
        desc_html = item.find('description').text or ''
        desc_html = limpar_html_e_caracteres_especiais(desc_html)
        sentimento = classificar_sentimento(titulo + " " + desc_html)
        noticia = {
            'title': titulo,
            'link': link,
            'descr': desc_html,
            'pubDate': pubDate,
            'sentimento': sentimento
        }

        noticias.append(noticia)
    
    print(noticias)
    
                 
    return pd.DataFrame(noticias[:qty_noticias])