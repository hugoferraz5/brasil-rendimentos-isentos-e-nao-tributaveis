# brasil-declaracao_imposto_de_renda
Realizamos análises exploratórias e explanatórias junto a um dashboard com dados reais sobre rendimentos isentos de tributação ou não-tributáveis, conforme a legislação fiscal brasileira. Através dessas análises, identificamos diversos insights importantes, permitindo uma compreensão aprofundada dos padrões e características desses rendimentos.

Este dataset contém uma lista de rendimentos isentos de tributação ou não-tributáveis, conforme a legislação fiscal brasileira. Ele inclui categorias como bolsas de estudo e pesquisa, ganhos de capital em determinadas condições, lucros e dividendos recebidos, e isenções para aposentadorias e pensões. Esses dados são úteis para a declaração de imposto de renda, pois ajudam a identificar quais rendimentos podem ser informados como isentos, permitindo o correto preenchimento da declaração e a otimização da tributação.

**Agregado dos rendimentos isentos e não tributáveis por faixa de rendimento em salários mínimos.**

Fonte: [rendimentos-isentos-e-nao-tributaveis](https://dados.gov.br/dados/conjuntos-dados/grandes-nmeros-do-imposto-de-renda-da-pessoa-fsica)

Análises exploratórias: [Análises exploratórias](https://github.com/hugoferraz5/brasil-rendimentos-isentos-e-nao-tributaveis/blob/main/analise_exploratoria_dos_dados.ipynb)

Análises explanatórias: [Análises explanatórias](https://github.com/hugoferraz5/brasil-rendimentos-isentos-e-nao-tributaveis/blob/main/analise_explanatoria_dos_dados.ipynb)

## Passo a passo para visualização do dashboard: 

1. **Instalar Python:**  

   Instalação do python no ambiente:
   ```bash
   sudo apt install python3
   ```  
   
2. **Criar ambiente virtual:**  

   No diretório do projeto:  

   ```bash
   python3 -m venv venv
   ```  

3. **Ativar o ambiente virtual no Linux:**   

     ```bash
     source venv/bin/activate
     ```  

4. **Instalar dependências do projeto:**
     
   Uso do requirements.txt

   ```bash
   pip install -r requirements.txt
   ```  

5. **Rodar o projeto:**
  
```bash
   streamlit run dashboard.py
   ```

## Ferramentas
- **Frontend**: Streamlit
- **Processamento de dados**: Pandas, NumPy
- **Visualização**: Plotly, Seaborn

## Imagens

![Visão Geral](https://github.com/user-attachments/assets/88828e3d-d7f7-4d19-b5bf-b85de6e3c433)
*Visão Geral*

#### Após escolher uma opção de rendimento:

![Gráfico 1](https://github.com/user-attachments/assets/4bfa5b28-80ab-4c06-b9ed-7471d89171cc)
*Gráfico 1*

![Gráfico 2](https://github.com/user-attachments/assets/dfadd998-fe9a-4b95-b87f-bf0be5aa1882)
*Gráfico 2*

![Gráfico 3](https://github.com/user-attachments/assets/34b518cd-9b64-4144-a5b0-17f7a4bf6a43)
*Gráfico 3*
