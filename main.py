import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

os.system('cls')

def web_scraping_simple():
    url = 'https://www.creditas.com/exponencial/tabela-imposto-de-renda/'
    response = requests.get(url)
    raw_html = response.text
    html_parser = BeautifulSoup(raw_html,'html.parser')

    tabela = html_parser.find('table')
    if tabela:
        linhas = tabela.find_all('tr')
        dados_tabela = []
        for linha in linhas:
            colunas = linha.find_all('td')
            dados_linha = [coluna.text.strip() for coluna in colunas]  # Extrair o texto das colunas
            dados_tabela.append(dados_linha)

        dados_base = []
        dados_aliq = []
        dados_deduc = []

        dados_tabela.pop(0)

        for i in dados_tabela:
            dados_base.append(i[0])
            dados_aliq.append(i[1])
            dados_deduc.append(i[2])

        dados = {'Base de Cálculo':dados_base,
             'Aliquota':dados_aliq,
             'Dedução do IR':dados_deduc}
    
        planilha = pd.DataFrame(dados)
        print(planilha.head())
        planilha.to_excel('Base de cálculo mensal.xlsx', index=False)
    else:
        print('Não foi possível encotrar a tabela!')

if __name__ == '__main__':
    web_scraping_simple()