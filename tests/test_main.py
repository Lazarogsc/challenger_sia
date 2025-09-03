from coleta import classificar_sentimento, limpar_html_e_caracteres_especiais


def test_classificar_sentimento(termo):
    resp = classificar_sentimento(termo)
    assert 'positivo' == resp

def test_limpar_html_e_caracteres_especiais(texto):
    resp = limpar_html_e_caracteres_especiais(texto)
    assert 'Feito no Piauí projeto de IA com base de dados em português é apresentado ao Governo' in resp 