# Monitoramento de Percepção Pública sobre IA no Piauí

Este projeto foi desenvolvido como parte de um case acadêmico, com o objetivo de monitorar notícias relacionadas a um termo específico.  
A aplicação coleta informações a partir do **Google News RSS**, processa os textos, realiza uma análise de sentimento simples e apresenta os resultados em um painel interativo criado com **Streamlit**.


## Funcionalidades

- Coleta de notícias do Google News RSS a partir de termos definidos pelo usuário.  
- Limpeza de textos para remover HTML e caracteres especiais.  
- Classificação de sentimento baseada em regras, categorizando as notícias em positivo, negativo ou neutro.  
- Painel interativo com:
  - Gráfico de pizza mostrando a distribuição dos sentimentos.  
  - Nuvem de palavras com os termos mais frequentes.  
  - Tabela interativa com as notícias coletadas.  
- Exportação dos dados em formato **CSV** e **JSON**.  


## Tecnologias utilizadas

- Python 3  
- Requests  
- BeautifulSoup4  
- Pandas  
- Matplotlib  
- WordCloud  
- Streamlit  
- PyTest


## Estrutura do projeto

```bash
├── app.py              # Dashboard em Streamlit
├── coleta.py           # Script de coleta e processamento
├── DECISIONS.md        # Documento com justificativas técnicas
├── README.md           # Este arquivo
├── requirements.txt    # Dependências do projeto
├── .env.example        # Exemplo de arquivo .env
├── pytest.ini          # Configurações do Pytest
├── tests/
│   ├── test_main.py    # Testes unitários da aplicação
│   └── conftest.py     # Fixtures do Pytest
```

## Como executar

1. Clone o repositório:

    git clone https://github.com/Lazarogsc/challenger_sia
    cd challenger_sia

2. Crie e ative um ambiente virtual:

    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. Instale as dependências:

    pip install -r requirements.txt

4. Copiar .env:

    cp .env.example .env

5. Execute o Streamlit:

    streamlit run app.py

## Observações de transparência ##

A análise de sentimento utilizada é baseada em regras simples e pode não capturar sarcasmo ou contextos mais complexos.

Durante o desenvolvimento, ferramentas de IA foram utilizadas apenas para sugerir melhorias em trechos de código, com foco em clareza e eficiência. Toda a implementação, integração e testes foram realizados manualmente pelo autor.