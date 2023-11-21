
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
## ------------------------------------------------------------------------------

def load_data():
    conn = pymssql.connect(
        server='10.0.1.5',
        user='dafonte',
        password='@d123',
        database='DBDafonte',
        as_dict=True
    )
    SQL_QUERY = """

            SELECT
            a.LOJA,
            CAST(a.EPRCOD as varchar) as Cod, 
            REPLACE(TRIM(a.EPRDESCRICAO),'PNEU ','') as Pneus,
            TRIM(REPLACE(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO)))),'C','')) AS Medida,
            CASE 
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1200R24' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1200R24' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1200R20' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1200R20' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1100R22' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1100R22' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1000R20' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1000R20' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '900R20' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '900R20' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '385/65R22.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '385/65R22.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '315/80R22.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '315/80R22.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '285/70R19.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '285/70R19.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '235/75R17.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '235/75R17.5'  THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '295/80R22.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '295/80R22.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '275/70R22.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '275/70R22.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '275/80R22.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '275/80R22.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '215/75R17.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '215/75R17.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1100R20' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '1100R20' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '11R22.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '11R22.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '12R22.5' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '12R22.5' THEN 'GIGANTE RADIAL - Importado'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '325/95R24' AND TRIM(a.FABRICANTE) in ('PIRELLI','SESTANTE','ANTEO','FORMULA') THEN 'GIGANTE RADIAL - Nacional'
                when TRIM(SUBSTRING(SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO),len(a.EPRDESCRICAO)),1,CHARINDEX(' ',SUBSTRING(a.EPRDESCRICAO,CHARINDEX(' ', a.EPRDESCRICAO)+1,len(a.EPRDESCRICAO))))) = '325/95R24' THEN 'GIGANTE RADIAL - Importado'	
                ELSE
                    (CASE 
                        WHEN TRIM(a.ESGDESCR) = 'RLI IMPORTADOS' THEN 'IMPORTADOS'
                        ELSE TRIM(a.ESGDESCR)
                    END)
            END Família,
            TRIM(a.ESGDESCR) as Grupo,
            TRIM(a.FABRICANTE) as Fabricante,
            a.EPRSALDO as Estoque,
            ROUND(a.EPRREFCUST,0) as CustoRef,
            a.EPRMEDCUST as CustoMéd,
            ROUND(a.VLRVENDA1,0) AS PrecoVenda,
            CASE 	
                when a.EPRREFCUST = 0 or a.VLRVENDA1 = 0 then 0
                else round((a.VLRVENDA1-a.EPRREFCUST)/a.VLRVENDA1,4) 
            END as MGB,
            a.EPRULT_AQUIS as DataEntrada, 
            a.EPRULT_SAIDA as DataSaída,
            CASE 
                WHEN a.EPRULT_SAIDA IS NULL THEN DATEDIFF(DAY , a.EPRULT_AQUIS, GETDATE())
                ELSE DATEDIFF(DAY , a.EPRULT_SAIDA, GETDATE())
            END AS DiasSemSaída,
            DATEDIFF(DAY , a.EPRULT_AQUIS, GETDATE()) AS DiasUltEntrada
            FROM DbDafonte.dbo.VW_ESTOQUE_SALDO a
            WHERE a.EGRDES = 'PNEUS NOVOS'
            AND a.LOJA NOT IN ('LOJA_01','LOJA_04','LOJA_05','LOJA_06','LOJA_07','LOJA_08','LOJA_109','LOJA_12','LOJA_13','LOJA_14','LOJA_15','LOJA_16')

                """
            
    cursor = conn.cursor()
    df = cursor.execute(SQL_QUERY)
    df = pd.DataFrame(df) 
    return df

## Carregamento do DataFrame
df = load_data()

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
logo_teste = Image.open('LogoDafonte.jpg')
colA, colB = st.columns([1,8])
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
    index=15,
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

