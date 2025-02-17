import plotly.express as px
import streamlit as st
from data import receita_data
from utils import colunas
from insights.insight_1 import exibir_insight_1
from insights.insight_2 import  exibir_insight_2


# Dado importa
df = receita_data()

st.set_page_config(layout="wide")

# Sidebar
with st.sidebar:
    st.image("assets/rir.jpg",  width=250)

    compare_opts = st.multiselect("Escolha uma fonte de rendimento:",colunas[2:],
                                  'Bolsas de estudo e de pesquisa caracterizadas como doação, exceto médico-residente ou Pronatec, exclusivamente para proceder a estudos ou pesquisas e desde que os resultados dessas atividades não representem vantagem para o doador, nem importem contraprestação de serviços',max_selections=1)

    # botões de insights na sidebar
    st.header('Insights')

    insight_1 = st.sidebar.button('Insight 1')
    insight_2 = st.sidebar.button('Insight 2')
    insight_3 = st.sidebar.button('Gráficos')

# Container 1
with st.container():
    # st.image("assets/imposto.jpg")
    st.markdown(
        """
        <style>
        .header {
            background-color: #054163; 
            color: white;
            padding: 10px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h1 style="color: white;" class='header'>Base de Dados - Rendimentos Isentos e Não Tributáveis 2016-2020</h1>
        """,
        unsafe_allow_html=True
    )

    expc_atual = 1

    if compare_opts:
        df_filtrado = df[['Ano Calendário','Faixa de Salários-Mínimos',compare_opts[0]]]
    else:
        df_filtrado = df

    st.dataframe(df_filtrado, use_container_width=True)


if not insight_1:
    if not insight_2:
            #Container 2
            with st.container():
                if compare_opts:
                    if compare_opts[0] != 'Ano Calendário':
                        if compare_opts[0] != 'Faixa de Salários-Mínimos':
                            
                            st.title("Análise das Receitas")
                            st.subheader("Fonte de Rendimentos escolhida:")
                            st.markdown(compare_opts[0])

                            # st.header("Gráfico Boxplot")
                            df_filtrado = df[['Ano Calendário','Faixa de Salários-Mínimos',compare_opts[0]]]

                            options = [2016, 2017, 2018, 2019, 2020]
                            selection = st.segmented_control("**Escolha o ano:**", options, 
                                                             selection_mode="single")
                            if selection:
                                
                                df_selecionado = df_filtrado[df_filtrado['Ano Calendário'] == selection]

                                fig = px.box(df_selecionado, x='Ano Calendário', y=compare_opts[0], 
                                             title='Receitas por Ano',custom_data=['Faixa de Salários-Mínimos'])
                                
                            else:

                                fig = px.box(df_filtrado, x='Ano Calendário', y=compare_opts[0], title='Receitas por Ano',
                                            custom_data=['Faixa de Salários-Mínimos'])

                            fig.update_traces(boxpoints='all', jitter=0.05,
                                                hovertemplate='%{customdata[0]}',
                                                line=dict(color='green', width=3))

                            fig.update_layout(
                                    title='Receitas do ano',
                                    xaxis_title='Ano Calendário',
                                    yaxis_title='Receitas (em milhões R$)',
                                    font=dict(size=12),
                                    height=600
                                )

                            st.plotly_chart(fig)

            # Container 3
            with st.container():
                if compare_opts:
                    if compare_opts[0] != 'Ano Calendário':
                        if compare_opts[0] != 'Faixa de Salários-Mínimos':
                            # st.header("Gráfico Histograma")
                            df_filtrado = df[['Ano Calendário','Faixa de Salários-Mínimos',compare_opts[0]]]

                            if selection:
                                
                                df_selecionado = df_filtrado[df_filtrado['Ano Calendário'] == selection]

                                fig = px.bar(df_selecionado[df_selecionado['Ano Calendário']==selection],
                                        x='Faixa de Salários-Mínimos',
                                        y=compare_opts[0],  
                                        labels={'Faixa de Salários-Mínimos': '',
                                                compare_opts[0]: 'Receita (em milhões R$)'},
                                        title=f'Receitas do ano de '+str(selection)+' por Faixa Salarial',
                                        height=800)
                            
                            else:

                                anos = [2016, 2017, 2018, 2019, 2020]

                                fig = px.bar(df_filtrado[df_filtrado['Ano Calendário'].isin(anos)],
                                            x='Faixa de Salários-Mínimos',
                                            y=compare_opts[0],
                                            facet_col='Ano Calendário',  
                                            labels={'Faixa de Salários-Mínimos': '',
                                                    compare_opts[0]: 'Receita (em milhões R$)'},
                                            title=f'Receitas por Faixa Salarial por Ano (R$)',
                                            height=800)

                            fig.update_layout(
                                xaxis_tickangle=90,  
                                showlegend=False,  
                                template="plotly_white" ,
                            )

                            st.plotly_chart(fig)



            # Container 4
            with st.container():
                if compare_opts:
                    if compare_opts[0] != 'Ano Calendário':
                        if compare_opts[0] != 'Faixa de Salários-Mínimos':

                            df_filtrado = df[['Ano Calendário','Faixa de Salários-Mínimos',compare_opts[0]]]

                            df_filtrado3 = df_filtrado[['Ano Calendário',compare_opts[0]]].groupby('Ano Calendário').sum().reset_index()

                            fig = px.line(df_filtrado3, x='Ano Calendário', y=compare_opts[0], 
                                            title="Receitas por Ano",
                                            labels={'Ano Calendário': 'Ano Calendário', compare_opts[0]: 'Receita (em milhões R$)'},
                                            range_y=[0, 1.1*df_filtrado3[compare_opts[0]].max()],
                                            markers=True)

                            st.plotly_chart(fig)


# Container 4 - INSIGHTS
with st.container():

    if insight_1:

        exibir_insight_1()

    elif insight_2:

        exibir_insight_2()

