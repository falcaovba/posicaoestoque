
import pandas as pd
import streamlit as st
import altair as alt
import time as time
import datetime as datetime
from PIL import Image
from io import BytesIO
output = BytesIO()
import warnings
warnings.simplefilter("ignore")
import pymssql

arquivo = 'C:/Users/intel/Documents/OneDrive/Inteligencia/Estoque Pneus/posicao.xlsx'

df = pd.read_excel(arquivo)

## df_posicao DE ESTQUE ##
df_df_posicao = pd.DataFrame(df,columns=['LOJA','Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda','Estoque'])
## ------------------------------------------------------------------------------
df_01 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_101']
df_01.rename(columns={'Estoque':'1'}, inplace=True)
df_01.drop('LOJA',axis='columns', inplace=True)

df_05 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_105']
df_05.rename(columns={'Estoque':'5'}, inplace=True)
df_05.drop('LOJA',axis='columns', inplace=True)

df_06 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_106']
df_06.rename(columns={'Estoque':'6'}, inplace=True)
df_06.drop('LOJA',axis='columns', inplace=True)

df_17 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_17']
df_17.rename(columns={'Estoque':'17'}, inplace=True)
df_17.drop('LOJA',axis='columns', inplace=True)

df_04 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_104']
df_04.rename(columns={'Estoque':'4'}, inplace=True)
df_04.drop('LOJA',axis='columns', inplace=True)

df_19 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_119']
df_19.rename(columns={'Estoque':'19'}, inplace=True)
df_19.drop('LOJA',axis='columns', inplace=True)

df_13 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_113']
df_13.rename(columns={'Estoque':'13'}, inplace=True)
df_13.drop('LOJA',axis='columns', inplace=True)

df_15 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_115']
df_15.rename(columns={'Estoque':'15'}, inplace=True)
df_15.drop('LOJA',axis='columns', inplace=True)

df_02 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_02']
df_02.rename(columns={'Estoque':'2'}, inplace=True)
df_02.drop('LOJA',axis='columns', inplace=True)

df_09 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_09']
df_09.rename(columns={'Estoque':'9'}, inplace=True)
df_09.drop('LOJA',axis='columns', inplace=True)

df_16 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_116']
df_16.rename(columns={'Estoque':'16'}, inplace=True)
df_16.drop('LOJA',axis='columns', inplace=True)

df_03 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_03']
df_03.rename(columns={'Estoque':'3'}, inplace=True)
df_03.drop('LOJA',axis='columns', inplace=True)

df_07 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_107']
df_07.rename(columns={'Estoque':'7'}, inplace=True)
df_07.drop('LOJA',axis='columns', inplace=True)

df_08 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_108']
df_08.rename(columns={'Estoque':'8'}, inplace=True)
df_08.drop('LOJA',axis='columns', inplace=True)

df_10 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_10']
df_10.rename(columns={'Estoque':'10'}, inplace=True)
df_10.drop('LOJA',axis='columns', inplace=True)

df_20 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_20']
df_20.rename(columns={'Estoque':'20'}, inplace=True)
df_20.drop('LOJA',axis='columns', inplace=True)

df_14 = df_df_posicao[df_df_posicao['LOJA'] == 'LOJA_114']
df_14.rename(columns={'Estoque':'14'}, inplace=True)
df_14.drop('LOJA',axis='columns', inplace=True)
## ------------------------------------------------------------------------------
df1 = pd.merge(df_01, df_05, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df2 = pd.merge(df_06, df_17, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df3 = pd.merge(df_04, df_19, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df4 = pd.merge(df_13, df_15, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df5 = pd.merge(df_02, df_09, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df6 = pd.merge(df_16, df_03, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df7 = pd.merge(df_07, df_08, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df8 = pd.merge(df_10, df_20, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
## ------------------------------------------------------------------------------
df_posicao = pd.merge(df1, df2, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df_posicao = pd.merge(df_posicao, df3, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df_posicao = pd.merge(df_posicao, df4, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df_posicao = pd.merge(df_posicao, df5, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df_posicao = pd.merge(df_posicao, df6, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df_posicao = pd.merge(df_posicao, df7, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df_posicao = pd.merge(df_posicao, df8, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
df_posicao = pd.merge(df_posicao, df_14, how="left", left_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'],right_on=['Cod','Pneus','Fabricante','Medida','CustoRef','PrecoVenda'])
## ------------------------------------------------------------------------------
df_posicao['1'] = df_posicao ['1']. fillna (0)
df_posicao['5'] = df_posicao ['5']. fillna (0)
df_posicao['6'] = df_posicao ['6']. fillna (0)
df_posicao['17'] = df_posicao ['17']. fillna (0)
df_posicao['4'] = df_posicao ['4']. fillna (0)
df_posicao['19'] = df_posicao ['19']. fillna (0)
df_posicao['13'] = df_posicao ['13']. fillna (0)
df_posicao['15'] = df_posicao ['15']. fillna (0)
df_posicao['2'] = df_posicao ['2']. fillna (0)
df_posicao['9'] = df_posicao ['9']. fillna (0)
df_posicao['16'] = df_posicao ['16']. fillna (0)
df_posicao['3'] = df_posicao ['3']. fillna (0)
df_posicao['7'] = df_posicao ['7']. fillna (0)
df_posicao['8'] = df_posicao ['8']. fillna (0)
df_posicao['10'] = df_posicao ['10']. fillna (0)
df_posicao['20'] = df_posicao ['20']. fillna (0)
df_posicao['14'] = df_posicao ['14']. fillna (0)


# Com loja 02 e 10
df_pos = pd.DataFrame(df_posicao, columns=['Cod','Pneus','Medida','Fabricante','CustoRef','PrecoVenda','1','5','6','17','4','19','2','9','16','3','7','8','10','20','13','15','14'])
df_pos['PeçasTT'] = df_pos['1'] + df_pos['5'] + df_pos['6'] + df_pos['17'] + df_pos['4'] + df_pos['19'] + df_pos['2'] + df_pos['9'] + df_pos['16'] + df_pos['3'] + df_pos['7'] + df_pos['8'] +  df_pos['10'] +  df_pos['20'] +  df_pos['13'] +  df_pos['15'] +  df_pos['20']
df_pos['CustoTT'] = df_pos['PeçasTT']*df_pos['CustoRef']
df_pos.rename(columns={'CustoRef':'Custo','PrecoVenda':'Preço'}, inplace=True)

## Sem Loja 02 e 10
df_pos2 = pd.DataFrame(df_posicao, columns=['Cod','Pneus','Medida','Fabricante','CustoRef','PrecoVenda','1','5','6','17','4','19','9','16','3','7','8','20','13','15','14'])
df_pos2['PeçasTT'] = df_pos2['1'] + df_pos2['5'] + df_pos2['6'] + df_pos2['17'] + df_pos2['4'] + df_pos2['19'] + df_pos2['9'] + df_pos2['16'] + df_pos2['3'] + df_pos2['7'] + df_pos2['8'] +  df_pos2['20'] +  df_pos2['13'] +  df_pos2['15'] +  df_pos2['20']
df_pos2['CustoTT'] = df_pos2['PeçasTT']*df_pos2['CustoRef']
df_pos2.rename(columns={'CustoRef':'Custo','PrecoVenda':'Preço'}, inplace=True)

## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------


## Configuração da Página
st.set_page_config(
    page_title="Posição de Estoque",
    page_icon="📶",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://api.whatsapp.com/send?phone=5581997518612',
        #'Report a bug': "https://api.whatsapp.com/send?phone=5581997518612",
        'About': "# Posição de estoque Dafonte Pneus"
    }
)

    ## Logo e Cabeçalho
logo_teste = Image.open('C:/Users/intel/Documents/OneDrive/Inteligencia/Estoque Pneus/imagens/LogoDafonte.jpg')
colA, colB = st.columns([1,9])
colA.image(
    logo_teste,
    width=150
)
colB.header(
    ':clipboard: :blue[Estoque]',
    divider='blue'
)


DFabricante = st.selectbox(
    "Fabricante:", 
    options=df_df_posicao['Fabricante'].unique(),
    #options=['PIRELLI','SESTANTE','ANTEO','CASUMINA','ADVANCE','LING LONG','DOUBLE STAR','MERIDIONAL','VIPAL','JINYU','JK TYRE','MAGNUM','ROADX', 'SPEED MAX', 'X-BRI', 'WESTLAKE',' VIKRANT'],
    index=16,
    placeholder="Selecione o fabricante...")
DMedida = st.selectbox(
    "Medida:", 
    options=df_df_posicao['Medida'].unique(),
    index=None,
    placeholder="Selecione a medida..."
    
    )
st.markdown("---")

if DMedida == None:
    df_posic = df_pos2.loc[(df_pos2['Fabricante'] == DFabricante)]
elif  DFabricante == None and DMedida == None:
    df_posic = df_pos2
elif  DFabricante == None:
    df_posic = df_pos2.loc[(df_pos2['Medida'] == DMedida)] 
else:
    df_posic = df_pos2.loc[(df_pos2['Fabricante'] == DFabricante) & (df_pos2['Medida'] == DMedida)]  
    

df_posic = pd.DataFrame(df_posic, columns=['Cod','Pneus','Fabricante','Custo','Preço','1','5','6','17','4','19','9','16','3','7','8','20','13','15','14','PeçasTT','CustoTT'])   
df_posic.rename(columns={'1':'1-PE','5':'5-PE','6':'6-PE','17':'17-PE','4':'4-BA','19':'19-BA','9':'9-AL','16':'16-AL','3':'3-PB','7':'7-PB','8':'8-PB','20':'20-PB','13':'13-CE','15':'15-CE','14':'14-RN'}, inplace=True)


## Tabela
st.dataframe(
        df_posic,
        use_container_width=True,
        width=600,
        hide_index=True,
        column_config={
            "widgets": st.column_config.Column(
                width="medium"
            )
        }
    )

st.markdown("---")

ttCusto = "{:,}".format(round(df_posic['CustoTT'].sum()))


col1, col2 = st.columns(2)
col1.metric("TT Custo", f'R$ {ttCusto}')
col2.metric("TT Peças", round(df_posic['PeçasTT'].sum()))

st.markdown("---")

from io import BytesIO
import streamlit as st

def to_excel(df_posic: pd.DataFrame):
    in_memory_fp = BytesIO()
    df_posic.to_excel(in_memory_fp,index=False)
    # Write the file out to disk to demonstrate that it worked.
    in_memory_fp.seek(0, 0)
    return in_memory_fp.read()

#cols = ["col1", "col2"]
#df = pd.DataFrame.from_records([{k: 0.0 for k in cols} for _ in range(25)])
excel_data = to_excel(df_posic)
file_name = f"Estoque - {DFabricante}.xlsx"
st.download_button(
    f"Download -  {DFabricante}",
    excel_data,
    file_name,
    f"text/{file_name}",
    key=file_name
)
st.caption('Baixar a consuta')

