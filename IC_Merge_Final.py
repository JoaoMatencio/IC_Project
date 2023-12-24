import pandas as pd
import os as os
import openpyxl

def main():
    path = 'C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/'
    path_docs = path + 'Doc_17_12_23/'
    path_final = path + 'Final_Reversal_56/'
    path_final_merge = path + 'Final/'
    if not os.path.exists(path_final_merge):
        os.makedirs(path_final_merge)
    df_docs = pd.read_excel(f'{path_docs}Subject_Questionaire_Experimental_Record_Merge.xlsx',index_col=False)
    df_docs['Nome do arquivo'] = df_docs['Nome do arquivo'] +'.xlsx'
    df_final = pd.read_excel(f'{path_final}Merge_Date_Reversal.xlsx',index_col=False)
    df = pd.merge(df_docs, df_final, on='Nome do arquivo')
    df = df.drop_duplicates()
    df.reset_index(inplace=True)
    df = df.drop(['Unnamed: 0', 'index','Carimbo de data/hora', 'Nome completo do responsável legal do(a) menor','Nome completo do responsável legal do(a) menor', 'Nome completo do responsável legal do(a) menor','Celular (DDD) do responsável legal','Grau de escolaridade do responsável legal:','Grau de parentesco do responsável legal com o(a) menor','E-mail do responsável legal','Turma do menor','Nome','Sessão','Nome do arquivo','Idade','Subject_name','Subject_id','expName'], axis=1)
    df['Data'] = pd.to_datetime(df['Data'])
    x = df['Data de nascimento do(a) menor (formato: dd/mm/aaaa):']
    x = pd.to_datetime(x)
    y = df['Data']
    y = pd.to_datetime(y)
    df['Idade No Dia do Teste'] = y - x
    df['Idade No Dia do Teste'] = df['Idade No Dia do Teste'].dt.days
    df['Idade No Dia do Teste'] = df['Idade No Dia do Teste']/365
    df['Idade No Dia do Teste Fracionada'] = df['Idade No Dia do Teste'].round(2)
    df['Idade No Dia do Teste'] = df['Idade No Dia do Teste'].apply(lambda x: x// 1)
    df.to_excel(f'{path_final_merge}Merge_Final.xlsx')

if __name__ == '__main__':
    main()