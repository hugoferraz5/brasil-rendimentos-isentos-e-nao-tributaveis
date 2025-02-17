import plotly.graph_objects as go
import streamlit as st
from data import receita_data

df = receita_data()

def exibir_insight_2():

    data = df.copy()

    # Renomear as colunas de forma resumida
    for i, column in enumerate(df.columns[-9:], start=1):
        data = data.rename(columns={column: f'col{i}'})

    # Gráfico 1
    with st.container():
    
                st.title('Na pandemia houve um crescimento nas atividades rurais')

                i_2 = data[['Ano Calendário','col6']].groupby('Ano Calendário').sum().reset_index()

                fig = go.Figure()

                fig.add_trace(go.Bar(
                    x=i_2['Ano Calendário'],
                    y=i_2['col6'],
                    marker=dict(color=['#006400' if x == 2020 else '#1f77b4' for x in i_2['Ano Calendário']]),  # Coloca a cor vermelha para o ano de 2020
                ))

                for idx, row in i_2.iterrows():
                    fig.add_annotation(
                        x=row['Ano Calendário'],
                        y=row['col6'] + 2000,  
                        text=f'{row["col6"]:.0f}',
                        showarrow=False,
                        font=dict(size=10, color='black'),
                        align='center'
                    )


                x_pos = i_2[i_2['Ano Calendário'] == 2020]['Ano Calendário'].values[0]
                y_pos = i_2[i_2['Ano Calendário'] == 2020]['col6'].values[0]

                fig.add_annotation(
                    x=2020,
                    y=y_pos + 5000,
                    text='Aumento na \n Pandemia',
                    arrowhead=2,
                    arrowsize=1.5,
                    arrowcolor='#B22222',
                    font=dict(size=14, color='black')
                )  
                
                    
                fig.update_layout(
                    title="Rendimento sobre parcela isenta correspondente à atividade rural por ano\n (crescimento e decrescimento em 2020)",
                    xaxis_title='Ano Calendário',
                    yaxis_title='Lucro (em milhões R$)',
                    yaxis=dict(range=[0, 95000]),
                    template="plotly_white",
                    showlegend=False
                )

                st.plotly_chart(fig)

    # Gráfico 2
    with st.container():
                
                faixas = ['De 80 a 160', 'De 160 a 240', 'De 240 a 320', 'Mais de 320']
                cores = ['#006400', '#006400', '#006400', '#006400']
                labels = ['De 80 a 160 Salários Mínimos', 'De 160 a 240 Salários Mínimos', 'De 240 a 320 Salários Mínimos',
                        'Mais de 320 Salários Mínimos']

                fig = go.Figure()

                for faixa, cor, label in zip(faixas, cores, labels):
                    dados_antes = data[(data['Faixa de Salários-Mínimos'] == faixa) & (data['Ano Calendário'] <= 2019)]
                    dados_depois = data[(data['Faixa de Salários-Mínimos'] == faixa) & (data['Ano Calendário'] >= 2019)]
                    
                    
                    fig.add_trace(go.Scatter(x=dados_antes['Ano Calendário'], 
                                            y=dados_antes['col6'], 
                                            mode='lines', 
                                            line=dict(color=cor), 
                                            name=label, 
                                            showlegend=False))
                    
                    fig.add_trace(go.Scatter(x=dados_depois['Ano Calendário'], 
                                            y=dados_depois['col6'], 
                                            mode='lines+markers', 
                                            line=dict(color=cor, dash='dash'), 
                                            name=label))
                    
                    
                    
                fig.add_shape(
                    type="rect",
                    x0=2020 - 0.5, y0=0, x1=2020 + 0.5, y1=max(data['col6']),
                    fillcolor="red", opacity=0.3, line=dict(color="red"),
                    name="Pandemia (2020)"
                )


                fig.add_annotation(
                    x=2020, y=max(data['col6']) * 0.6,
                    text="Pandemia",
                    showarrow=True, arrowhead=2, arrowsize=1,
                    ax=100, ay=-30,
                    font=dict(size=16, color="black"),
                    arrowcolor="black"
                )

                fig.add_annotation(
                    x=2016, y=10000,  
                    text="Todas as faixas salariais <br> aumentaram os lucros em 2020",
                    showarrow=False,
                    font=dict(size=10, color="black", family="Arial", weight="bold"),  
                    align="center"
                )

                for faixa, label in zip(['De 80 a 160', 'De 160 a 240', 'De 240 a 320', 'Mais de 320'], 
                                        ['Crescente', 'Crescente', 'Crescente', 'Crescente']):
                    
                    faixa_data = data[data['Faixa de Salários-Mínimos'] == faixa]
                    ponto_2020 = faixa_data[faixa_data['Ano Calendário'] == 2020]
                    
                    if not ponto_2020.empty:
                        x = ponto_2020['Ano Calendário'].iloc[0]
                        y = ponto_2020['col6'].iloc[0]
                        
                        fig.add_annotation(
                            x=x, y=y+400,
                            text=label,
                            showarrow=True, arrowhead=2, arrowsize=1,
                            ax=10, ay=-50,
                            font=dict(size=10, color="black"),
                            arrowcolor="black"
                        )
                    
                    
                fig.update_layout(
                    title="Rendimento sobre parcela isenta correspondente à atividade rural por ano\n (crescimento e decrescimento em 2020)",
                    xaxis_title="Ano Calendário",
                    yaxis_title="Lucro (em milhões R$)",
                    legend_title="Faixa de Salário",
                    template="plotly_white",
                    hovermode="closest"
                )

                st.plotly_chart(fig)    

    # Textos
    with st.container():
                
                st.header("Motivos")

                st.markdown("""
                - **Demanda externa**: O Brasil é um grande exportador de produtos agrícolas, como soja, milho, carne, entre outros. Durante a pandemia, muitos países continuaram importando esses produtos, o que impulsionou as exportações brasileiras, principalmente a países como China.

                - **Setor essencial**: A agricultura foi considerada um setor essencial durante a pandemia, o que permitiu que a produção continuasse mesmo com as restrições impostas em outros setores da economia.

                - Percebemos que o setor rural beneficia mais quem tem maiores rendas por serem proprietários de terras, logo é autoexplicativo as maiore rendas.


                Produtores e economistas consultados pelo G1 afirmam que os fatores ajudaram a impulsionar o agro em 2020 foram:
                - A safra recorde de grãos de 257,8 milhões de toneladas em 2019/2020;
                - Investimento dos produtores em pacotes tecnológicos avançados - sementes, defensivos, fertilizantes e rações de maior qualidade;
                - Clima favorável;
                - Demanda externa aquecida - receio de desabastecimento de alimentos por causa do fechamento de fronteiras * impulsionou importações dos países. E Brasil é um grande exportador do setor;
                - Agro foi considerado uma atividade essencial durante a pandemia para evitar falta de mantimentos;
                - Auxílio emergencial aqueceu a demanda interna;
                - Valorização do dólar em relação ao real impulsionou exportações do agro;
                - Recomposição do rebanho suíno chinês após peste suína africana puxou vendas de soja e milho do Brasil - grãos viram ração para os animais;
                - Aumento da produção e exportação de carnes.

                Fonte: https://g1.globo.com/economia/agronegocios/noticia/2021/03/03/agropecuaria-foi-o-unico-setor-que-cresceu-no-pib-de-2020-entenda.ghtml
                                """)

                st.image("assets/i2_3.png")

       