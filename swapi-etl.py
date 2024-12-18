import os
import re
import requests
import pandas as pd

os.makedirs("raw", exist_ok=True)
os.makedirs("work", exist_ok=True)

URLS = {
    "people": "https://swapi.py4e.com/api/people/",
    "planets": "https://swapi.py4e.com/api/planets/",
    "films": "https://swapi.py4e.com/api/films/",
}

###
def extract(url, quantidade_paginas=5):
    resultados = []
    
    for pagina in range(1, quantidade_paginas + 1):
        response = requests.get(f"{url}{pagina}")
        if response.status_code == 200:
            resultados.append(response.json())
        else:
            print(f"Erro - {url}{pagina}: {response.status_code}")
    return resultados

def transform(dados):
    dados_transformados = []
    for dado in dados:
        dicionario_dados = {}
        for chave, valor in dado.items():
            valor = lower_case(valor)
            valor = caracteres_especiais(valor)
            dicionario_dados[chave] = valor
        dados_transformados.append(dicionario_dados)
    return dados_transformados

def load(dados, arquivo):
    df = pd.DataFrame(dados)
    df.to_csv(arquivo, index=False, encoding="utf-8")
    print(f"Arquivo> {arquivo}")

###
def lower_case(texto):
    if isinstance(texto, str):
        return texto.lower()
    if isinstance(texto, list):
            resultado = []
            for textos in texto:
                resultado.append(lower_case(textos))
            return resultado
    return texto

def caracteres_especiais(texto):
    if isinstance(texto, str):
        texto = texto.replace("\r", " ").replace("\n", " ")
        return re.sub(r"[^a-zA-Z0-9\s]", "", texto)
    if isinstance(texto, list):
        resultado = []
        for textos in texto:
            resultado.append(caracteres_especiais(textos))
        return resultado
    return texto

###
def etl_people():
    print("Processando - Pessoas: ")
    dados = extract(URLS["people"])
    diretorio = os.path.join("raw", "people.csv")
    load(dados, diretorio)
    dados_etl = transform(dados)
    diretorio_etl = os.path.join("work", "people.csv")
    load(dados_etl, diretorio_etl)

def etl_planets():
    print("Processando - Planetas: ")
    dados = extract(URLS["planets"])
    diretorio = os.path.join("raw", "planets.csv")
    load(dados, diretorio)
    dados_etl = transform(dados)
    diretorio_etl = os.path.join("work", "planets.csv")
    load(dados_etl, diretorio_etl)

def etl_films():
    print("Processando - Filmes: ")
    dados = extract(URLS["films"])
    diretorio = os.path.join("raw", "films.csv")
    load(dados, diretorio)
    dados_etl = transform(dados)
    diretorio_etl = os.path.join("work", "films.csv")
    load(dados_etl, diretorio_etl)

if __name__ == "__main__":
    etl_people()
    etl_planets()
    etl_films()