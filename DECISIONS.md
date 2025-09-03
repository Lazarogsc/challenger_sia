# Documentação de Decisões

### Análise de Sentimento: Abordagem de Regras

A análise de sentimento do projeto foi implementada usando uma abordagem baseada em regras simples, com listas de palavras-chave positivas e negativas. Essa escolha foi feita porque:

* **Simplicidade:** A implementação é rápida e direta, sem a necessidade de um conjunto de dados de treinamento ou de um modelo de machine learning (ML).
* **Adequação ao Objetivo:** Para o objetivo deste case, que é demonstrar um protótipo funcional, a abordagem de regras é suficiente para dar uma noção geral do sentimento das notícias, mesmo com suas limitações.

É importante notar que, como indicado no painel, esta abordagem não é capaz de capturar detalhes como sarcasmo ou contextos mais complexos. Para uma análise mais robusta, um modelo de ML pré-treinado seria necessário.

### Tratamento de Erros

O código foi projetado para lidar com possíveis falhas na coleta de dados. Especificamente, o `app.py` verifica se o DataFrame retornado pela função de coleta está vazio. Se não houver notícias para o termo de busca, uma mensagem de aviso (`st.warning("Nenhuma notícia encontrada.")`) é exibida ao usuário, em vez de o aplicativo travar.

### Uso de IA Generativa

Este projeto foi desenvolvido com o auxílio de um modelo de IA Generativa. A IA foi usada para:

* **Refinar o código-fonte:** Sugestões de melhoria em trechos de código para otimizar a clareza e a eficiência.
