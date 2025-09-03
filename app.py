import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
from coleta import coleta_googlerss

def app():

    st.set_page_config(page_title="Monitoramento de Notícias", layout="wide")

    st.markdown("## 📊 Monitoramento de Percepção Pública sobre IA no Piauí")
    st.markdown("---")

    termo = st.text_input("Digite o termo de busca:", "Inteligência Artificial Piauí")

    qtd = st.slider(
        "Quantidade de notícias",
        min_value=10,
        max_value=15,
        value=10,      
        step=1         
    )


    if st.button("Coletar Notícias"):
        df = coleta_googlerss(termo, qtd)

        if df.empty:
            st.warning("Nenhuma notícia encontrada.")
        else:
        
            col1, col2 = st.columns([1, 2])  
        
            with col1:
                st.subheader("Distribuição de Sentimentos")
                contagem = df['sentimento'].value_counts()
                fig1, ax1 = plt.subplots(figsize=(2.5, 2.5))
                cores = ['#66b3ff','#ff9999','#99ff99']  
                ax1.pie(
                    contagem, 
                    labels=contagem.index, 
                    autopct='%1.1f%%', 
                    startangle=90, 
                    colors=cores[:len(contagem)],
                    textprops={'fontsize': 9}
                )
                ax1.axis("equal")
                plt.tight_layout()
                st.pyplot(fig1)

            
            with col2:
                st.subheader("Nuvem de Palavras (descrições)")
                texto_unico = " ".join(df['descr'].astype(str))
                if texto_unico.strip():
                    wc = WordCloud(
                        width=600, height=300, background_color="white",
                        colormap="tab10"
                    ).generate(texto_unico)
                    fig2, ax2 = plt.subplots(figsize=(6, 3))
                    ax2.imshow(wc, interpolation="bilinear")
                    ax2.axis("off")
                    plt.tight_layout()
                    st.pyplot(fig2)
                else:
                    st.info("Sem descrições suficientes para gerar nuvem de palavras.")

            st.markdown("### 📰 Tabela de Notícias")
            st.dataframe(df)

            col_csv, col_json = st.columns(2)
            col_csv.download_button(
                label="📥 Baixar CSV",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="noticias.csv",
                mime="text/csv"
            )
            col_json.download_button(
                label="📥 Baixar JSON",
                data=df.to_json(orient="records", force_ascii=False).encode("utf-8"),
                file_name="noticias.json",
                mime="application/json"
            )


    st.markdown("---")
    st.caption("⚠️ Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos.")

if __name__ == "__main__":
    app()
