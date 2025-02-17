import pandas as pd

def receita_data():
    receita = pd.read_csv('data/rendimentos-isentos-e-nao-tributaveis.csv', sep=';')

    receita = receita.drop_duplicates()
    colunas_objeto = receita.select_dtypes(include=['object']).columns
    colunas_a_converter = colunas_objeto.difference([colunas_objeto[0]])
    receita[colunas_a_converter] = receita[colunas_a_converter].apply(lambda x: x.str.replace(',', '.')).apply(pd.to_numeric, errors='coerce')
    receita=receita[receita['Ano Calendário']>=2016]

    ordem=['Até 1/2', 'De 1/2 a 1', 'De 1 a 2', 'De 2 a 3', 'De 3 a 5',
       'De 5 a 7', 'De 7 a 10', 'De 10 a 15', 'De 15 a 20', 'De 20 a 30',
       'De 30 a 40', 'De 40 a 60', 'De 60 a 80', 'De 80 a 160',
       'De 160 a 240', 'De 240 a 320', 'Mais de 320']

    # Garantir que a coluna 'Faixa de Salários-Mínimos' seja categórica e ordenada
    receita['Faixa de Salários-Mínimos'] = pd.Categorical(receita['Faixa de Salários-Mínimos'],categories=ordem,ordered=True)
    return receita

