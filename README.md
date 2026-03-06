# Data-Science-coleta_dados_python
**Coleta de dados do curso Ciência de Dados - EBAC.**
# 📊 Coleta de Dados

## 📌 Visão Geral

Este projeto explora diferentes técnicas de **coleta de dados utilizando Python**, abordando métodos comuns utilizados em projetos de ciência de dados para obter informações de diversas fontes.

Foram estudadas abordagens como **consumo de APIs, web scraping, extração de tabelas HTML e geração de dados sintéticos**, permitindo compreender como dados podem ser coletados, estruturados e preparados para análise.

O projeto tem caráter educacional e serve como base para entender a **primeira etapa do pipeline de dados: Data Collection**.

---

## 🎯 Objetivos do Projeto

- Compreender o funcionamento de **requisições HTTP**
- Realizar **coleta de dados via API**
- Extrair informações de páginas web através de **Web Scraping**
- Identificar e extrair **tabelas HTML com Pandas**
- Simular bases de dados através de **dados sintéticos**
- Praticar a organização de scripts de coleta de dados

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Requests** — requisições HTTP e consumo de APIs  
- **BeautifulSoup (bs4)** — parsing e navegação em HTML  
- **Pandas** — manipulação e extração de tabelas  
- **Faker** — geração de dados fictícios para testes  

---

## 📂 Estrutura do Projeto
    coleta-de-dados/
    │
    ├── coleta_dados_web.py
    ├── coleta_dados_basica.py
    ├── coleta_dados_api.py
    ├── gerar_dados.py
    ├── estudo_dataframe_ciencias.py
    │
    ├── Dados.csv
    └── README.md

---
  
**Descrição dos arquivos:**

- **coleta_dados_web.py**  
  Script de web scraping para extração de títulos, parágrafos e links em páginas HTML.

- **coleta_dados_basica.py**  
  Exemplo simples de coleta de dados através de requisições HTTP.

- **coleta_dados_api.py**  
  Script para interação com API, incluindo upload e download de arquivos.

- **gerar_dados.py**  
  Geração de dados fictícios utilizando a biblioteca Faker para simulações.

- **estudo_dataframe_ciencias.py**  
  Exploração de tabelas HTML utilizando Pandas.

- **Dados.csv**  
  Exemplo de dataset utilizado para testes e manipulação.

---

## 🌐 Coleta de Dados via API

Foi utilizada a biblioteca **Requests** para realizar requisições HTTP e interagir com serviços externos.

Foram implementadas funções para:

- **Upload de arquivos**
- **Upload autenticado com chave de API**
- **Download de arquivos via URL**

Essas operações simulam cenários comuns em pipelines de dados que envolvem integração com APIs.

---

## 🕸️ Web Scraping

O projeto também explora **extração de informações de páginas web** utilizando a biblioteca **BeautifulSoup**.

Foram analisadas páginas como:

- https://books.toscrape.com (site educacional)
- https://valor.globo.com

A extração inclui:

- Títulos (`h2`)
- Parágrafos (`p`)
- Links (`a`)

Além da identificação da quantidade de elementos encontrados e da análise da estrutura HTML.

---

## 📊 Extração de Tabelas com Pandas

Utilizando o método:

```python
pd.read_html()
