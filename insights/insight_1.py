import plotly.graph_objects as go
import streamlit as st
from data import receita_data

df = receita_data()

def exibir_insight_1():

    data = df.copy()

    # Renomear as colunas de forma resumida
    for i, column in enumerate(df.columns[-9:], start=1):
        data = data.rename(columns={column: f'col{i}'})

    # Gráfico 1
    with st.container():
    
                st.title('Houve crescimento e declínio nos rendimentos A DEPENDER da área da prestação de serviços decorrente do transporte de passageiros na pandemia')

                i_1 = data[['Ano Calendário', 'col3']].groupby('Ano Calendário').sum().reset_index()

                fig = go.Figure()

                fig.add_trace(go.Bar(
                    x=i_1['Ano Calendário'],
                    y=i_1['col3'],
                    marker=dict(color=['#B22222' if x == 2020 else '#1f77b4' for x in i_1['Ano Calendário']]), 
                ))

                for idx, row in i_1.iterrows():
                    fig.add_annotation(
                        x=row['Ano Calendário'],
                        y=row['col3'] + 15,  
                        text=f'{row["col3"]:.0f}',
                        showarrow=False,
                        font=dict(size=10, color='black'),
                        align='center'
                    )

                x_pos = i_1[i_1['Ano Calendário'] == 2020]['Ano Calendário'].values[0]
                y_pos = i_1[i_1['Ano Calendário'] == 2020]['col3'].values[0]

                fig.add_annotation(
                    x=2020,
                    y=y_pos + 100,
                    text='Queda na Pandemia',
                    arrowhead=2,
                    arrowsize=1.5,
                    arrowcolor='#B22222',
                    font=dict(size=12, color='black')
                )

                fig.update_layout(
                    title="Rendimento de prestação de serviços decorrente do transporte de passageiros por ano\n (crescimento e decrescimento em 2020)",
                    xaxis_title='Ano Calendário',
                    yaxis_title='Lucro (em milhões R$)',
                    yaxis=dict(range=[0, 900]),
                    template="plotly_white",
                    showlegend=False
                )

                st.plotly_chart(fig)

    # Gráfico 2
    with st.container():
                # Faixas e cores
                faixas = ['Até 1/2', 'De 1/2 a 1', 'De 1 a 2', 'De 2 a 3']
                cores = ['#006400', '#006400', '#B22222', '#B22222']
                labels = ['Até 1/2 Salários Mínimos', 'De 1/2 a 1 Salários Mínimos', 'De 1 a 2 Salários Mínimos', 'De 2 a 3 Salários Mínimos']

                fig = go.Figure()

                for faixa, cor, label in zip(faixas, cores, labels):
                    dados_antes = data[(data['Faixa de Salários-Mínimos'] == faixa) & (data['Ano Calendário'] <= 2019)]
                    dados_depois = data[(data['Faixa de Salários-Mínimos'] == faixa) & (data['Ano Calendário'] >= 2019)]
                    
                    fig.add_trace(go.Scatter(x=dados_antes['Ano Calendário'], 
                                            y=dados_antes['col3'], 
                                            mode='lines', 
                                            line=dict(color=cor), 
                                            name=label, 
                                            showlegend=False))
                    
                    fig.add_trace(go.Scatter(x=dados_depois['Ano Calendário'], 
                                            y=dados_depois['col3'], 
                                            mode='lines+markers', 
                                            line=dict(color=cor, dash='dash'), 
                                            name=label))

                fig.add_shape(
                    type="rect",
                    x0=2020 - 0.5, y0=0, x1=2020 + 0.5, y1=max(data['col3']),
                    fillcolor="red", opacity=0.3, line=dict(color="red"),
                    name="Pandemia (2020)"
                )

                fig.add_annotation(
                    x=2020, y=max(data['col3']) * 0.8,
                    text="Pandemia",
                    showarrow=True, arrowhead=2, arrowsize=1,
                    ax=100, ay=-30,
                    font=dict(size=16, color="black"),
                    arrowcolor="black"
                )

                fig.add_annotation(
                    x=2016, y=90,  
                    text="Acima de 1 salário mínimo, <br> todos os lucros caíram em 2020",
                    showarrow=False,
                    font=dict(size=10, color="black", family="Arial", weight="bold"),  
                    align="center"
                )

                for faixa, label in zip(['Até 1/2', 'De 1/2 a 1', 'De 1 a 2', 'De 2 a 3'], 
                                        ['Uber, 99, táxis tradicionais, etc', 'Uber, 99, táxis tradicionais, etc', 
                                        'Transporte aéreo, táxi de alta renda, etc', 'Transporte aéreo, táxi de alta renda, etc']):
                    
                    faixa_data = data[data['Faixa de Salários-Mínimos'] == faixa]
                    ponto_2020 = faixa_data[faixa_data['Ano Calendário'] == 2020]
                    
                    if not ponto_2020.empty:
                        x = ponto_2020['Ano Calendário'].iloc[0]
                        y = ponto_2020['col3'].iloc[0]
                        
                        fig.add_annotation(
                            x=x, y=y+5,
                            text=label,
                            showarrow=True, arrowhead=2, arrowsize=1,
                            ax=60, ay=-30,
                            font=dict(size=10, color="black"),
                            arrowcolor="black"
                        )

                fig.update_layout(
                    title="Rendimento de prestação de serviços decorrente do transporte de passageiros por ano\n (crescimento e decrescimento em 2020)",
                    xaxis_title="Ano Calendário",
                    yaxis_title="Lucro (em milhões R$)",
                    legend_title="Faixa de Salário",
                    template="plotly_white",
                    hovermode="closest"
                )

                st.plotly_chart(fig)    

    # Textos
    with st.container():
                
                # Título
                st.header("Motivos")

                # Seção para até 1 salário mínimo
                st.subheader("Até 1 salário mínimo")
                st.markdown("""
                Houve aumento de rendimento pelos seguintes motivos em 2020:

                - **Mudança na demanda e comportamento do consumidor**: Durante a pandemia, muitas pessoas passaram a evitar o transporte público devido ao risco de contágio, preferindo opções mais seguras, como o transporte individual. Isso levou a um aumento na demanda por serviços de transporte por aplicativos (como Uber, 99 e outros), que são usados, em grande parte, por motoristas de baixa renda.

                - **Mesmo com restrições de mobilidade**: o transporte de passageiros se manteve relevante para deslocamentos essenciais, e muitas pessoas estavam dispostas a pagar mais por viagens de forma mais segura.

                - **Flexibilidade nos horários**: Muitos motoristas de aplicativos tiveram mais flexibilidade para trabalhar em horários alternativos ou em horários mais vantajosos, aproveitando a mudança nos padrões de mobilidade da população.

                - **Essa flexibilidade permitiu que esses trabalhadores** conseguissem melhorar sua renda, ajustando-se à demanda e oferecendo mais disponibilidade de serviço.

                Fonte: [Uber Datafolha](https://www.uber.com/pt-BR/newsroom/datafolha-bicicleta-e-apps-como-uber-sao-os-transportes-mais-seguros-durante-a-pandemia-para-brasileiros-sem-carro/)
                """)

                st.image("assets/i1_3.png")

                # Seção para acima de 1 salário mínimo
                st.subheader("Acima de 1 salário")
                st.markdown("""
                Houve diminuição de rendimento pelos seguintes motivos em 2020:

                - **Redução da demanda**: A pandemia provocou uma queda significativa na demanda por viagens e transportes de luxo ou não essenciais. Por exemplo, o setor de transporte aéreo sofreu uma queda drástica na quantidade de passageiros devido ao fechamento de fronteiras e à redução de viagens. Empresas de táxi de alta renda também enfrentaram queda nas corridas devido ao medo do contágio e à redução da mobilidade urbana.

                Fonte: [CNT - Transporte durante a pandemia](https://cnt.org.br/agencia-cnt/segmentos-do-transporte-de-passageiros-entre-os-mais-afetados-pela-crise-da-covid-19)
                """)

                st.image("assets/i1_4.png")